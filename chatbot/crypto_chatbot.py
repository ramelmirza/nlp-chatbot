"""
This script provides the actual implementation of the chatbot on discord

Ramel Mirza, 000778681, Sunday, January 26, 2025

Original reference was from Sam Scott, Mohawk College, 2021
"""

import file_input as fi


# I did not include the load_FAQ_data function because that's what the file_input import does

def understand(utterance):
    """
    Utterance is what the user said and this finds the intent to match it
    :param utterance: User message
    :return: Index of the intent, or -1 to signify not found
    """

    global intents

    try:
        # This for loops checks if there are extra quotation marks, if there is, remove them and the original question mark from the len of the utterance
        extra = 0
        for i in range(0, len(utterance)):
            if utterance[i] == '?':
                extra += 1
        utterance = utterance[:(len(utterance) - extra)]
        utterance = utterance.strip()
        return intents.index(utterance)
    except ValueError:
        return -1


def generate(intent):
    """
    This function returns a response based on users' intent
    :param intent: What the user is trying to do
    :return: A string that says that the chatbot doesn't know what the answer is or the response of the bot
    """

    global responses

    if intent == -1:
        return "I don't know enough to respond to that, sorry."

    return responses[intent]


# Looks weird but [0] is questions, [1] are the responses as file_input returns a 2D list
intents = fi.file_input("qna.txt")[0]
intents = [i.lower().strip('?') for i in intents]  # all lower case and removing the question mark
responses = fi.file_input("qna.txt")[1]


def main():
    """
    Conversation with the bot in the shell
    :return: None
    """

    # Dialog between the user and the chatbot
    print("Konichiwa. I know a decent amount of Crypto - when you get sick of me, say 'goodbye'.")
    print()
    utterance = ""

    while True:
        utterance = input(">>> ")
        utterance = utterance.strip()
        utterance = utterance.lower()

        if utterance in ["hello", "good morning", "hi", "hey", "hiya", "what up"]:
            print("Hello there!")
        elif utterance in ["goodbye", "bye", "ciao", "see you later"]:
            print("Bye for now.")
            break
        else:
            intent = understand(utterance)
            response = generate(intent)
            print(response)
            print()


if __name__ == "__main__":
    main()
