import os, discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot_token = os.environ['BOT_TOKEN']

is_On = False

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    global is_On
    if message.content == '!start':
        is_On = True
        await message.channel.send('Hello, I am your friendly bot!')
        
    elif message.content == '!stop':
        is_On = False
        await message.channel.send('Goodbye! Hope I was helpful to you!')

    elif message.content == '!livescore':
        if is_On:
            await message.channel.send('I am currently on!')

client.run(bot_token)
