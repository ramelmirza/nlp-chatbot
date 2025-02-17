"""
Implements the discord version of the crypto chatbot
Ramel Mirza, Date Started: February 10, 2025
"""

import discord
from crypto_chatbot import *


class MyClient(discord.Client):
    """
    Discord bot
    """

    def __init__(self):
        """
        Setting default intents
        """
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

    async def kill(self):
        """
        Ends the program when one of the "bye" lemmas are uttered
        :return:
        """
        await self.close()

    async def on_ready(self):
        """
        Message when logged on
        :return: None
        """
        print('Logged on as', self.user)

    async def on_message(self, message):
        """
        The dialog between the bot and user
        :param message: The message the user uttered
        :return: None
        """

        both = read_files("answers", "regex")
        ans = both[0]
        exps = both[1]

        if message.author == self.user:
            return

        utterance = message.content

        if utterance in ["hello", "good morning", "hi", "hey", "hiya", "what up", "what's up"]:
            await message.channel.send("Hello there")
        elif utterance in ["goodbye", "bye", "ciao", "see you later"]:
            await message.channel.send("Bye for now")
            await self.kill()
        else:
            response = dialog(utterance, ans, exps)

            if type(response) == tuple:  # PDF Part
                await message.channel.send(response[0])
                time.sleep(2)
                await message.channel.send(response[1])
            elif type(response) == list and len(response) == 2:  # Bitcoin Pizza Day Part
                await message.channel.send(response[1])
                await message.channel.send(response[0])
            elif type(response) == list and len(response) == 4:  # API Part
                csv_file = response[3]
                for i in range(0, len(response) - 1):
                    await message.channel.send(response[i])
                    time.sleep(2)
                await message.channel.send(file=discord.File(csv_file))
                # I used https://stackoverflow.com/questions/50860397/discord-py-bot-sending-file-to-discord-channel as a reference for the 1 line above
            else:
                await message.channel.send(response)


# Logs the bot on
client = MyClient()
with open("token.txt") as file:
    token = file.read()
client.run(token)
