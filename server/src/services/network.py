from src.assets.start_node_template import START
from src.assets.docker_compose_node_template import DOCKER_COMPOSE_NODE
from src.assets.genesis_template import GENESIS

class Network:
  _public_keys: list[str] = []
  client_number = 1

  @classmethod
  def config_start_node(cls, public_key: str):
    #agreagar la llave publica de cada node
    cls._public_keys.append(public_key)

    #obtener node_name del nodo y el node number
    node_name = f'node{cls.client_number}'
    node_number = int(node_name[4:])

    #configurar start.sh
    with open(f'quorum-network/{node_name}/start.sh', 'w') as f:
      f.write(START.format(node_number, node_number - 1))
      
    #configurar genesis.json
    with open(f'quorum-network/{node_name}/genesis.json', 'w') as f:
      f.write(GENESIS)
      
    cls.client_number += 1

  @classmethod
  def config_docker_compose(cls):
    content = 'version: "3.8"\n\n'
    content += 'services:\n'

    for i in range(len(cls._public_keys)):
      #obtener common_name del nodo y el node number
      node_name = f'node{i + 1}'
      node_number = int(node_name[4:])

      content += DOCKER_COMPOSE_NODE.format(node_name, node_number - 1, node_number)
      content += '\n'

    with open('quorum-network/docker-compose.yml', 'w') as f:
      f.write(content)

  @classmethod
  def config_enode(cls):
    content = '[\n'

    for i in range(len(cls._public_keys)):
      #obtener common_name del nodo y el node number
      node_name = f'node{i + 1}'
      public_key = cls._public_keys[i]
      content += f' "enode://{public_key}@{node_name}:21000"{',' if i != len(cls._public_keys) - 1 else ''}\n'

    content += ']\n'

    with open('quorum-network/static-nodes.json', 'w') as f:
      f.write(content)
