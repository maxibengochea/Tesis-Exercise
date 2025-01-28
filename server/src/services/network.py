from src.assets.start_node_template import START, INIT
from src.assets.docker_compose_node_template import DOCKER_COMPOSE_NODE
from src.assets.genesis_template import GENESIS
from eth_account import Account
from web3 import Web3

class EtheriumAccount():
  def __init__(self, private_key: str, public_key: str, address: str):
    self._public_key = public_key
    self._address = address
    self._private_key = private_key

  @classmethod
  def export(cls):
    while True:
      #crear una nueva cuenta
      account = Account.create()

      #obtener la dirección
      address = account.address

      #verificar si la dirección es válida
      if not Web3.is_checksum_address(address):
        continue

      #obtener la clave privada y la clave publica y devolver el objeto
      private_key = account.key.hex() 
      public_key = account._key_obj.public_key
      return EtheriumAccount(str(private_key), str(public_key), str(address))

  @property
  def private_key(self): return self._private_key
  @property
  def public_key(self): return self._public_key
  @property
  def address(self): return self._address

class Network:
  client_number = 0
  _accounts: list[EtheriumAccount] = []

  @classmethod
  def add_conn(cls):
    account = EtheriumAccount.export()
    cls._accounts.append(account)
    cls._config_start_node()
    cls.client_number += 1

  @classmethod
  def _config_start_node(cls):
    #obtener node_name del nodo y el node number
    node_name = f'node{cls.client_number}'
    account = cls._accounts[-1]

    content = f'{INIT} & \n\nwait\n\n'
    content += START.format(account.address[2:])

    #configurar run.sh
    with open(f'quorum-network/{node_name}/run.sh', 'w') as f:
      f.write(content)

    #configurar la cuenta de los validadores de Etherium
    account_address = f'quorum-network/{node_name}/data/keystore/accountAdrress'
    address = account.address[2:]

    with open(f'quorum-network/{node_name}/data/address', 'w') as f:
      f.write(address)
    
    with open(account_address, 'w') as f:
      f.write(address)

    #configurar la llave privada de la cuenta
    with open(f'quorum-network/{node_name}/data/nodekey', 'w') as f:
      f.write(account.private_key)
    
    #configurar la llave publica de la cuenta
    with open(f'quorum-network/{node_name}/data/nodekey.pub', 'w') as f:
      f.write(account.public_key[2:])

    #

  @classmethod
  def config_docker_compose(cls):
    content = 'version: "3.8"\n\n'
    content += 'services:\n'

    for i in range(cls.client_number):
      #obtener common_name del nodo y el node number
      node_name = f'node{i}'

      content += DOCKER_COMPOSE_NODE.format(node_name, i)
      content += '\n'

    with open('docker-compose.yml', 'w') as f:
      f.write(content)
  
  #configurar genesis.json y static-nodes.json
  @classmethod
  def config_json(cls):
    content_enodes = '[\n'
    content_alloc = ''

    for i in range(cls.client_number):
      account = cls._accounts[i] #tomar el cuenta eth
      alloc = _generate_alloc(account.address) #generar el alloc del genesis.json
      enode_url = account.public_key[2:] #parsear el enode_url
      content_enodes += f'  "enode://{enode_url}@node{i}:30303?discport=0&raftport=5300{i}"{"," if i != cls.client_number - 1 else ""}\n'
      content_alloc += f'{alloc}{"," if i != cls.client_number - 1 else ""}\n'

    content_enodes += ']\n'

    #agregar el static-nodes.json en cada nodo
    for i in range(cls.client_number):
      #crear el node name
      node_name = f'node{i}'

      with open(f'quorum-network/{node_name}/data/static-nodes.json', 'w') as f:
        f.write(content_enodes)

      #configurar genesis.json en cada nodo
      with open(f'quorum-network/{node_name}/data/genesis.json', 'w') as f:
        f.write(GENESIS.replace('alloc_content', content_alloc))

def _generate_alloc(address: str):
  content = f'    "{address}": '
  content += '{ "balance": "1000000000000000000000000000" }'
  return content
