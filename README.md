# TelegramNotifier
Details here:
https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay

## Short Setup
Create your own user settings in

```
TelegramNotifier/Tools/python/user.py
```

#### Get Bot Token:
Visit telegram.me/botfather and type

```
\newbot 
<your-bot-username> 
```

Copy the Token you get to

```
TelegramNotifier/Tools/python/user.py
```

#### Get User ID:
Visit https://api.telegram.org/botTOKEN/getUpdates and copy your UserID to

```
TelegramNotifier/Tools/python/user.py
```

#### Install settings
Install requests:

```
pip install requests --user 
```
scram

```
scram b -j 8
```

## Run Notifier

local without nohup:

```
notifier.py COMMAND
```

local with nohup:

```
runNotifier.sh COMMAND
```
