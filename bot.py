import os, discord, csv, datetime
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

def read_csv_file(csv_file_path):
    with open(csv_file_path, 'r') as file:
      lines = file.readlines()
      last_line = lines[-1].strip()
      lit=list(last_line)
      lit = lit[-15:-10]
      time_format = datetime.now().strftime('%H:%M')
      if isinstance(time_format, str):
        last_line = last_line.replace(',', '\n')
        return last_line[:-15]
      else:
        raise Exception()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot_token = os.getenv('BOT_TOKEN')

@client.event
async def on_ready():
  print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):      
    if message.content == '!livescore':
      with open("scraper.py") as f:
        try:
            exec(f.read())
            await message.channel.send('Fetching the live scores...')
            all_rows = read_csv_file('liveScores.csv')
            await message.channel.send(all_rows)
        except Exception as e:
          print(e)
          await message.channel.send("No live scores available!")

    elif message.content == '!help':
        await message.channel.send('Commands: \n !csv - get the csv file the livescores are stored in \n !livescore - get the live scores')

    elif message.content == '!csv':
        file = discord.File('liveScores.csv')
        await message.channel.send(file=file)

client.run(bot_token)