#!/bin/bash
: ${IOTA_IP:?Not found}
: ${ORION_URL:?Not found}
: ${IOTA_KEY:=8f9z57ahxmtzx21oczr5vaabot}
curl -iX POST \
  "http://$IOTA_IP:4041/iot/services" \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d "{
 \"services\": [
   {
     \"apikey\":      \"$IOTA_KEY\",
     \"cbroker\":     \"$ORION_URL\",
     \"entity_type\": \"Thing\",
     \"resource\":    \"\"
   }
 ]
}"
