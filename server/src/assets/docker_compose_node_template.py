DOCKER_COMPOSE_NODE = '''
  {0}:
    image: quorumengineering/quorum
    container_name: {0}
    ports:
      - "2100{1}:21000"
      - "2200{1}:22000"
      - "5040{2}:50401"
    volumes:
      - ./{0}:/data
      - ./{0}:/tls
      - ./genesis.json:/genesis.json
      - ./static-nodes.json:/data/static-nodes.json
    entrypoint: ["/bin/sh", "/tls/start.sh"]'''