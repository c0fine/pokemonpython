import random
import time 
import sys
from Bag import Bag
from Moves import Moves
from Pokemon import Pokemon
from Mechanics import Mechanics



def make_starters(): #makes starter pokemon options 
  
  #To create each pokemon 
  #pokemon name = Pokemon("pokemonname",level,current_hp,max_hp)
  #Example:
  turtwig = Pokemon("Turtwig",12,55,55) #create pokemon
  #pokemon name.add_move("movename",damage,"discription")
  turtwig.add_move("tackle",8,"Charges at the foe with a full body attack") #add move to pokemon 
  turtwig.add_move("absorb",4,"does not do what it should, just does 4 damage")
  turtwig.add_move("razor leaf",10,"a sharp edged leaf is launched to slash at the foe")
  turtwig.add_move("test",100,"a sharp edged leaf is launched to slash at the foe")
  
  starter_pokemon = [] #create list of potential starter pokemon
  starter_pokemon.append(turtwig) #add turtwig to list of potential starter pokemon
  return starter_pokemon  #return  list of potential starter pokemon



def battle_pokemon():  #make easy enemy pokemon
  #pokemon name = Pokemon("Pokemonname", level, current_hp,max_hp)
  maril = Pokemon("Maril",12,55,55)
  #pokemonname.add_move("move name",damage,"discription")
  maril.add_move("tackle",8,"Charges at the foe with a full body attack")

  battle_pokemon = []
  battle_pokemon.append(maril) #add pokemon to the list of potential enemies 

  return battle_pokemon #returns the list of potential enemies 



def medium_pokemon():
  nidoqueen = Pokemon("Nidoqueen",24,75,75)
  nidoqueen.add_move("Fury Swipes",20,"Swipes at foe")
  
  med_pokemon = []
  med_pokemon.append(nidoqueen)
 
  return med_pokemon

def hard_pokemon():

  charizard = Pokemon("Charizard",30,76,76)
  charizard.add_move("Dragon Breath",45,"Fire but from mouth")

  hard_enemy = []
  hard_enemy.append(charizard)


  return hard_enemy

#actual game play code

#intro
print("Why hello young trainer, you have quite the adventure ahead of you")
#player name and validation 
okay = False
while(not okay == True):
  name = input("What is your name? ")
  print(f"Your name is {name} correct? (yes/no)")
  okay=input().lower()
  if(okay=="yes"):
    okay = True
#story to get you to the professor's lab
print("Your mom wakes you up")
print(f"'Wake up {name}! You're going to be late to meet Professor Palm!'")
time.sleep(.5)
input("Press enter to continue")
print("You get out of bed and survey your room. Would you like to investigate or leave for your meeting? (investigate/leave)")
decision = input().lower()
if(decision == "investigate"):
  print("You see medals hanging on the wall from when you were younger, as your TV plays in the background. Someone is discussing Professor Palm's groundbreaking Pokemon research")
print("You go down stairs and say goodbye to your mom on the way out of the door and begin the walk to professor Palm's house")
print(".....")
time.sleep(3)
print("As you arrive at professor Plum's house she comes out to greet you.")
print(f"'{name}, right on time. Come on in'")
time.sleep(.5)
print("'I have asked you here today to help me with a very important venture'")
time.sleep(.5)
print("'You may have heard of my Pokemon research. To continue my findings I need you to gather data about Pokemon in the wild.'")
time.sleep(.5)
print("'Take this, it will be instramental on your journey'")
print(f"🌟{name} aquired a pokedex🌟")
time.sleep(1)
print("You will also need a companion to accompany you on your journey")
#choose starters 
choices = make_starters()
picked_pokemon = Mechanics.choose_starter(choices)
#story to get to battles
time.sleep(1.5)
print(f"A {picked_pokemon.name} what a wonderful choice")
print("That is all I have for you today, young adventurer. It is time for you to begin your Pokemon journey")
print("The best way to train your pokemon is in battle, maybe you should start with route 1")
print(".....")
time.sleep(1.5)
print("You leave the professor's house and find your way to the entrance of route 1")
print("Are you ready to begin? Press enter to contihnue")
#begin battles
input()
battles_won = 0
my_bag = Bag(10)
for i in range(3):
  wild = battle_pokemon()
  enemy1 = random.choice(wild)
  print(f"A wild {enemy1.name} appeared")
  
  winner1 = Mechanics.battle2(picked_pokemon,enemy1,my_bag)
  if(not winner1.name==picked_pokemon.name):
    print(f"You won {battles_won} battles")
    print("You lost :(")
    sys.exit(0)
  battles_won = battles_won+1

#if survived move to next tier of battles and level up your pokemon
picked_pokemon.level_up()

for j in range(4):
  wild_med = medium_pokemon()
  enemy_med = random.choice(wild_med)
  print(f"A wild {enemy_med.name} appeared")
  #winner_med = Mechanics.battle(picked_pokemon,enemy_med)
  winner_med  = Mechanics.battle2(picked_pokemon,enemy_med)
  if(not winner_med.name == picked_pokemon.name):
    print(f"You won {battles_won}")
    print("But you still lost :(")
    sys.exit(0)
  battles_won = battles_won + 1
#if survived move to next tier of battles and level up your pokemon
picked_pokemon.level_up()

for k in range(5):
  wild_hard = hard_pokemon()
  enemy_hard = random.choice(wild_hard)
  print(f"A wild {enemy_hard.name} appeared")
  #winner_med = Mechanics.battle(picked_pokemon,enemy_med)
  winner_hard  = Mechanics.battle2(picked_pokemon,enemy_hard)
  if(not winner_hard.name == picked_pokemon.name):
    print(f"You won {battles_won}")
    print("But you still lost :(")
    sys.exit(0)
  battles_won = battles_won + 1

#you won!
