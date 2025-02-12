# Description
This project was built using Python, regular expressions, and the SpaCy library.
It's a fully functioning chatbot designed to be used in a Discord server, but it
works in the Python Shell as well. The surrounding theme is Bitcoin, and it's history - the data was acquired from the trading-bot repo where it sends HTTP GET requests to CoinMarketCaps API.

# Features
The fundamentals of a chatbot consist of 4 parts:

1. __Utterance__
2. __Intent__
3. __Entity__
4. __Response__

- The __utterance__ is what the user has typed(in the case of voice chat, it would be speech recognition)
  - i.e. "Hello, how are you doing?"
- The __intent__ is what the user is trying to do, or get at
  - So in this example, the goal is to greet the bot
- The __entity__ could be thought of as a noun, but it's better put as "a living thing/object from the real world"
  - In "Hello, how are you doing" it would be "you" as the entity. In the case of the SpaCy pipeline, this is classified as a Named Entity Recognition (NER) where "you" would get labelled as "PERSON"
- Lastly, __response__ is the text that the bot sends back (think Alexa or Siri for voice chat)

Combining the 4 key components of a chatbot, these all get categorized under the NLP pipeline where you have Natural Language Understanding, Dialog Management, and Natural Language Generation. This bot encompasses all those key aspects of the NLP pipeline to give a Discord user the ability to communicate with a chatbot for Cryptocurrency related purposes.
