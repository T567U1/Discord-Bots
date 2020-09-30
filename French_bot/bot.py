#if bot has connection problems E.i connection with giving token,
#unistall and install discord.py
import os, discord
from dotenv import load_dotenv
from googletrans import Translator

#conver local .env variables into os.envi()
load_dotenv(verbose=True)
trans = Translator()
TOKEN = os.getenv('BOT_TOKEN')
client = discord.Client()

def happy_birthday():
    str = 'Bon anniversaire, nos vœux les plus sincères Que ces quelques fleurs vous apportent le bonheur Que l\'année entière vous soit douce et légère Et que l\'an fini, nous soyons tous réunis Pour chanter en chœur : \"Bon Anniversaire !\"'
    return str

@client.event
async def on_ready():
    print(f'{ client.user } has connected to discord')

@client.event
async def on_message(msg):
    try:
        print(msg.author)
        command = ' '.join(msg.content.split()[:2])
        msg_ = ' '.join(msg.content.split()[2:])
        print(command, msg_)
        if msg.author == client.user:
            return
        if msg.content == 'getusers':
            await print(type(client.users))

        if '!bot translate' ==  command:
            await msg.channel.send(trans.translate(msg_, dest='fr').text)
            
        if '!bot powerdown' == command:
            await msg.channel.send(trans.translate('Good bye!!', dest='fr').text)
            await client.logout()

    except:
        if msg.author != client.user:
            await msg.channel.send(trans.translate('No', dest='fr').text)

client.run(TOKEN)
