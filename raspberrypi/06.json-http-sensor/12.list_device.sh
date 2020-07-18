#!/bin/bash
: ${IOTA_IP:?Not found}
curl -s "http://$IOTA_IP:4041/iot/devices" -H 'fiware-service: openiot' \
-H 'fiware-servicepath: /' | jq .
