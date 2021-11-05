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

#player name and validation 

#story to get you to the professor's lab

#choose starters 

#story to get to battles
#initalize everything for battles
battles_won = 0
my_bag = Bag(10)
#start first battle loop


#if survived move to next tier of battles and level up your pokemon

#start next difficulty of battle

#if survived move to next tier of battles and level up your pokemon

#start next difficulty of battle


#you won!
