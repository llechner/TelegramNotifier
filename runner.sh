#!/bin/bash
echo "Starting nohup with notifier..."
nohup krenew -t -K 10 -- bash -c "notifier.sh \"$1\"" &
