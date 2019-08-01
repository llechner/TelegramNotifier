#!/bin/bash

echo "Starting nohup with notifier..."
CMD=${@}
echo "Executing command '${CMD}'"

nohup krenew -t -K 10 -- bash -c "notifier.py '${CMD}'" &
