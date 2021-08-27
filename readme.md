## Azure Sentinel config
Copy example.env to .env and replace variables for required modules

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
``` copy docker_refresh.sh /etc/cron.daily/ ```