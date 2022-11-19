
import random
import json
import datetime

current_time = datetime.datetime.now()
print(current_time)

secret = random.randint(1, 30)
attempts = 0
wrong = attempts

with open("score_list.json",  "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

with open("guess_list.json", "r") as guess_file:
    guess_list = json.loads(guess_file.read())
    print("Wrong_guesses: " + str(guess_list))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:

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

    wrong += 1
    if guess != secret:

        guess_list.append(wrong)

        with open("guess_list.json", "w") as guess_file:
            guess_file.write(json.dumps(guess_list))

        print("Wrong_guesses: " + str(wrong))



