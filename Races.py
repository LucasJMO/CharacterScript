from Character import Character

def applyRaceHuman(Character):
	Character.race = Race.HUMAN
	Character.size = Size.MEDIUM
	Character.firstLevelBonusFeats = 1
	Character.bonusSkillPoints = 1
	Character.speed = 30
def applyRaceDwarf(Character):
	Character.race = Race.DWARF
	Character.size = Size.MEDIUM
	Character.conRacialMod = 2
	Character.chaRacialMod = -2
	Character.speed = 20
	Character.darkvision = 60
	Character.languages.append("Dwarven")
	#stonecunning
	#weapon familiarity
	#stability: when standing on the ground a dwarf gains a +4 bonus on ability checks made to resist being bull rushed or tripped 
	#+2 racial bonus on saving throws against poison
	#+2 racial bonus on saving throws against spells and spell like effects
	#+1 racial bonus on attack rolls against orcs and goblinoids
	#+4 dodge bonus to Armor Class against monsters of the giant type. Any time a creature loses its Dexterity bonus (if any) to Armor Class, such as when it's caught flat footed, it loses its dodge bonus, too.
	#+2 racial bonus on Appraise checks that are related to stone or metal.
	#+2 racial bonus on Craft checks that are related to stone or metal.			
def applyRaceElf(Character):
	Character.race = Race.ELF
	Character.size = Size.MEDIUM
	Character.dexRacialMod = 2
	Character.conRacialMod = -2
	Character.speed = 30
	Character.lowLightVision = True
	#immunity to magic sleep effects, and a +2 racial saving throw bonus against enchantment spells or effects
	#weapon proficiency: Elves receive the Martial Weapon Proficiency feats for the longsword, rapier, longbow (including composite longbow), and shortbow (including composite shortbow) as bonus feats
	#+2 racial bonus on Listen, Search, and Spot checks. An elf who merely passes within 5 feet of a secret or concealed door is entitled to a Search check to notice it as if she were actively looking for it.
	Character.languages.append("Elven")		
def applyRaceGnome(Character):
	Character.race = Race.GNOME
	Character.size = Size.SMALL
	Character.speed = 20
	#low light vision
	#weapon familiarity
	#+2 racial bonus on saving throws against illusions
	#+1 DC for saving throws against illusion spells cast by gnomes. This adjustment stacks with those from similar effects.
	#+4 dodge bonus to AC against monsters of the giant type. 
	#+2 racial bonus on listen checks
	#+2 racial bonus on Craft (alchemy) checks.
	Character.languages.append("Gnome")
	#spell like abilities: 1/day-speak with animals (burrowing mammal only, duration 1 minute). A gnome with a Charisma score of at least 10 also has the following spell like abilities: 1/day-dancing lights, ghost sound, prestidigitation. Caster level 1st; save DC 10+gnome's Cha modifier+spell level
def applyRaceHalfElf(Character):
	Character.race = Race.HALFELF
	Character.size = Size.MEDIUM
	Character.speed = 30
	#immunity to magic sleep effects, and a +2 racial saving throw bonus against enchantment spells or effects
	#low light vision
	#+1 racial bonus on listen, search, and spot checks
	#Elven blood: For all effects related to race, a half-elf is considered an elf
	Character.languages.append("Elven")
def applyRaceHalfOrc(Character):
	Character.race = Race.HALFORC
	Character.size = Size.MEDIUM
	Character.speed = 30
	Character.strRacialMod = 2
	Character.intRacialMod = -2
	Character.chaRacialMod = -2
	# a half orc's starting intelligence score is always at least 3. If this adjustment would lower the character's score to 1 or 2, his score is nevertheless 3.
	Character.darkvision = 60
	#Orc blood: For all effects related to race, a half-orc is considered an orc
	Character.languages.append("Orc")
def applyRaceHalfling(Character):
	Character.race = Race.HALFLING
	Character.size = Size.SMALL
	Character.speed = 20
	Character.dexRacialMod = 2
	Character.strRacialMod = -2
	#+2 racial bonus on climb, jump, listen, and move silently checks
	#+1 racial bonus on all saving throws
	#+2 morale bonus on saving throws against fear: This bonus stacks with the halfling's +1 bonus on saving throws in general
	#+1 racial bonus on attack rolls with thrown weapons and slings
	Character.languages.append("Halfling")