# run.sh
task () {
docker -v
}
export -f task
parallel --sshloginfile servers --onall   --env task {} :::  task
# servers
server1
server2