#!/usr/bin/env python

import os, sys, time

from TelegramNotifier.Tools.telegramNotifier import send

# Defaults
user         = os.getenv("USER")
cwd          = os.getcwd()
hostname     = os.getenv("HOSTNAME")
submit_time  = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
cmd          = " ".join( sys.argv[1:] )

send( "%s TelegramNotifier: Start executing '%s' for user %s from %s on %s"%(submit_time, cmd, user, cwd, hostname) )
exitcode = os.system( cmd )
send( "%s TelegramNotifier: Done executing '%s' for user %s from %s on %s (exit code: %s)"%(submit_time, cmd, user, cwd, hostname, exitcode) )
