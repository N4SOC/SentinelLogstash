## To build all images:
``` docker compse build ```

## To run specific images:
``` docker compse --profile eset --profile trend run ```

## To build individual images:
``` docker build --build-arg workspaceID=123456abc --build-arg workspaceKey=abcdef123 --tag sentinel_eset .```

## To run image (with network input)
``` docker run -d -it --rm -p 2514:514 --name "Sentinel_ESET" sentinel_eset ```

## To run image (with file input)
``` docker run -d -it --rm --mount type=bind,source=/opt/zeek/logs/current,target=/logs --name "Sentinel_Zeek" sentinel_zeek ```

