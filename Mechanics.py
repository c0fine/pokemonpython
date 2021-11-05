class Mechanics:
  def choose_starter(options):
    names = []
    for pokemon in options:
      names.append(pokemon.name.lower())
    chosen = ""    
    sure = ""
    while(not sure == "yes"):
      print("You have three options choose wisely")
      for pokemon in names:
        print(pokemon)
      while(chosen not in names):
        chosen = input("Who do you choose? ").lower()
      sure = input("Are you sure (yes/no)").lower()
    num = 0
    for pokemon in names:
      if (pokemon == chosen):
        break
      num = num + 1
    return options[num]
  def choose_move(pokemon):
    choice = ""
    sure = ""
    moves = pokemon.pokemon_moves
    move_names = []
    for each in moves:
      move_names.append(each.name.lower())
    while(not sure == "yes"):
      print("Choose which move you'd like to use")
      pokemon.print_moves()
      choice = input().lower()
      while(not choice in move_names):
        print("That was not one of the moves, please try again")
        choice = input().lower()
      sure = input(f"You want to use {choice}? (yes/no)").lower()
    number = move_names.index(choice)
    return moves[number]    
  def choose_option():
    play_choice = ""
    play_options = ["bag","move"]
    while(play_choice not in play_options):
      print("Would you like to use a move or the bag? (move/bag)")
      play_choice = input().lower()
    return play_choice   
  def battle(player,enemy):
    enemy.full_heal()
    player.full_heal()
    while(player.hp>0 and enemy.hp>0):
      enemy_move = enemy.random_move()
      feint = enemy.use_move(enemy_move,player)
      if(not feint):
        return enemy
      player_move = Mechanics.choose_move(player)
      feint = player.use_move(player_move,enemy)
      if(not feint):
        return player
  def battle2(player,enemy,bag):
    enemy.full_heal()
    player.full_heal()
    while(player.hp>0 and enemy.hp>0):
      enemy_move = enemy.random_move()
      feint = enemy.use_move(enemy_move,player)
      if(not feint):
        return enemy
      gameplay_choice = Mechanics.choose_option()
      if(gameplay_choice == "move"):
        player_move = Mechanics.choose_move(player)
        feint = player.use_move(player_move,enemy)
        if(not feint):
          return player
      elif(gameplay_choice == "bag"):
        chosen_item = Mechanics.choose_item(bag)
        bag.use_item(chosen_item,player)
      
  def choose_item(player_bag):
    print(player_bag)
    item_choice = ""
    while(item_choice not in player_bag.contents):
      print("Enter the item you would like to use")
      item_choice= input().lower()
    num = player_bag.contents.index(item_choice)
    if(player_bag.inventory[num] == 0):
      return "no"
    return player_bag.contents[num]
    