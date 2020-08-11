class Pokemon:
	def __init__(self, name, level, type, current_health, is_knocked_out):
		self.name = name
		self.level = level
		self.type = type
		self.maximum_health = level*10
		self.current_health = current_health
		self.is_knocked_out = is_knocked_out
		self.experience = 0

	def __repr__(self):
		return "This pokemon is called {}".format(self.name)

	def lose_health(self, hp):     									#hp is a number coming from the attack method
		if self.is_knocked_out == False:
			if (self.current_health - hp) > 0:
				self.current_health = self.current_health - hp
				return self.current_health
			else:
				self.is_knocked_out = True
				self.current_health = 0
				return "Your pokemon is knocked out"
		else:
			self.current_health = 0
			return "Your pokemon is already knocked out"
	
	def gain_health(self, hp):
		self.is_knocked_out = False
		#if current health equals max health
		if self.current_health == self.maximum_health:
			return '{} is already fully healed'.format(self.name)
		#if added health exceeds max health	
		elif self.current_health + hp >= self.maximum_health:
			self.current_health = self.maximum_health
			return '{} fully healed and now has {} health points'\
			.format(self.name, self.current_health)		
		else:
			#gaining health normally
			self.current_health = self.current_health + hp
			return '{} partially healed and now has {} health points'\
			.format(self.name, self.current_health)
		
	def attack(self, pokemon):
		if pokemon.is_knocked_out == True:
			return '{} is already knocked out.'.format(pokemon.name)
		if self.is_knocked_out == True:
			return '{} is knocked out and needs health before fighting {}'\
			.format(self.name, pokemon.name)
		self.experience += 25
		if self.experience >= 50:
			self.level = self.level + 1
			self.experience = 0
		if self.type == 'Fire':
		#Fire pokemon scenarios
		
			if pokemon.type == self.type or pokemon.type == 'Water':
				pokemon.lose_health(int((self.level)/2))
				return "{} was attacked and now has {} health points. \nIt wasn't very effective."\
				.format(pokemon.name, pokemon.current_health)
			if pokemon.type == 'Grass':
				pokemon.lose_health((self.level)*2)
				return "{} was attacked and now has {} health points. \nIt was super effective!."\
				.format(pokemon.name, pokemon.current_health)
				
		if self.type == 'Water':
		#Water pokemon scenarios
		
			if pokemon.type == 'Grass' or pokemon.type == self.type:
				pokemon.lose_health(int((self.level)/2))
				return "{} was attacked and now has {} health points. \nIt wasn't very effective."\
				.format(pokemon.name, pokemon.current_health)
			if pokemon.type == 'Fire':
				pokemon.lose_health((self.level)*2)
				return "{} was attacked and now has {} health points. \nIt was super effective!."\
				.format(pokemon.name, pokemon.current_health)

		if self.type == 'Grass':
		#Grass pokemon scenarios
			if pokemon.type == self.type or pokemon.type == 'Fire':
				pokemon.lose_health(int((self.level)/2))
				return "{} was attacked and now has {} health points. \nIt wasn't very effective."\
				.format(pokemon.name, pokemon.current_health)
			if pokemon.type == 'Water':
				pokemon.lose_health((self.level)*2)
				return "{} was attacked and now has {} health points. \nIt was super effective!."\
				.format(pokemon.name, pokemon.current_health)
				

class Trainer:
	def __init__(self, name, pokemons, potions):
		self.name = name
		self.pokemons = pokemons
		self.potions = potions
		self.current_pokemon = pokemons[0]
		
	def __repr__(self):
		return 'Hi {}, your current pokemon is {}.'\
		.format(self.name, self.current_pokemon.name)
	
	def use_potion(self, potion):
		if potion not in self.potions:
			return "You don't have that potion"
		index = self.potions.index(potion)
		self.current_pokemon.gain_health(self.potions[index].healing)
		self.potions.pop(index)
		return '{} gained {} health points from {}. \nThey now have {} health points'\
		.format(self.current_pokemon.name, potion.healing, potion.name, self.current_pokemon.current_health)
	
	def switch_pokemon(self, pokemon):
		if pokemon.is_knocked_out == True:
			return "{} is already knocked out they cannot be used right now."\
			.format(pokemon.name)
		index = self.pokemons.index(pokemon)
		self.current_pokemon = self.pokemons[index]
		return '{} switched their current pokemon to {}'.format(self.name, self.current_pokemon.name)
		
	def attack_trainer(self, trainer):
		if self.current_pokemon.is_knocked_out == True:
			return "{} is knocked out. Switch your current pokemon.".format(self.current_pokemon.name)
		if trainer.current_pokemon.is_knocked_out == True:
			return "{}'s current pokemon is already knocked out".format(trainer.name)
		self.current_pokemon.attack(trainer.current_pokemon)
		return "{}'s {} attacked {}'s {} and now \nthey only have {} health points."\
		.format(self.name, self.current_pokemon.name, trainer.name, \
		trainer.current_pokemon.name, trainer.current_pokemon.current_health)
		
		
class Potion:
	def __init__(self, name, health):
		self.name = name
		self.healing = health
	def __repr__(self):
		return '{} heals your pokemon by {} health points'.format(self.name, self.healing)

class Russell(Pokemon):
	def revive(self):
		if self.is_knocked_out == True:
			self.gain_health(50)
			return '{} revived himself!'.format(self.name)

	
	

charizard = Pokemon('Charizard', 20, 'Fire', 100, False)
blastoise = Pokemon('Blastoise', 15, 'Water', 90, False)
bulbasaur = Pokemon('Bulbasaur', 14, 'Grass', 80, False)
russell = Russell('Russell', 27, 'Grass', 120, False)
fresa = Pokemon('Fresa', 5, 'Water', 45, False)
flareon = Pokemon('Flareon', 16, 'Fire', 90, False)
becky = Pokemon('Becky', 6, 'Grass', 55, False)
maya = Pokemon('Maya', 6, 'Water', 60, False)

pokemon_list = [charizard, blastoise, bulbasaur, russell, fresa, flareon, becky, maya]
	
blue_potion = Potion('Blue potion', 40)
red_potion = Potion('Red potion', 60)
ancient_potion = Potion('Ancient potion', 95) 

potion_list = [blue_potion, red_potion, ancient_potion]


henry = Trainer('Henry', [charizard, blastoise, bulbasaur, russell, flareon, fresa], potion_list)
maddie = Trainer('Maddie', [charizard, becky, maya, flareon, bulbasaur, blastoise], potion_list)


henry.switch_pokemon(russell)
maddie.switch_pokemon(charizard)
print(charizard)

print(henry.attack_trainer(maddie))





