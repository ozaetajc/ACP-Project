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

while player_hp > 0 and enemy_hp > 0
    print (f"\n{turn}'s turn")
    if turn != 'Enemy':
        action = int(input(f"{name}, What will you do:\n1) Normal Attack\n2) Burst Attack\n3) Regen\n"))
    if action == 1:
        player_normal_attack = player.normal_atk()
        enemy_hp = enemy_hp - player_normal_attack
        player_stamina += 10
        time.sleep(2)
        print (f"\n{name} just did {player_normal_attack} damage!")
        print (f"{name} now has {player_hp} hp and {player_stamina} stamina")
        time.sleep(2)
        print (f"The enemy now has {enemy_hp} hp and {enemy_stamina} stamina")
        turn = 'Enemy'

    
