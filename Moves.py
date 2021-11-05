#############
#Moves class
class Moves:
  def __init__(self,name,damage,disc):
    self.name = name
    self.damage = damage
    self.disc = disc
  def __str__(self):
    return f"{self.name}|{self.disc}| Damage: {self.damage}"
    #Tackle|flings body at enemy| Damage: 12
