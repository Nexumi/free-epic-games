# free-epic-games
> A simple Python script that checks the Epic Games Store API for current free games and automatically posts them to a Discord channel via a webhook.

## Setup Guide
### How to Generate a Discord Webhook
To send notifications to your Discord server, you will need a webhook URL.

> [!NOTE]
> You must have the "Manage Webhooks" permission on your Discord server (server administrators have this by default). 

1. Open Discord and navigate to the server where you want the alerts to appear.
2. Click the gear icon next to the text channel where you want the messages sent (or go to Server Settings > Integrations).
3. Go to the Integrations tab and click Create Webhook.
4. Give your webhook a name (and optionally a profile picture).
5. Click Copy Webhook URL.

### Configuring the Script
1. Open the script file (main.py) in any text editor (like Notepad, VS Code, etc.).
2. Locate the discord(url) function near the top.
3. Replace the placeholder text with your copied webhook URL.
  - Example:
```python
def discord(url):
  webhooks = [
    "https://discord.com/api/webhooks/123456789/abcdef...",
  ]
```

### Configuring the Script (Debug)
1. Open the script file (main.py) in any text editor (like Notepad, VS Code, etc.).
2. Locate the report(type, url) function near the top.
3. Replace the placeholder text with your copied webhook URL.
  - Example:
```python
def report(type, url):
  webhooks = [
    "https://discord.com/api/webhooks/123456789/abcdef...",
  ]
```
This will allow you to receive alerts on Discord for when the script fails in any way.

### Running the Script (Manually)
To run the script manually, open your terminal or command prompt in the script's folder and run:
```bash
python3 main.py
```
The script will track last detected games using a generated last_sent.log file so it doesn't spam the same games when they haven't switched out yet. This will make more sense later.

### Running the Script (Automatically)
There are many ways to automatically run a python script. Any of the methods work. Here is a recommended way of running the script.

24/7 Linux Server
```bash
sudo crontab -e
```
```bash
0 0 * * * python3 /path/to/free-epic-games/main.py
```
Remember to update the path to the actual path to the script.

It is recommended to configure the cronjob to run daily 1 hour after when the games refresh. This is to allow for the API time to update with the new free games.

Normally games cycle out once a week but running it daily accounts for the special occasions like Chrstimas, where games are refreshed daily.

> [!TIP]
> You can get a free vps with Oracle's Free Tier
