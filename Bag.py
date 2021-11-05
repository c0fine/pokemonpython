#bag class
class Bag:
  def __init__(self, potions):
    #quantitiy of potions
    self.potions = potions
    self.inventory = [potions]
    self.contents = ["potion"]
  def use_item(self,item_choice,pokemon):
    #print(f"{item_choice} IS THE CHOICE")
    if(item_choice.lower()== "potion"):
      self.use_potion(pokemon)
  def use_potion(self,pokemon):
    #print("POTION IS BEING USED")
    if(not self.potions > 0):
      return False
    heal = 20
    pokemon.change_health(heal)
    print(f"{pokemon.name} used a potion, it has {pokemon.hp}hp")  
    self.potions = self.potions-1
    return True
  def __str__(self):
    return f"Potions: {self.potions}"