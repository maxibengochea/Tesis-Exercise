from src.assets.start_node_template import START, INIT
from src.assets.docker_compose_node_template import DOCKER_COMPOSE_NODE
from src.assets.start_network_template import START_NETWORK

class Network:
  client_number = 0

  @classmethod
  def config_start_node(cls):
    #obtener node_name del nodo y el node number
    node_name = f'node{cls.client_number}'
    node_number = int(node_name[4:])

    content = f'{INIT} & \n\nwait\n\n'
    content += START.format(node_number, node_name)

    #configurar run.sh
    with open(f'quorum-network/{node_name}/run.sh', 'w') as f:
      f.write(content)
      
    cls.client_number += 1

  @classmethod
  def config_docker_compose(cls):
    content = 'version: "3.8"\n\n'
    content += 'services:\n'

    for i in range(cls.client_number):
      #obtener common_name del nodo y el node number
      node_name = f'node{i}'

      content += DOCKER_COMPOSE_NODE.format(node_name, i)
      content += '\n'

    with open('quorum-network/docker-compose.yml', 'w') as f:
      f.write(content)

  @classmethod
  def config_start_network(cls):
    with open('quorum-network/start_network.sh', 'w') as f:
      f.write(START_NETWORK.format(cls.client_number))