import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

import GunRouletteDiscord

gameChannel = ""

# Load environment variables, get token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("[!] Token not found, enter token manually")
    TOKEN = input(">")

# Set up bot
intents = Intents.default() #:create variable that store permission-like config
intents.message_content = True #:permit reading message content
client = Client(intents=intents) #:create discord user with these intents

# Send message
async def send_message(message, content):
    if not content or content[0] != ">":
        return
    else:
        try:
            global gameChannel
            messageChannel = message.channel
            messageChannelTitle = str(messageChannel)
            
            command = content[1:].lower()
            print(f"[>] {command}")

            if gameChannel == "":
                if command == "start":
                    gameChannel = messageChannelTitle
                    await messageChannel.send("The game has started in this channel: "+gameChannel)

            elif messageChannelTitle != gameChannel:
                await messageChannel.send("The game is ongoing in this channel: "+gameChannel)
                return
            
            GunRouletteDiscord.program()

        except Exception as err:
            print(f'[!] ERR:{err}')

# Bot startup
@client.event
async def on_ready():
    print(f"[!] {client.user} is online")

# Read messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    content = message.content
    channel = str(message.channel)

    print(f"{channel}\t{username}:{content}")
    await send_message(message, content)

# Main function
def main():
    client.run(token=TOKEN)

# Execute
if __name__ == "__main__":
    main()
