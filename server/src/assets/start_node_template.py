START = '''export PRIVATE_CONFIG=ignore
  geth --datadir data/data
      --networkid 1337 --nodiscover --verbosity 5 
      --syncmode full
      --istanbul.blockperiod 5 --mine --miner.threads 1 --miner.gasprice 0 --emitcheckpoints
      --http --http.addr 0.0.0.0 --http.port 8545 --http.corsdomain "*" --http.vhosts "*" 
      --ws --ws.addr 0.0.0.0 --ws.port 8546 --ws.origins "*" 
      --http.api admin,eth,debug,miner,net,txpool,personal,web3,istanbul 
      --ws.api admin,eth,debug,miner,net,txpool,personal,web3,istanbul 
      --unlock {0} --allow-insecure-unlock
      --ptm.tls.mode strict --ptm.tls.rootca data/data/tls/root_cert.pem --ptm.tls.clientcert data/data/tls/cert.pem --ptm.tls.clientkey data/data/tls/private_key.pem --ptm.tls.insecureskipverify
      --port 30303'''

INIT = '''geth --datadir data/data init data/data/genesis.json'''
