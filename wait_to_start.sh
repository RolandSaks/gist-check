#!/bin/bash

echo $WAIT_COMMAND
echo $WAIT_START_CMD

is_ready() {
    eval "$WAIT_COMMAND"
}

timeout 300 bash -c "until curl --silent --output /dev/null http://elasticsearch:9200/_cat/health?h=st; do printf '.'; sleep 5; done; printf '\n'"

#start the script
exec $WAIT_START_CMD
