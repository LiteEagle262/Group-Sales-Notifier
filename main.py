import requests
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed

cookie = 'cookiehere' # for the cookie, i recomend having a bot account as the cookie as its easier, to refresh the cookie to be used by any ip use this: https://rblxcopy.net/cookierefresh.php
webhook_url = 'webhookhere'
group_id = '696969' #your group id
headers = {'Cookie':f'.ROBLOSECURITY={cookie}'}
webhook = DiscordWebhook(url=webhook_url, content='<@785585779429867561>') # example of how to ping someone, its <@> and in the middle is your user id on discord

def getdata():
    r = requests.get(f"https://economy.roblox.com/v2/groups/{group_id}/transactions?cursor=&limit=100&sortOrder=Asc&transactionType=Sale",headers=headers)
    jso = r.json()
    return jso["data"][0]

def start():
    print("Running")
    compare()
    return

def getnew():
    r = requests.get(f"https://economy.roblox.com/v2/groups/{group_id}/transactions?cursor=&limit=100&sortOrder=Asc&transactionType=Sale",headers=headers)
    jso = r.json()
    return jso["data"][0]

def compare():
    try:
        predat = getdata()
        print(predat)
        while getnew() == predat:
            sleep(1)
        else:
            r = requests.get(f"https://economy.roblox.com/v2/groups/{GROUP_ID}/transactions?cursor=&limit=100&sortOrder=Asc&transactionType=Sale",headers=headers)
            jso = r.json()
            user_id = jso['data'][0]['agent']['id']
            username = jso['data'][0]['agent']['name']
            product_name = jso['data'][0]['details']['name']
            Product_Price = jso['data'][0]['currency']['amount']
            desc = f"""
    ```fix
    User Id: {user_id}
    Username: {username}
    Product Name: {product_name}
    Product Price: {Product_Price} Robux
    ```
    """
            embed = DiscordEmbed(title='New Sale!!', description=desc, color='FFFF00')
            embed.set_thumbnail(url=f"https://www.roblox.com/headshot-thumbnail/image?userId={user_id}&width=420&height=420&format=png")
            embed.set_timestamp()
            embed.set_footer(text='Made by LiteEagle262#2777')
            webhook.add_embed(embed)
            response = webhook.execute()
            start()
            return
    except:
        print("A error has occurred, restarting")
        start()
        return

start()
