DOCKER_COMPOSE_NODE = '''
  {0}:
    image: quorumengineering/quorum
    container_name: {0}
    ports:
      - "3030{1}:30303"
      - "854{1}:8545"
      - "864{1}:8546"
    volumes:
      - ./quorum-network/{0}:/data
    entrypoint: ["/bin/sh", "/data/run.sh"]'''