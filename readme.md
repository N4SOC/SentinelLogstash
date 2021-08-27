## Azure Sentinel log collectors
Copy **example.env** to **.env** and replace variables for required modules
``` cp example.env .env ```

## To install docker & docker compose:
``` sudo bash docker_install.sh ```

## To build a single profile:
``` docker-compse --profile ids build ```

## To build multiple profiles:
``` docker-compse --profile ids --profile sophos build ```

## To run (Foreground):
``` docker-compse --profile ids up ```

## To run (Background):
``` docker-compse --profile ids up -d ```

## To enable auto-update
Edit **docker_refresh.sh** to refelect correct path and profiles in use
``` cp docker_refresh.sh /etc/cron.daily/ ```

## To enable remote management access
Add ngrok auth key into .env
``` docker-compse --profile mgmt up -d ```

