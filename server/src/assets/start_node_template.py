START = '''export PRIVATE_CONFIG=ignore
geth --datadir data 
    --networkid 1337 --nodiscover --verbosity 5 
    --syncmode full 
    --istanbul.blockperiod 5 --mine --miner.threads 1 --miner.gasprice 0 --emitcheckpoints 
    --http --http.addr {1} --http.port 2200{0} --http.corsdomain "*" --http.vhosts "*" 
    --ws --ws.addr {1} --ws.port 3200{0} --ws.origins "*" 
    --http.api admin,eth,debug,miner,net,txpool,personal,web3,istanbul 
    --ws.api admin,eth,debug,miner,net,txpool,personal,web3,istanbul 
    --unlock $(grep -o '"address": *"[^"]*"' ./data/keystore/accountKeystore | grep -o '"[^"]*"$' | sed 's/"//g') --allow-insecure-unlock --password ./data/keystore/accountPassword 
    --port 3030{0}
    --tlskeyfile "/tls/private_key.pem" 
    --tlscertfile "/tls/cert.pem" 
    --tlsca "/tls/root_cert.pem"'''

INIT = '''geth --datadir data init data/data/genesis.json'''