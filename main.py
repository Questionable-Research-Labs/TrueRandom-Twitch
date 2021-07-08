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
        num = get_dice_roll()
        print(num)
        await ctx.send(f'Rolled a {num}!')


def initialize_twitch():
    global bot
    bot = Bot()
    bot.run()

def get_dice_roll():
    response = requests.get("https://tr.host.qrl.nz/api/twitch/random")
    print("got number",response)
    number = int(json.loads(response.text)["response"])
    return number
if __name__=="__main__":

    initialize_twitch()