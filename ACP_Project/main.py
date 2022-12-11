import random
import time
import sys
import pygame
from pygame import mixer
pygame.mixer.init()

ATTACK_SOUND = pygame.mixer.Sound ('sound.mp3')
BURST_SOUND = pygame.mixer.Sound ('burst.mp3')
HEAL_SOUND = pygame.mixer.Sound ('heal.wav')

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
    

class Enemy(Player): #Inherits Player class
    def gather(self):
        gather = random.randint(5, 12)
        return gather

player = Player()
player_hp = 100
player_stamina = 0

enemy = Enemy()
enemy_hp = 100
enemy_stamina = 0

ready = input ("Press ENTER to Continue")
mixer.init()
mixer.music.load("bgm.mp3")
mixer.music.play()
name = input ("Enter your Name: ")


def first_turn():
    fturn = random.randint(0,2)
    if fturn == 0:
        return 'Enemy'
    else:
        return name
turn = first_turn()

def slowprint(reaper):
    for symbols in reaper + '\n':
        sys.stdout.write(symbols)
        sys.stdout.flush()
        time.sleep(1/500)
        
print ('')
print ('')
slowprint ('             *********')
slowprint ('           *************')
slowprint ('          *****     *****')
slowprint ('         ***     ✡     ***')
slowprint ('        ***             ***')
slowprint ('        **    0     0    **')
slowprint ('        **               **                  ____')
slowprint ('        ***             ***             //////////')
slowprint ('        ****           ****        ///////////////  ')
slowprint ('        *****         *****    ///////////////////')
slowprint ('        ******       ******/////////         |  |')
slowprint ('      *********     ****//////               |  |')
slowprint ('     ***********   **/////*****              |  |')
slowprint ('  *************** **///***********        ***|  |*')
slowprint (' ******************/****************    *****| <=>*')
slowprint (' ********************************************|<===>* ')


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
        ATTACK_SOUND.play()
        print (f"{name} now has {player_hp} hp and {player_stamina} stamina")
        time.sleep(2)
        print (f"The enemy now has {enemy_hp} hp and {enemy_stamina} stamina")
        turn = 'Enemy'

    elif action == 2 and player_stamina >= 20:
        player_burst_attack = player.burst_atk()
        enemy_hp = enemy_hp - player_burst_attack
        player_stamina -= 20
        time.sleep(2)
        print (f"\n{name} just did {player_burst_attack} damage!")
        BURST_SOUND.play()
        print (f"{name} now has {player_hp} hp and {player_stamina} stamina")
        ime.sleep(2)
        print (f"The enemy now has {enemy_hp} hp and {enemy_stamina} stamina")
        turn = 'Enemy'
        
    elif action == 3 and player_stamina >= 15:
        player_regenerate = player.heal()
        player_hp += player_regenerate
        player_stamina -= 15
        time.sleep(2)
        print (f"\n{name} regenerated {player_regenerate} hp")
        HEAL_SOUND.play()
        print (f"{name} has {player_hp} hp and {player_stamina} stamina")
        turn = 'Enemy'

    elif action == 2 or action == 3 and player_stamina < 15:
        print (f"\n{name} you have {player_hp} hp and {player_stamina} stamina")
        print (f"\n{name} your stamina is too low, recharge by doing Normal Attack ")
    else:
        print ("Enter a correct Action")
        
        
else:
       if enemy_hp < 50 and enemy_stamina >= 15:
            enemy_regenerate = enemy.heal()
            enemy_hp += enemy_regenerate
            enemy_stamina -= 15
            time.sleep(2)
            print (f"\nThe enemy healed for {enemy_regenerate} hp!")
            HEAL_SOUND.play()
            print (f"{name} now has {player_hp} hp and {player_stamina} stamina")
            time.sleep(2)
            print (f"The enemy now has {enemy_hp} hp and {enemy_stamina} stamina")
            turn = name
            
       elif enemy_stamina <= 10:
            gather_stamina = enemy.gather()
            enemy_stamina = enemy_stamina + gather_stamina
            player_hp = player_hp - gather_stamina
            time.sleep(2)
            print (f"\nThe enemy gathered {gather_stamina} stamina in exchange for your hp!")
            HEAL_SOUND.play()
            print (f"{name} now has {player_hp} hp and {player_stamina} stamina")
            time.sleep(2)
            print (f"The enemy now has {enemy_hp} hp and {enemy_stamina} stamina")
            turn = name

       elif enemy_stamina >= 20:
            enemy_burst_attack = enemy.burst_atk()
            player_hp = player_hp - enemy_burst_attack
            enemy_stamina -= 20
            time.sleep(2)
            print (f"\n The enemy just did {enemy_burst_attack} damage!")
            BURST_SOUND.play()
            print (f"{name} now has {player_hp} hp and {player_stamina} stamina")
            time.sleep(2)
            print (f"The enemy now has {enemy_hp} hp and {enemy_stamina} stamina")
            turn = name

        else:
            enemy_norm_attack = enemy.normal_atk()
            player_hp = player_hp - enemy_norm_attack
            enemy_stamina += 10
            time.sleep(2)
            print (f"\nEnemy just did {enemy_norm_attack} damage!")
            ATTACK_SOUND.play()
            print (f"\n{name} now has {player_hp} hp and {player_stamina} stamina")
            print (f"The enemy now has {enemy_hp} hp and {enemy_stamina} stamina")
            turn = name

if player_hp <=0:
    print ("You Lost.")
elif enemy_hp <=0:
    print (f"\n{name}, you won!")


