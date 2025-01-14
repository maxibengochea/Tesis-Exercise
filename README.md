# Como correr la app

## Instalación de dependencias
- pip install -r server/requirements.txt
- cd ui (navegar a la ruta de la ui)
- npm install

## Ejecutar en el directorio raíz: 
- chmod +x start.sh
- ./start.sh

## Movernos al directorio de quorum-network para trabajar con la blockchain a través de docker (EJEMPLO CON 3 NODOS)
- cd quorum-network

## Inicializar la red de Quorum con el protocolo de consenso QBFT
- chmod +x start_network.sh
- ./start_network.sh

## Mover los archivos a la raíz de artifacts
- mv artifacts/[nombre de la carpeta generada]/* artifacts

## Actualizar los archivos enode en static-nodes.json
- En la ruta artifacts/goQuorum/static-nodes.json, actualizar cada ip con el nombre del contenedor y el puerto de cada nodo así como su raftport con las terminales del nombre del contenedor

## Crear las rutas de cada nodo
- mkdir -p node0/data/keystore
- mkdir -p node1/data/keystore
- mkdir -p node2/data/keystore

## Copiar el contenido de static-nodes.json y genesis.json en cada nodo
- cp artifacts/goQuorum/static-nodes.json artifacts/goQuorum/genesis.json node0/data
- cp artifacts/goQuorum/static-nodes.json artifacts/goQuorum/genesis.json node1/data
- cp artifacts/goQuorum/static-nodes.json artifacts/goQuorum/genesis.json node2/data

## En el directorio de cada validator, copiar el contenido las key y address en el data de su respectivo nodo
- cp artifacts/validator0/nodekey* artifacts/validator0/address node0/data
- cp artifacts/validator1/nodekey* artifacts/validator1/address node1/data
- cp artifacts/validator2/nodekey* artifacts/validator2/address node2/data

## En el directorio de cada validator, copiar el contenido las account en el data de su respectivo nodo
- cp artifacts/validator0/account* node0/data/keystore
- cp artifacts/validator1/account* node1/data/keystore
- cp artifacts/validator2/account* node2/data/keystore

## Levantar la red
- docker compose up -d