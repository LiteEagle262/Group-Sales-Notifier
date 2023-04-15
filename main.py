import requests
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed

cookie = 'cookiehere' # for the cookie, I recommend having a bot account as the cookie as it's easier, to refresh the cookie to be used by any IP use this: https://rblxcopy.net/cookierefresh.php
webhook_url = 'webhookhere'
group_id = '696969' #your group id
headers = {'Cookie':f'.ROBLOSECURITY={cookie}'}
webhook = DiscordWebhook(url=webhook_url, content='<@785585779429867561>') # example of how to ping someone, it's <@> and in the middle is your user ID on discord

def get_data():
    try:
        r = requests.get(f"https://economy.roblox.com/v2/groups/{group_id}/transactions?cursor=&limit=100&sortOrder=Asc&transactionType=Sale",headers=headers)
        r.raise_for_status()
        jso = r.json()
        return jso.get("data", [])[0]
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def send_webhook(data):
    user_id = data['agent'].get('id')
    username = data['agent'].get('name')
    product_name = data['details'].get('name')
    product_price = data['currency'].get('amount')
    desc = f"""
    ```fix
    User ID: {user_id}
    Username: {username}
    Product Name: {product_name}
    Product Price: {product_price} Robux
    ```
    """
    embed = DiscordEmbed(title='New Sale!!', description=desc, color='FFFF00')
    embed.set_thumbnail(url=f"https://www.roblox.com/headshot-thumbnail/image?userId={user_id}&width=420&height=420&format=png")
    embed.set_timestamp()
    embed.set_footer(text='Made by https://liteeagle.me/')
    webhook.add_embed(embed)
    response = webhook.execute()

def start():
    print("Running")
    while True:
        try:
            prev_data = get_data()
            print(prev_data)
            sleep(1)
            new_data = get_data()
            if new_data != prev_data:
                send_webhook(new_data)
        except:
            print("An error has occurred, restarting")
            continue

start()
