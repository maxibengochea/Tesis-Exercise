from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
from src.services.network import Network
import os

class Client:
  def __init__(self, organization_name='', common_name='', country='CU', state='La Habana', locality='Playa', ):
    self._common_name = common_name
    self._private_key = self._create_private_key()
    self._hex_public_key = self._create_hex_public_key() #llave publica en formato hexadecimal
    self._country = country
    self._state = state
    self._locality = locality
    self._organization_name = organization_name

  def _create_private_key(self):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    #guardar la clave privada
    os.makedirs(f'quorum-network/node{Network.client_number}', exist_ok=True)

    with open(os.path.join(f'quorum-network/node{Network.client_number}', "private_key.pem"), "wb") as f:
        f.write(key.private_bytes(encoding=serialization.Encoding.PEM, 
                                  format=serialization.PrivateFormat.TraditionalOpenSSL, 
                                  encryption_algorithm=serialization.NoEncryption()))
        
    return key
  
  #emitir un csr
  def issue_csr(self):
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, self._country),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, self._state),
        x509.NameAttribute(NameOID.LOCALITY_NAME, self._locality),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, self._organization_name),
        x509.NameAttribute(NameOID.COMMON_NAME, self._common_name),
    ])).sign(self._private_key, hashes.SHA256())
  
    #guardar la clave privada y el CSR
    csr_path = os.path.join("CA", f"{self._common_name}_csr.pem")

    with open(csr_path, "wb") as f:
      f.write(csr.public_bytes(serialization.Encoding.PEM))

    print(f"CSR emited by {self._common_name}")
    return csr_path

  def _create_hex_public_key(self):
    #extraer la clave pública
    public_key = self._private_key.public_key()

    #serializar la clave pública en formato hexadecimal para usarla en el enode
    public_key_bytes = public_key.public_bytes( encoding=serialization.Encoding.DER,
                                               format=serialization.PublicFormat.SubjectPublicKeyInfo)

    #convertir a hexadecimal (sin encabezado DER)
    return public_key_bytes.hex()

  @property
  def common_name(self): return self._common_name
  @property
  def hex_public_key(self): return self ._hex_public_key
