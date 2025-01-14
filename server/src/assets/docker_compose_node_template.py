DOCKER_COMPOSE_NODE = '''
  {0}:
    image: quorumengineering/quorum
    container_name: {0}
    ports:
      - "3030{1}:3030{1}"
      - "2200{1}:2200{1}"
      - "5040{1}:5040{1}"
    volumes:
      - ./{0}:/data
    entrypoint: ["/bin/sh", "/data/run.sh"]'''