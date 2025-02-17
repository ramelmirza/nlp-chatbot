"""
Implements the python shell version of the crypto chatbot
Ramel Mirza, Date Started: February 10, 2025
"""

import regex as re
import coinmarketcapAPI.cmc_request as cmc
import time
import spacy
from spacy.matcher import Matcher


def read_files(filename1, filename2):
    """
    Reads the contents of 2 files (Answers, Regexes)
    :param filename1: File name 1
    :param filename2: File name 2
    :return: 2D tuple containing 2 lists; answers and regexes
    """
    with open(filename1) as file1, open(filename2) as file2:
        answers = file1.readlines()
        regexes = file2.readlines()

        for i in range(0, len(answers)):
            answers[i] = answers[i].strip()

        for i in range(0, len(regexes)):
            regexes[i] = regexes[i].strip()

        return answers, regexes


def spacy_part(utterance):
    """
    Handles utterance when match object is not found (out of scope for the chatbot)
    :param utterance: Users input
    :return: Formatted string containing information about the users utterance - potentially redirecting them to a website containing the info they desire
    """
    nlp = spacy.load("en_core_web_lg")
    matcher = Matcher(nlp.vocab)

    pattern = [
        {"POS": "PRON"},
        {"POS": {"IN": ["VERB", "NOUN"]}},
        {"POS": "ADP"},
        {"POS": {"IN": ["PROPN", "NOUN"]}, "OP": "+"}
    ]

    matcher.add("non-crypto", [pattern])
    doc = nlp(utterance)
    matches = matcher(doc)

    response_out_of_vocabulary = ''
    for match_id, start, end in matches:
        response_out_of_vocabulary = doc[start:end].text

    named_entity = doc.ents
    return f"Sorry. That's not specific enough for me.\nYou\'re asking me things like \"{response_out_of_vocabulary}\". \nHowever, if you want some information on {named_entity[0]}, here's a link!\n https://www.google.com/search?q={named_entity[0]}"


def api_part(match_parallel):
    """
    Manages the response when user is asking for the current market price of BTC
    :param match_parallel: First response in the text file "answers"
    :return:
    """
    responses = []
    if match_parallel == 0:
        btc_data = cmc.json_to_csv()
        if btc_data is not None:
            api_price = btc_data.get("price")
            responses.append(f'Using CoinMarketCaps API, the current market price of BTC is: ${api_price} [USD]')
            responses.append('Here is also some more data regarding BTC:')
            responses.append(f'24H % Change is: {btc_data.get("percent_change_24h")}%\n'
                             f'24H Total Volume is: ${btc_data.get("volume_24h"):,.0f}... That is a lot of Bitcoin!\n'
                             f'Also, I saved a CSV file so you can see more data if you are interested.')
    responses.append('btc.csv')

    return responses


def dialog(utterance, ans, exps):
    """
    Redirects the utterance from the user based on their intent... Pathways built to manage what the user wants (name of PDF, image of pizza day guy, etc.)
    :param utterance: Users input
    :param ans: Answers list
    :param exps: Regex list
    :return: String, Tuple, List, 2D List - based on users input
    """
    matches = []
    index_of_regex_matches = []
    for i in range(0, len(exps)):
        match_object = re.search(r"" + exps[i] + "", utterance, flags=re.BESTMATCH | re.IGNORECASE)
        if match_object is not None:
            matches.append(match_object)
            index_of_regex_matches.append(i)

    heuristic = 0
    match_parallel = -1
    if len(matches) == 0:
        return spacy_part(utterance)
    elif len(matches) == 1 and 0 not in index_of_regex_matches:
        if index_of_regex_matches[0] == 15:
            t = (ans[index_of_regex_matches[0]],
                 'Because you asked, I\'m also going to give you the link to the pdf:\n https://bitcoin.org/bitcoin.pdf')
            return t
        elif index_of_regex_matches[0] == 8:
            l = [ans[index_of_regex_matches[0]],
                 'https://techresearcho.com/wp-content/uploads/2023/05/Laszlo-Hanyecz-bitcoin-pizza-day.jpg']
            return l
        else:
            return ans[index_of_regex_matches[0]]
    else:
        for m in range(0, len(matches)):
            """
            Implementing a heuristic score to find the best match if multiple match objects are found
            """
            errors_in_match = sum(matches[m].fuzzy_counts) * 2
            length = len(matches[m].group())
            compare_score = length - errors_in_match
            if compare_score > heuristic:
                heuristic = compare_score
                match_parallel = m # Index gets set to the match object with the highest heuristic score

        if match_parallel == 0:
            return api_part(match_parallel)
        else:
            return ans[index_of_regex_matches[match_parallel]]


def main():
    """
    The dialog between the bot and user
    :return: None
    """
    print("Hello. I know a decent amount of Crypto - when you get sick of me, say 'goodbye'.")
    print()

    both = read_files("answers", "regex")
    ans = both[0]
    exps = both[1]

    while True:
        utterance = input(">>> ")
        utterance = utterance.strip().lower()

        if utterance in ["hello", "good morning", "hi", "hey", "hiya", "what up", "what's up"]:
            print("Hello there")
        elif utterance in ["goodbye", "bye", "ciao", "see you later"]:
            print("Bye for now")
            break
        else:
            response = dialog(utterance, ans, exps)

            if type(response) == tuple:  # PDF Part
                print(response[0])
                time.sleep(2)
                print(response[1])
            elif type(response) == list and len(response) == 2:  # Bitcoin Pizzaday Part
                print(response[0])
                # No image here, saving that part for discord
            elif type(response) == list and len(response) == 4:  # API Part
                for i in range(0, len(response) - 1):
                    print(response[i])
                    time.sleep(2)
                    # Again, saving the CSV file to be uploaded in the discord
            else:
                print(response)
                print()


if __name__ == "__main__":
    main()
