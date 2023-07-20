import os, discord, csv

def read_csv_file(csv_file_path):
        all_rows = []
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                all_rows.append(row)

        return all_rows

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
            await message.channel.send('Fetching the live scores...')
            all_rows = read_csv_file('liveScores.csv')
            await message.channel.send(f"{all_rows[0]} \n {all_rows[1]} \n {all_rows[2]}")

client.run(bot_token)
