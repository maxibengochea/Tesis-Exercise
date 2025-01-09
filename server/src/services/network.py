from src.assets.start_node_template import START
from src.assets.docker_compose_node_template import DOCKER_COMPOSE_NODE

class Network:
  _nodes: list[str] = []

  @classmethod
  def config_start_node(cls, node: str):
    #agregar el nodo a la lista de nodos
    cls._nodes.append(node)

    #parsing node number
    node_number = int(node[4:])

    #config start.sh
    with open(f'quorum-network/{node}/start.sh', 'w') as f:
      f.write(START.format(node_number))

  @classmethod
  def config_docker_compose(cls):
    content = 'version: "3.8"\n'
    content += 'services:\n'

    for node in cls._nodes:
      #parsing node number
      node_number = int(node[4:])

      content += DOCKER_COMPOSE_NODE.format(node, node_number - 1, node_number)
      content += '\n'

    with open('quorum-network/docker-compose.yml', 'w') as f:
      f.write(content)