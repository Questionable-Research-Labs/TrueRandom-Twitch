import os
from twitchio import *
from twitchio.ext import commands
import requests
import json

from dotenv import load_dotenv


load_dotenv()

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=os.environ['TWITCH_ACCESS_TOKEN'],  prefix='!',
                         initial_channels=['TrueRandomQRL'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | tes')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='roll')
    async def roll_command(self, ctx):
        await ctx.send(f'Hang on a second... Rolling!')
        num = get_dice_roll()
        if num is not False:
            print(num)
            await ctx.send(f'Rolled a {num}!')
        else:
            await ctx.send(f'Dice roll failed...')
    
    @commands.command(name='alive')
    async def alive_command(self, ctx):
        await ctx.send(f'I am at least partially alive!')
    
    @commands.command(name='help')
    async def alive_command(self, ctx):
        await ctx.send(f'Use !roll to roll a random number, and !alive to check the twitch bot is alive.')

def initialize_twitch():
    global bot
    bot = Bot()
    bot.run()

def get_dice_roll():
    response = requests.get("https://tr.host.qrl.nz/api/twitch/random")
    print("got number",response)
    try:
        return int(json.loads(response.text)["response"])
    except:
        return False
if __name__=="__main__":

    initialize_twitch()