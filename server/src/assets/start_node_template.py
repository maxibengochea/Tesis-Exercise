START = '''
  geth --datadir /data \
    --networkid 10 \
    --raft \
    --raftport 5040{0} \
    --rpc \
    --rpcaddr "0.0.0.0" \
    --rpcport 2200{1} \
    --rpcapi "admin,eth,debug,miner,net,txpool,personal,web3" \
    --port 2100{1} \
    --nodiscover \
    --tls \
    --tls.cacert "/tls/root_cert.pem" \
    --tls.cert "/tls/cert.pem" \
    --tls.key "/tls/private_key.pem"'''
