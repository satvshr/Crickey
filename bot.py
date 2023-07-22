import os, discord, csv
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

def read_csv_file(csv_file_path):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            return row

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot_token = os.getenv('BOT_TOKEN')

@client.event
async def on_ready():
    with open("scraper.py") as f:
        exec(f.read())
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):      
    if message.content == '!livescore':
            await message.channel.send('Fetching the live scores...')
            all_rows = read_csv_file('liveScores.csv')
            if all_rows == None:
                await message.channel.send('No live scores available!')
            else:
                await message.channel.send(f"{all_rows[0]} \n {all_rows[1]} \n {all_rows[2]}")

    elif message.content == '!help':
        await message.channel.send('Commands: \n !csv - get the csv file the livescores are stored in \n !livescore - get the live scores')

    elif message.content == '!csv':
        file = discord.File('liveScores.csv')
        await message.channel.send(file=file)

client.run(bot_token)