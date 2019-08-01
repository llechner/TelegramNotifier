#!/bin/bash

python telegram_notifier.py "Runner.sh: Start executing $1 from ${PWD} on $(hostname -s)"

eval $1

python telegram_notifier.py "Runner.sh: Done executing $1 from ${PWD} on $(hostname -s)"
