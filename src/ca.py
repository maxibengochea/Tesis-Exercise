from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta, timezone
from cryptography.hazmat.primitives import serialization, hashes
import os

# Directorios para guardar los certificados y claves
ROOT_CERT_DIR = "src/assets/root_cert"
CERTS_DIR = "src/assets/certs"
os.makedirs(ROOT_CERT_DIR, exist_ok=True)
os.makedirs(CERTS_DIR, exist_ok=True)

class CA:
  def __init__(self):
    self._private_key = self._create_private_key()
    self._public_key = self._private_key.public_key()
    self._identity = self._create_identity()
    self._create_certificate(self._identity, root=True) #crear certificado autofirmado

  def _create_private_key(self):
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)
  
  def _create_identity(self):
    return x509.Name([
      x509.NameAttribute(NameOID.COUNTRY_NAME, "CU"),
      x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "La Habana"),
      x509.NameAttribute(NameOID.LOCALITY_NAME, "Playa"),
      x509.NameAttribute(NameOID.ORGANIZATION_NAME, "HumanToilet CA"),
      x509.NameAttribute(NameOID.COMMON_NAME, "humantoilet-ca.com"),
    ])
  
  def _create_certificate(self, subject: x509.Name, root=False):
    #ruta del certificado
    cert_dir = os.path.join(ROOT_CERT_DIR, "ca_cert.pem") if root else os.path.join(CERTS_DIR, f"{subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}_cert.pem") 

    certificate = x509.CertificateBuilder()
    certificate = certificate.subject_name(subject)
    certificate = certificate.issuer_name(self._identity)
    certificate = certificate.public_key(self._public_key)
    certificate = certificate.serial_number(x509.random_serial_number())
    certificate = certificate.not_valid_before(datetime.now(timezone.utc))
    certificate = certificate.not_valid_after(datetime.now(timezone.utc) + timedelta(days=3650))
    certificate = certificate.add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
    certificate = certificate.sign(self._private_key, hashes.SHA256())

    #guardar la clave privada
    with open(os.path.join(ROOT_CERT_DIR, "ca_key.pem"), "wb") as f:
        f.write(self._private_key.private_bytes(encoding=serialization.Encoding.PEM, 
                                                format=serialization.PrivateFormat.TraditionalOpenSSL, 
                                                encryption_algorithm=serialization.NoEncryption()))

    #guardar el certificado
    with open(os.path.join(cert_dir), "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))

    print(f"Certificate emited to {subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}")

  def issue_certificate(self, csr_path: str):
    #cargar el CSR del cliente
    with open(csr_path, "rb") as f:
      csr = x509.load_pem_x509_csr(f.read())

    #crear el certificado firmado por la CA
    self._create_certificate(csr.subject)

    with open(os.path.join(ROOT_CERT_DIR, "ca_cert.pem"), "rb") as f:
      certificate = x509.load_pem_x509_certificate(f.read())

    return {
      'message': 'Succesful operation',
      'certificate': str(certificate)
    }
