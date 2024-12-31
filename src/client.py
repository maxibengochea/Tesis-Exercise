from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
import os

#crear el directorio para guardar el csr del cliente
CSRS_DIR = "src/assets/csrs"
os.makedirs(CSRS_DIR, exist_ok=True)

class Client:
  def __init__(self, country: str, state: str, locality: str, organization_name: str, common_name: str):
    self._private_key = self._create_private_key()
    self._country = country
    self._state = state
    self._locality = locality
    self._organization_name = organization_name
    self._common_name = common_name

  def _create_private_key(self):
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)
  
  #emitir un csr
  def issue_csr(self):
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, self._country),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, self._state),
        x509.NameAttribute(NameOID.LOCALITY_NAME, self._locality),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, self._organization_name),
        x509.NameAttribute(NameOID.COMMON_NAME, self._common_name),
    ])).sign(self._private_key, hashes.SHA256())
  
    #guardar la clave privada y el CSR en disco
    csr_path = os.path.join(CSRS_DIR, f"{self._common_name}_csr.pem")

    with open(csr_path, "wb") as f:
      f.write(csr.public_bytes(serialization.Encoding.PEM))

    print(f"CSR generado para {self._common_name}")
    return csr_path