/opt/zeek/bin/zeekctl deploy
echo "Deployed"
/opt/zeek/bin/zeekctl start
echo "Started"
tail -f /dev/null # nasty hack to prevent caontiner exiting after entrypoint script finishes