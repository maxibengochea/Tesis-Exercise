START = '''#iniciar el nodo en la blockchain
export PRIVATE_CONFIG=ignore
  geth --datadir data/data
      --networkid 1337 --nodiscover --verbosity 5 
      --syncmode full
      --istanbul.blockperiod 5 --mine --miner.threads 1 --miner.gasprice 0 --emitcheckpoints
      --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.vhosts "*" 
      --ws --ws.addr 0.0.0.0 --ws.port 8546 --ws.origins "*" 
      --http.api admin,eth,debug,miner,net,txpool,personal,web3,istanbul 
      --ws.api admin,eth,debug,miner,net,txpool,personal,web3,istanbul 
      --unlock {0} --allow-insecure-unlock
      --ptm.tls.mode "strict" --ptm.tls.rootca data/data/tls/root_cert.pem --ptm.tls.clientcert data/data/tls/cert.pem --ptm.tls.clientkey data/data/tls/private_key.pem
      --port 30303'''

INIT = '''#iniciar el node genesis
geth --datadir data/data init data/data/genesis.json'''

VALIDATIONS = '''#verificar que los certificados no fueron alterados o son invalidos
VALIDATION_CERT=$(openssl verify -CAfile data/data/tls/root_cert.pem data/data/tls/cert.pem)

if [ ! "$VALIDATION_CERT" ]; then
  echo "Invalid cert or corrupted root cert"
  exit 1

fi 

wait

#verificar que la llave privada no fue alterada
CERT_MODULUS=$(openssl x509 -noout -modulus -in data/data/tls/cert.pem)
KEY_MODULUS=$(openssl rsa -noout -modulus -in data/data/tls/private_key.pem)

if [ "$CERT_MODULUS" != "$KEY_MODULUS" ]; then
    echo "Certifcate missmatch with private key"
    exit 1

fi'''