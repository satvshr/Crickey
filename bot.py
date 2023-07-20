import discord, csv

def read_csv_file(csv_file_path):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            return row

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot_token = 'MTEzMTIxMzc4NDcwMzMwMzc2MA.Goomqr.Z4GvdibqL9aTfQgM_f54FAPDjnxWlyGF7EVSZc'

is_On = False

@client.event
async def on_ready():
    with open("scraper.py") as f:
        exec(f.read())
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
            await message.channel.send('Fetching the live scores...')
            all_rows = read_csv_file('liveScores.csv')
            if all_rows == None:
                await message.channel.send('No live scores available!')
            else:
                await message.channel.send(f"{all_rows[0]} \n {all_rows[1]} \n {all_rows[2]}")
        else:
            await message.channel.send('Please start the bot first!')

    elif message.content == '!help':
        await message.channel.send('Commands: \n !start - start the bot \n !stop - stop the bot \n !livescore - get the live scores')
client.run(bot_token)
