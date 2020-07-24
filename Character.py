import json

flist = []

class Character:
	# Ability Scores
	_con = 0
	_dex = 0
	_str = 0
	_cha = 0
	_int = 0
	_wis = 0
	# Ability Score Modifiers
	_conRacialMod = 0
	_dexRacialMod = 0
	_strRacialMod = 0
	_chaRacialMod = 0
	_intRacialMod = 0
	_wisRacialMod = 0
	# Character Variables
	_level = 0
	_classes = []
	_languages = ["Common"]
	_AC = 0
	_hitpoints = 0
	_fortitude = 0
	_reflex = 0
	_will = 0
	_speed = 0 # base land speed in feet
	_race = ""
	_size = ""
	_darkvision = 0 # Darkvision range in feet
	# To avoid having to check for racial feats
	_firstLevelBonusFeats = 0
	_bonusSkillPoints = 1
	#def __init__(name=""):

	def func():
		print(_AC)
	def applyRaceHuman():
		_race = "Human"
		_size = "Medium"
		_firstLevelBonusFeats = 1
		_bonusSkillPoints = 1
		_speed = 30
	def applyRaceDwarf():
		_race = "Dwarf"
		_size = "Medium"
		_conRacialMod = 2
		_chaRacialMod = -2
		_speed = 20
		_darkvision = 60
		_languages.append("Dwarven")
		#stonecunning
		#weapon familiarity
		#stability: when standing on the ground a dwarf gains a +4 bonus on ability checks made to resist being bull rushed or tripped 
		#+2 racial bonus on saving throws against poison
		#+2 racial bonus on saving throws against spells and spell like effects
		#+1 racial bonus on attack rolls against orcs and goblinoids
		#+4 dodge bonus to Armor Class against monsters of the giant type. Any time a creature loses its Dexterity bonus (if any) to Armor Class, such as when it's caught flat footed, it loses its dodge bonus, too.
		#+2 racial bonus on Appraise checks that are related to stone or metal.
		#+2 racial bonus on Craft checks that are related to stone or metal.			
	def applyRaceElf():
		_race = "Elf"
		_size = "Medium"
		_dexRacialMod = 2
		_conRacialMod = -2
		_speed = 30
		#low light vision: Ok so 'twice as far', what does that even mean? Why do we need low light and darkvision?
		#immunity to magic sleep effects, and a +2 racial saving throw bonus against enchantment spells or effects
		#weapon proficiency: Elves receive the Martial Weapon Proficiency feats for the longsword, rapier, longbow (including composite longbow), and shortbow (including composite shortbow) as bonus feats
		#+2 racial bonus on Listen, Search, and Spot checks. An elf who merely passes within 5 feet of a secret or concealed door is entitled to a Search check to notice it as if she were actively looking for it.
		_languages.append("Elven")		
	def applyRaceGnome():
		_race = "Gnome"
		_size = "Small"
		_speed = 20
		#low light vision
		#weapon familiarity
		#+2 racial bonus on saving throws against illusions
		#+1 DC for saving throws against illusion spells cast by gnomes. This adjustment stacks with those from similar effects.
		#+4 dodge bonus to AC against monsters of the giant type. 
		#+2 racial bonus on listen checks
		#+2 racial bonus on Craft (alchemy) checks.
		_languages.append("Gnome")
		#spell like abilities: 1/day-speak with animals (burrowing mammal only, duration 1 minute). A gnome with a Charisma score of at least 10 also has the following spell like abilities: 1/day-dancing lights, ghost sound, prestidigitation. Caster level 1st; save DC 10+gnome's Cha modifier+spell level
	def applyRaceHalfElf():
		_race = "Half-Elf"
		_size = "Medium"
		_speed = 30
		#immunity to magic sleep effects, and a +2 racial saving throw bonus against enchantment spells or effects
		#low light vision
		#+1 racial bonus on listen, search, and spot checks
		#Elven blood: For all effects related to race, a half-elf is considered an elf
		_languages.append("Elven")
	def applyRaceHalfOrc():
		_race = "Half-Orc"
		_size = "Medium"
		_speed = 30
		_strRacialMod = 2
		_intRacialMod = -2
		_chaRacialMod = -2
		# a half orc's starting intelligence score is always at least 3. If this adjustment would lower the character's score to 1 or 2, his score is nevertheless 3.
		_darkvision = 60
		#Orc blood: For all effects related to race, a half-orc is considered an orc
		_languages.append("Orc")
	def applyRaceHalfling():
		_race = "Halfling"
		_size = "Small"
		_speed = 20
		_dexRacialMod = 2
		_strRacialMod = -2
		#+2 racial bonus on climb, jump, listen, and move silently checks
		#+1 racial bonus on all saving throws
		#+2 morale bonus on saving throws against fear: This bonus stacks with the halfling's +1 bonus on saving throws in general
		#+1 racial bonus on attack rolls with thrown weapons and slings
		_languages.append("Halfling")