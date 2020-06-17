#Pokemon class with parameters
class Pokemon:
  def __init__(self, name, pokemon_type, level = 5, is_knocked_out = False):
    self.name = name
    self.level = level
    self.experience = 0
    self.health = 5 * level
    self.max_health = 5 * level
    self.pokemon_type = pokemon_type
    self.is_knocked_out = is_knocked_out


#info about pokemon and its properties
  def __repr__(self):
    return "The {} was created! Current level: {}, type: {}, maximun health: {}, current health: {}.\n".format(self.name, self.level, self.pokemon_type, self.max_health, self.health)

  #resurrection
  def resurrection(self):
    self.is_knocked_out = False
    if self.health == 0:
      self.health = 1
    print("{name} was resurrected!".format(name = self.name))

  # knock out
  def knock_out(self):
    self.is_knocked_out = True
    if self.health != 0:
      self.health = 0
    print("{name} was knocked out!".format(name = self.name))

  #gain health
  def gain_health(self, points):
    if self.health == 0:
      self.resurrection()
    self.health += points
    if self.health > self.max_health:
      self.health = self.max_health
    print("{name} now has {health} points of health.".format(name = self.name, health = self.health))

  #loos health
  def loose_health(self, damage):
    self.health -= damage
    if self.health <= 0:
      self.health = 0
      self.knock_out()
    else:
      print("{name} received {damage} points of damage and now has {health} points of health.".format(name = self.name, damage = str(damage), health = round(self.health)))

  #attack
  def attack(self, opponent):
    if self.is_knocked_out:
      print("{name} can't attack because it is knocked out!".format(name = self.name))
      return
    if self.pokemon_type == 'Water':
      if opponent.pokemon_type == 'Fire':
        print("{name} attacked {opponent} for {damage} damage.".format(name = self.name, opponent = opponent.name, damage = round(self.level * 2)))
        self.get_experience(1)
        opponent.loose_health(self.level * 2)
      elif opponent.pokemon_type == 'Grass':
        print("{name} attacked {opponent} for {damage} damage.".format(name = self.name, opponent = opponent.name, damage = round(self.level * 0.5)))
        self.get_experience(1)
        opponent.loose_health(self.level * 0.5)
    elif self.pokemon_type == 'Fire':
      if opponent.pokemon_type == 'Grass':
        print("{name} attacked {opponent} for {damage} damage.".format(name = self.name, opponent = opponent.name, damage = round(self.level * 2)))
        self.get_experience(1)
        opponent.loose_health(self.level * 2)
      elif opponent.pokemon_type == 'Water':
        print("{name} attacked {opponent} for {damage} damage.".format(name = self.name, opponent = opponent.name, damage = round(self.level * 0.5)))
        self.get_experience(1)
        opponent.loose_health(self.level * 0.5)
    elif self.pokemon_type == 'Grass':
      if opponent.pokemon_type == 'Water':
        print("{name} attacked {opponent} for {damage} damage.".format(name = self.name, opponent = opponent.name, damage = round(self.level * 2)))
        self.get_experience(1)
        opponent.loose_health(self.level * 2)
      elif opponent.pokemon_type == 'Fire':
        print("{name} attacked {opponent} for {damage} damage.".format(name = self.name, opponent = opponent.name, damage = round(self.level * 0.5)))
        self.get_experience(1)
        opponent.loose_health(self.level * 0.5)

  #experience
  def get_experience(self, experience):
    self.experience += experience
    print("{name} gained 1 point of experience and has {experience} points of experience in total".format(name = self.name, experience = self.experience))

#subclasses of Pokemon class
class Fire_Pokemon(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Fire_Pokemon", "Fire", level)

class Water_Pokemon(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Water_Pokemon", "Water", level)

class Grass_Pokemon(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Grass_Pokemon", "Grass", level)

#Trainer class
class Trainer:
  def __init__(self, pokemons, potions, name):
    self.pokemons = pokemons
    self.potions = potions
    self.active_pokemon = 0
    self.name = name

  #Trainer info
  def __repr__(self):
    print("The trainer {name} has the following pokemon".format(name = self.name))
    for pokemon in self.pokemons:
      print(pokemon)
    return "The current active pokemon is {name}".format(name = self.pokemons[self.active_pokemon].name)

  #Pokemon switch
  def switch_active_pokemon(self, new_active):
    if new_active < len(self.pokemons) and new_active >= 0:
      if self.pokemons[new_active].is_knocked_out:
        print("{name} is knocked out. You can't make it your active pokemon".format(name = self.pokemons[new_active].name))
      elif new_active == self.active_pokemon:
        print("{name} is already your active pokemon".format(name = self.pokemons[new_active].name))
      else:
        self.active_pokemon = new_active
        print("Your turn {name}!".format(name = self.pokemons[self.active_pokemon].name))

  def use_potion(self):
    if self.potions > 0:
      print("You used {potion} points of potion on {name}.".format(potion = self.potions, name = self.pokemons[self.active_pokemon].name))
      self.pokemons[self.active_pokemon].gain_health(10)
      self.potions -= 1
    else:
      print("You don't have any more potions")

  #attack other trainer
  def attack_other_trainer(self, other_trainer):
    my_pokemon = self.pokemons[self.active_pokemon]
    their_pokemon = other_trainer.pokemons[other_trainer.active_pokemon]
    my_pokemon.attack(their_pokemon)


#making Pokemon
pokemon1 = Fire_Pokemon(6)
# print(pokemon1)
pokemon2 = Water_Pokemon(7)
# print(pokemon2)
pokemon3 = Grass_Pokemon(8)
# print(pokemon3)
pokemon4 = Fire_Pokemon(6)
# print(pokemon1)
pokemon5 = Water_Pokemon(4)
# print(pokemon2)
pokemon6 = Grass_Pokemon(6)
# print(pokemon3)

#making trainers
trainer1 = Trainer([pokemon1, pokemon2, pokemon3], 3, "Trainer1")
# print(trainer1)
trainer2 = Trainer([pokemon4, pokemon5, pokemon6], 5, "Trainer2")
# print(trainer2)

pokemon1.attack(pokemon2)
# pokemon1.attack(pokemon3)
# pokemon3.attack(pokemon1)

# trainer2.attack_other_trainer(trainer1)
# trainer1.attack_other_trainer(trainer2)

# trainer1.use_potion()
# trainer2.use_potion()

# trainer1.switch_active_pokemon(2)
# trainer2.switch_active_pokemon(1)
