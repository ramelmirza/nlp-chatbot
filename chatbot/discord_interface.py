"""
Puts the FAQ bot skeleton code (I renamed it to cryptocb_skeleton)online as a discord bot

Ramel Mirza, 000778681, Sunday, January 26, 2025

Original reference was from Sam Scott, Mohawk College, 2021
"""

import discord
from crypto_chatbot import *


class MyClient(discord.Client):
    """
    Class that represents the bot user
    """

    def __init__(self):
        """
        Sets default intents for the bot
        :return: Constructs an object
        """
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

    async def killProgram(self):
        """
        Made this helper function so that when the user types goodbye the program ends/chatbot logs off Discord
        :return: None
        """
        await self.close()

    async def on_ready(self):
        """
        Gets called when the bot is logged in
        :return: None
        """
        print('Logged on as', self.user)

    async def on_message(self, message):
        """
        Gets called when the bot receives a message from a bot user. The message object contains all information
        :param message: The message from the user
        :return: None
        """

        # Makes sure that the bot does not respond to itself
        if message.author == self.user:
            return

        # Gets the utterance then generates response
        utterance = message.content

        # This for loops checks if there are extra quotation marks, if there is, remove them and the original question mark from the len of the utterance
        extra = 0
        for i in range(0, len(utterance)):
            if utterance[i] == '?':
                extra += 1
        utterance = utterance[:(len(utterance) - extra)]
        utterance = utterance.strip()
        utterance = utterance.lower()

        if utterance in ["hello", "good morning", "hi", "hey", "hiya", "what up"]:
            await message.channel.send("Hello there!")
        elif utterance in ["goodbye", "bye", "ciao", "see you later"]:
            await message.channel.send("Bye for now.")
            await self.killProgram()
        else:
            intent = understand(utterance)
            response = generate(intent)
            await message.channel.send(response)


# Logs in
client = MyClient()
with open("token.txt") as file:
    token = file.read()
client.run(token)
