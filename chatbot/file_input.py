"""
Processes the reading of each line in a given file (qna.txt in my case)

Ramel Mirza, 000778681, Sunday, January 26, 2025

Original reference was from Sam Scott, Mohawk College, 2021
"""


def file_input(filename):
    """
    I modified this function slightly because I put all questions and answers in 1 text file where the lines alternate between questions and answers
    :param filename: The name of the file
    :return: 2D list containing 2 lists - 1 holds the questions, the other holds the answers
    """
    questions = []
    answers = []
    with open(filename) as file:
        qna = file.readlines()  # reads the entire file into 1 big list

        # Because line 1 of the file is a question, the file follows a "q a q a q a q a" format
        questions = qna[0:len(qna):2]  # Even numbers are questions
        answers = qna[1:len(qna):2]  # Odd numbers are answers, hence the start from 1

        # Have to strip the \n and only need 1 for loop because they are parallel/same length
        for i in range(0, len(questions)):
            questions[i] = questions[i].strip()
            answers[i] = answers[i].strip()

    return questions, answers


# print(file_input("qna.txt")[0])
# print(file_input("qna.txt")[1])