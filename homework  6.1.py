# Objektno orijentirano programiranje u Pythonu

import dataclasses


class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

        def weight_to_lbs(self):
            pounds = self.weight_kg * 2.20462262
            return pounds


# Nasljeđuje klasu Player
class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals_numbers = goals
        self.yellow_cards = y_cards
        self.red_cards = r_cards
        self.assists = assists


print("Enter some football player's data!")

f_name = input("Enter player's first name: ")
l_name = input("Enter player's last name: ")
height = input("Enter player's height: ")
weight = input("Enter player's weight: ")
goals = input("Enter the number of player's goals: ")
y_cards = input("Enter the number of player's yellow cards: ")
r_cards = input("Enter the number of player's red cards: ")

new_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                            goals_numbers=int(goals), yellow_cards=int(y_cards), red_cards=int(r_cards))

with open("football_players.json", "w") as football_file:
    football_file.write(str(new_player.__dict__))

print("Player successfully entered!")
print("Player's data: {0}".format(new_player.__dict__))
