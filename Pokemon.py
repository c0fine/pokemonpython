from Moves import Moves
import random
class Pokemon:
  def __init__(self, name,level,hp,max_hp):
    self.name = name
    self.level = level
    self.hp = hp
    self.max_hp = max_hp
    self.pokemon_moves = []
  def add_move(self,move_name,move_damage,move_disc):
    new_move = Moves(move_name,move_damage,move_disc)
    self.pokemon_moves.append(new_move) 
  def print_moves(self):
    for item in self.pokemon_moves:
      print(item)
  def change_health(self,change):
    self.hp = self.hp + change
    return self.hp
  def full_heal(self):
    self.hp = self.max_hp
    return self.hp
  def random_move(self):
    move = random.choice(self.pokemon_moves)
    return move
  def use_move(self,move,target):
    damage = -move.damage
    new_health = target.change_health(damage)
    if(new_health < 0):
      print(f"{self.name} used {move.name}. {target.name} has 0 hp remaining")
      return False 
    else:
      print(f"{self.name} used {move.name}. {target.name} as {new_health}hp remaining")
      return True 
  def level_up(self):
    self.max_hp = self.max_hp + 20
    self.hp = self.max_hp  
    for each in self.pokemon_moves:
      each.damage = each.damage + random.randint(10,15)

