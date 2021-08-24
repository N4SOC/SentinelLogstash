#!/usr/bin/env bash
#Change below path to match customer environment
cd /home/logcollect/SentinelLogstash
/usr/bin/git pull
# Change profiles below to match customer environment
/usr/local/bin/docker-compose --profile vmware --profile netscaler up --force-recreate -d
















