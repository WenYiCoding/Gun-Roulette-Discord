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
    if (not user_message or user_message[0] != ">"):
        return
    else:
        try:
            command = user_message[1:]
            
        except Exception as err:
            print(f'[!] ERR:{err}')

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
    content = message.content
    channel = str(message.channel)

    print(f"{channel}\t{username}:{content}")
    await send_message(Message, content)

# Main function
def main():
    client.run(token=TOKEN)

# Execute
if __name__ == "__main__":
    main()
