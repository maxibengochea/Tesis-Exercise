from src.assets.start_template import START

class Quorum:
  @classmethod
  def config_start_node(cls, node: str):
    #parsing node number
    node_number = int(node[4:])

    #config start.sh
    with open(f'quorum-network/{node}/start.sh', 'w') as f:
      f.write(START.format(node_number))

      