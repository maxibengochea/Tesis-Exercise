from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta, timezone
from cryptography.hazmat.primitives import serialization, hashes
from src.services.network import Network
import os

# Directorios para guardar los certificados y claves
CA_ROOT = 'CA'
DB_ROOT =  f'{os.getcwd()}/server/src/db.txt'
os.makedirs(CA_ROOT, exist_ok=True)

class CA:
  def __init__(self):
    self._private_key = self._create_private_key()
    self._public_key = self._private_key.public_key()
    self._identity = self._create_identity()
    self._root_cert = self._create_certificate(self._identity, root=True) #crear certificado autofirmado

  def _create_private_key(self):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    #guardar la clave privada
    with open(os.path.join(CA_ROOT, "private_key.pem"), "wb") as f:
        f.write(key.private_bytes(encoding=serialization.Encoding.PEM, 
                                  format=serialization.PrivateFormat.TraditionalOpenSSL, 
                                  encryption_algorithm=serialization.NoEncryption()))
        
    return key
  
  def _create_identity(self):
    return x509.Name([
      x509.NameAttribute(NameOID.COUNTRY_NAME, "CU"),
      x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "La Habana"),
      x509.NameAttribute(NameOID.LOCALITY_NAME, "Playa"),
      x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Sex Company"),
      x509.NameAttribute(NameOID.COMMON_NAME, "humantoilet-ca"),
    ])
  
  def _create_certificate(self, subject: x509.Name, client_key=None, root=False):
    #ruta del certificado
    cert_dir = os.path.join(CA_ROOT, "root_cert.pem") if root else os.path.join(f"quorum-network/node{Network.client_number}/tls", "cert.pem") 

    #crear el certifcado
    certificate = x509.CertificateBuilder()
    certificate = certificate.subject_name(subject)
    certificate = certificate.issuer_name(self._identity)
    certificate = certificate.public_key(self._public_key)
    certificate = certificate.serial_number(x509.random_serial_number())
    certificate = certificate.not_valid_before(datetime.now(timezone.utc))
    certificate = certificate.not_valid_after(datetime.now(timezone.utc) + timedelta(days=3650))
    certificate = certificate.add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
    certificate = certificate.sign(self._private_key, hashes.SHA256())

    if root:
      #guardar el certificado
      with open(cert_dir, "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))

    else:    
      self._add_client(client_key)

      #guardar el certificado
      with open(cert_dir, "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))

      #si no es el certificado raiz guardarlo tambien en la CA
      with open(f'{CA_ROOT}/{subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}_cert.pem', "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))
    
      #si no es el certificado raiz entonces guardar tambien el certificado raiz
      with open(cert_dir.replace('cert.pem', 'root_cert.pem'), "wb") as f:
        f.write(self._root_cert.public_bytes(serialization.Encoding.PEM))
        
    print(f"Certificate emited to {subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}")
    return True if not root else certificate

  def issue_certificate(self, data: dict):
    #cargar el CSR del cliente
    subject = data['csr'].subject

    #validar que el csr no haya sido emitido
    with open(DB_ROOT, 'r') as f:
      if f'{subject.get_attributes_for_oid(NameOID.ORGANIZATION_NAME)[0].value} - {subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}\n' in f.readlines():
        return False
    
    #agregar la solicitud a la db
    with open(DB_ROOT, 'a') as f:
      f.write(f'{subject.get_attributes_for_oid(NameOID.ORGANIZATION_NAME)[0].value} - {subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}\n')

    #agregar el csr a la ca
    self._add_csr(data['csr'])
    
    #crear el certificado firmado por la CA
    return self._create_certificate(subject, data['key'])
  
  def _add_client(self, key: rsa.RSAPrivateKey):
    #guardar la clave privada del cliente
    os.makedirs(f'quorum-network/node{Network.client_number}/tls', exist_ok=True)

    with open(os.path.join(f'quorum-network/node{Network.client_number}/tls', "private_key.pem"), "wb") as f:
        f.write(key.private_bytes(encoding=serialization.Encoding.PEM, 
                                  format=serialization.PrivateFormat.TraditionalOpenSSL, 
                                  encryption_algorithm=serialization.NoEncryption()))
        
  def _add_csr(self, csr):
    #guardar la clave privada y el CSR
    csr_path = os.path.join("CA", f"{csr.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}_csr.pem")

    with open(csr_path, "wb") as f:
      f.write(csr.public_bytes(serialization.Encoding.PEM))

    print(f"CSR emited by {csr.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}")

ca = CA()