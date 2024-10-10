import random
from termcolor import cprint

POSSIBLE_ANSWERS = ['a', 'b', 'c', 'd']

QUESTION = 'question'
ANSWER = 'answer'
OPTIONS = 'options'


def get_answer():
    while True:
        answer = input('Your answer: ').lower()
        if answer in POSSIBLE_ANSWERS:
            return answer


def check_answer(answer, question):
    return True if answer == question.get(ANSWER) else False


def display_message(is_answer_correct, correct_answer):
    if is_answer_correct:
        cprint('Correct!', 'light_green')
    else:
        cprint(f'Wrong! The correct answer is {correct_answer}', 'light_red')


def ask_question(i, question):
    print('Question {}: {}'.format(i+1, question.get(QUESTION)))
    for option in question.get('options'):
        print(option)


def run(quizz):
    score = 0
    random.shuffle(quizz)
    for i, question in enumerate(quizz):
        ask_question(i, question)
        answer = get_answer()
        is_answer_correct = check_answer(answer, question)
        display_message(is_answer_correct, question.get(ANSWER))
        if is_answer_correct:
            score += 1

    print(f'Quizz over!  your final score is {score} out of {len(quizz)}')


if __name__ == '__main__':
    quizz = [
        {
            QUESTION: "Qui a remporté la Coupe du Monde de la FIFA en 2018 ?",
            OPTIONS: ["a) Allemagne", "b) Brésil", "c) France", "d) Espagne"],
            ANSWER: "c"
        },
        {
            QUESTION: "Quel joueur a remporté le plus de Ballons d'Or ?",
            OPTIONS: ["a) Cristiano Ronaldo", "b) Lionel Messi", "c) Zinedine Zidane", "d) Johan Cruyff"],
            ANSWER: "b"
        },
        {
            QUESTION: "Quel club a remporté le plus de titres de la Ligue des Champions de l'UEFA ?",
            OPTIONS: ["a) FC Barcelone", "b) Bayern Munich", "c) AC Milan", "d) Real Madrid"],
            ANSWER: "d"
        },
        {
            QUESTION: "En quelle année la première Coupe du Monde de la FIFA a-t-elle été organisée ?",
            OPTIONS: ["a) 1930", "b) 1940", "c) 1950", "d) 1960"],
            ANSWER: "a"
        },
        {
            QUESTION: "Quel joueur est surnommé 'El Fenomeno' ?",
            OPTIONS: ["a) Ronaldinho", "b) Ronaldo Nazário", "c) Romário", "d) Rivaldo"],
            ANSWER: "b"
        },
        {
            QUESTION: "Quel pays a remporté le plus de Coupes du Monde de la FIFA ?",
            OPTIONS: ["a) Allemagne", "b) Argentine", "c) Italie", "d) Brésil"],
            ANSWER: "d"
        },
        {
            QUESTION: "Qui est le meilleur buteur de tous les temps en Coupe du Monde de la FIFA ?",
            OPTIONS: ["a) Miroslav Klose", "b) Pelé", "c) Cristiano Ronaldo", "d) Diego Maradona"],
            ANSWER: "a"
        },
        {
            QUESTION: "Quel club est surnommé 'Les Reds' ?",
            OPTIONS: ["a) Arsenal", "b) Manchester United", "c) Liverpool", "d) Bayern Munich"],
            ANSWER: "c"
        },
        {
            QUESTION: "Qui est le joueur le plus cher de l'histoire du football (transfert) ?",
            OPTIONS: ["a) Neymar", "b) Kylian Mbappé", "c) Cristiano Ronaldo", "d) Lionel Messi"],
            ANSWER: "a"
        },
        {
            QUESTION: "Quelle équipe nationale est surnommée 'La Roja' ?",
            OPTIONS: ["a) Portugal", "b) Espagne", "c) Chili", "d) Italie"],
            ANSWER: "b"
        }
    ]
    run(quizz)
