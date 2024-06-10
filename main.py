import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

# Load environment variables, get token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up bot
intents = Intents.default() #:create variable that store permission-like config
intents.message_content = True #:permit reading message content
client = Client(intents=intents) #:create discord user with these intents

# Read message
async def send_message(message, user_message):
    if (not user_message and user_message[0] != ">"):
        return
    try:
        command = user_message[1:]
        print(command)
    except Exception as err:
        print(err)

# Bot startup
@client.event
async def on_ready():
    print(f"[!] {client.user} is online")

# Handle incoming messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f"{channel}|{username}:{user_message}")
    await send_message(Message, user_message)

def main():
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()
