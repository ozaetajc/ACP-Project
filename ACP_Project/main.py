import random
import time

class Player():
    def normal_atk(self):
        attack = random.randint(1, 15)
        return attack

    def burst_atk(self):
        burst_atk = random.randint(20, 35)
        return burst_atk

    def heal(self):
        regeneration = random.randint(5, 20)
        return regeneration



player = Player()
player_hp = 100
player_stamina = 0

enemy = Player()
enemy_hp = 100
enemy_stamina = 0

ready = input ("Press ENTER to Continue")
name = input ("Enter your Name: ")


def first_turn():
    fturn = random.randint(0,2)
    if fturn == 0:
        return 'Enemy'
    else:
        return name
turn = first_turn()
