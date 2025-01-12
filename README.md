# Como correr la app

## Instalación de dependencias
- pip install -r server/requirements.txt
- cd ui (navegar a la ruta de la ui)
- npm install

## Ejecutar en el directorio raíz: 
- chmod +x start.sh
- start.sh

## Movernos al directorio de quorum-network para trabajar con la blockchain a través de docker
- cd quorum-network

## Inicializar cada node de la blockchain con el archivo genesis.json (ejemplo con 3 nodos)
- docker run --rm -v $(pwd)/node1:/data quorumengineering/quorum init /data/genesis.json
- docker run --rm -v $(pwd)/node2:/data quorumengineering/quorum init /data/genesis.json
- docker run --rm -v $(pwd)/node3:/data quorumengineering/quorum init /data/genesis.json

## Levantar la red
- docker compose up -d