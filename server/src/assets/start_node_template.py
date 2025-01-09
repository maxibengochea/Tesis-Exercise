START = '''
  geth --datadir /data \
    --networkid 10 \
    --raft \
    --raftport 5040{0} \
    --rpc \
    --rpcaddr "0.0.0.0" \
    --rpcport 2200{0} \
    --rpcapi "admin,eth,debug,miner,net,txpool,personal,web3" \
    --port 2100{0} \
    --nodiscover \
    --tlskeyfile "/tls/private_key.pem" \
    --tlscertfile "/tls/cert.pem" \
    --tlsca "/tls/root_cert.pem"'''