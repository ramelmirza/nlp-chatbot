# About
This is a chatbot based on a BTC/Cryptocurrency theme. It uses Natural Language Processing to manage the conversations - based off of the SpaCy library/NLP Pipeline.

There are 4 main components in a pipeline:

1. __Utterance__
2. __Intent__
3. __Entity__
4. __Response__

In the case of *Utterance*, this is based on the users message. Given this is chatbot is based off of text only, there is no text-to-speech synthesis but
voice chat is another valid form of an utterance.

*Intent* is what the user is trying to do - a simple "Hello, good morning" means that the user is trying to greet the chatbot.

*Entity* are things that are a real world thing, so in the prior example given with a simple greeting, a real world thing would be "Morning".

*Response* is based off of what the chatbot will respond with. After figuring out the intent and identifying the entities, the chatbot will respond with something that is
based off of the natural language understanding stage. It wouldn't make sense to give a link to Amazon when the user is trying to greet the bot.

All of this is done through what is known as the NLP pipeline.

![image](https://github.com/ramelmirza/nlp-chatbot/image.png)

# Features
Using the discord version of the bot, specific utterances will have the chatbot answer with extras such as links, files(csv), images, and raw data.

An utterance made that is in the form of a question outside the general vocabulary of the chatbot will be met with a link redirecting the user regarding that information.