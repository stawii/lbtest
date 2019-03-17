# lbtest

docker network create --driver overlay lbtest
docker service create --name lb1 --network lbtest -p 8000:80 lb:latest
docker service create --name test1 --network lbtest --replicas 5 --endpoint-mode dnsrr test:latest
docker service create --name dns --network lbtest -p 5353:53/udp alpine/socat udp-listen:53,fork UDP:127.0.0.11:53
