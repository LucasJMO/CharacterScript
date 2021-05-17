#import json
from random import randint

from ETypes import Classes
from ETypes import Race
from ETypes import Size

import Barbarian
import Bard
import Cleric
import Fighter
import Monk
import Paladin
import Ranger
import Rogue
import Sorcerer
import Wizard

class Character:
	# Ability Scores
	con = 0
	dex = 0
	str = 0
	cha = 0
	int = 0
	wis = 0
	# Ability Score Modifiers
	conRacialMod = 0
	dexRacialMod = 0
	strRacialMod = 0
	chaRacialMod = 0
	intRacialMod = 0
	wisRacialMod = 0
	# Character Variables
	level = 0
	barbarianLevel = 0
	bardLevel = 0
	clericLevel = 0
	fighterLevel = 0
	paladinLevel = 0
	rangerLevel = 0
	rogueLevel = 0
	sorcererLevel = 0
	wizardLevel = 0
	languages = ["Common"]
	AC = 0
	BAB = 0
	baseHitpoints = 0
	fortitude = 0
	reflex = 0
	will = 0
	speed = 0 # base land speed in feet
	race = Race.UNSPECIFIED
	size = Size.UNSPECIFIED
	darkvision = 0 # Darkvision range in feet
	lowLightVision = False # False/True = has/doesn't have LLV
	###
	# Why is low light vision even a thing? Its actual effects are so vague that basically everyone just ignores them, and yet because
	# it's a racial trait it's one of the first things new players are going to see. Why muddy the waters like this? Just give elves
	# 30 feet of darkvision or something and be done with it.
	# inb4 "But illumination!" Nobody tracks that, it's annoying, if you do track it congratulations on being a massive nerd
	###
	firstLevelBonusFeats = 0
	bonusSkillPoints = 0
	def assignAbilityScores(self,character,con,dex,str,cha,int,wis):
		self.con = con
		self.dex = dex
		self.str = str
		self.cha = cha 
		self.int = int 
		self.wis = wis
	def increaseHitpoints(self,hitDie,rerollOne=False,increaseByAverage=False):
		# hitDie = number of sides, 4 for d4, 6 for d6, etc
		if self.level == 1:
			self.baseHitpoints += hitDie
		elif increaseByAverage:
			if level%2==0:
				self.baseHitpoints += int(hitDie/2)
			else:
				self.baseHitpoints += int(hitDie/2)+1
		elif rerollOne:
			self.baseHitpoints += randint(2,hitDie)
		else:
			self.baseHitpoints += randint(1,hitDie)	
	def levelUp(self,classLevel,rerollOne=False,increaseByAverage=False):
		# classLevel is an enumerated type specified in ETypes.Class
		self.level += 1
		if classLevel == Classes.BARBARIAN:
			self.barbarianLevel += 1
			increaseHitpoints(12,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
			Bard.applyBardLevel(self)
		elif classLevel == Classes.BARD:
			self.bardLevel += 1
			self.increaseHitpoints(6,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
			Barbarian.applyBarbarianLevel(self)
		elif classLevel == Classes.CLERIC:
			self.clericLevel += 1
			self.increaseHitpoints(8,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
			Cleric.applyClericLevel(self)
		elif classLevel == Classes.FIGHTER:
			self.fighterLevel += 1
			self.increaseHitpoints(10,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
			Fighter.applyFighterLevel(self)
		elif classLevel == Classes.MONK:
			self.monkLevel += 1
			self.increaseHitpoints(8,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
			Monk.applyMonkLevel(self)
		elif classLevel == Classes.PALADIN:
			self.paladinLevel += 1
			self.increaseHitpoints(10,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
			Paladin.applyPaladinLevel(self)
		elif classLevel == Classes.RANGER:
			self.rangerLevel += 1
			self.increaseHitpoints(8,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
			Ranger.applyRangerLevel(self)
		elif classLevel == Classes.ROGUE:
			self.rogueLevel += 1
			self.increaseHitpoints(6,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
			Rogue.applyRogueLevel(self)
		elif classLevel == Classes.SORCERER:
			self.sorcererLevel += 1
			self.increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
			Sorcerer.applySorcererLevel(self)
		elif classLevel == Classes.WIZARD:
			self.wizardLevel += 1
			self.increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
			Wizard.applyWizardLevel(self)	
