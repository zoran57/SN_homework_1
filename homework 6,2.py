
import datetime
import json
import random
current_time = datetime.datetime.now()
print(current_time)


class Rezultat:
    def __init__(self, attempts, player_name,date,top_scores):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date
        self.top_scores = top_scores

with open("Rezultat_list.json", "w") as Rezultat_file:
    Rezultat_file.write(str(Rezultat.__dict__))


def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list
"""
print("Top scores: " + str(score_list))
for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
"""

def play_game_hard():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    player_name = input("Unesite ime igrača: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            osobni_rezultat = Rezultat(attempts=attempts, player_name=player_name,top_scores=get_top_scores, date=str(datetime.datetime.now()))

            score_list.append(attempts)

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))



            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break

def play_game_easy():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    player_name = input("Unesite ime igrača: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            osobni_rezultat = Rezultat(attempts = attempts, player_name = player_name,top_scores=get_top_scores, date =str(datetime.datetime.now()))

            score_list.append(attempts)

            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))


            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


"""
def odabir(new_game_A = "A" ,top_scores_B="B", exit_C="C"):
    A = new_game_A = input("Dali želite započeti novu igru, A): ")
    B = top_scores_B = input("Dali želite vidjeti najbolji rezultat, B): ")
    C = exit_C = input("Dali želite napustiti igru, C): ")
    return odabir
"""
def get_top_scores():
    score_list = get_score_list()
    top_scores_list = sorted(score_list, key=lambda k: k["attempts"])[:5]
    return top_scores_list

def get_attempts_list():
    attempts = get_attempts_list()
    return attempts

while True:
    odabir = input("Dali želite započeti lakšu igru, A):,"
                   "Dali želite započeti težu igru, B):,"
                   " Dali želite vidjeti najbolji rezultat, C):"
                   "  ili Dali želite napustiti igru, D): ")
    if odabir.upper()== "A":
        play_game_easy()
    elif odabir.upper()== "B":
        play_game_hard()
    elif odabir.upper() == "C":
        for score_dict in get_score_list():
            osobni_rezultat = Rezultat(attempts=score_dict.get("attempts"),
                                player_name=score_dict.get("player_name", "Anonymous"),
                                top_scores=score_dict.get("score_list"),
                                date=score_dict.get("date"))

            print("Player: {name}; Attempts: {attempts}; Date: {date}".format(name=osobni_rezultat.player_name,
                                                                              attempts=osobni_rezultat.attempts,
                                                                              date=osobni_rezultat.date))

    elif odabir.upper() == "D":

        print("Kraj igre")

    else:
        break




