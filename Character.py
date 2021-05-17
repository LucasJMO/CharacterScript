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

def levelUp(Character,classLevel,rerollOne=False,increaseByAverage=False):
	Character.level += 1
	
	if classLevel == Classes.BARBARIAN:
		Character.barbarianLevel += 1
		Character.increaseHitpoints(12,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	elif classLevel == Classes.BARD:
		Character.bardLevel += 1
		Character.increaseHitpoints(6,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	elif classLevel == Classes.CLERIC:
		Character.clericLevel += 1
		Character.increaseHitpoints(8,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	elif classLevel == Classes.FIGHTER:
		Character.fighterLevel += 1
		Character.increaseHitpoints(10,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	elif classLevel == Classes.MONK:
		Character.monkLevel += 1
		Character.increaseHitpoints(8,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	elif classLevel == Classes.PALADIN:
		Character.paladinLevel += 1
		Character.increaseHitpoints(10,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	elif classLevel == Classes.RANGER:
		Character.rangerLevel += 1
		Character.increaseHitpoints(8,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	elif classLevel == Classes.ROGUE:
		Character.rogueLevel += 1
		Character.increaseHitpoints(6,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	elif classLevel == Classes.SORCERER:
		Character.sorcererLevel += 1
		Character.increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	elif classLevel == Classes.WIZARD:
		Character.wizardLevel += 1
		Character.increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)

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
	race = 0
	size = 0
	darkvision = 0 # Darkvision range in feet
	lowLightVision = False # False/True = has/doesn't have LLV
	###
	# Why is low light vision even a thing? It's actual effects are so vague that basically everyone just ignores them, and yet because
	# it's a racial trait it's one of the first things new players are going to see. Why muddy the waters like this? Just give elves
	# 30 feet of darkvision or something and be done with it.
	# inb4 "But illumination!" Nobody tracks that, it's annoying, if you do track it congratulations on being a massive nerd
	###
	firstLevelBonusFeats = 0
	bonusSkillPoints = 0
	def assignAbilityScores(con,dex,str,cha,int,wis):
		con = con
		dex = dex
		str = str
		cha = cha 
		int = int 
		wis = wis
	def abilityScorePointBuy(totalPoints,con,dex,str,cha,int,wis):
		scoreCost = [0,1,2,3,4,5,6,8,10,13,16] # Ability score - 8 to get point cost
		totalPoints -= scoreCost[con-8]
		totalPoints -= scoreCost[dex-8]
		totalPoints -= scoreCost[str-8] # I should change str & int 
		totalPoints -= scoreCost[cha-8]
		totalPoints -= scoreCost[int-8]
		totalPoints -= scoreCost[wis-8]
		if totalPoints < 0:
			return
		assignAbilityScores(con=con,dex=dex,str=str,cha=cha,int=int,wis=wis)
	def increaseHitpoints(hitDie,rerollOne=False,increaseByAverage=False):
		# hitDie = number of sides, 4 for d4, 6 for d6, etc
		if level == 1:
			baseHitpoints += hitDie
		elif increaseByAverage:
			if level%2==0:
				baseHitpoints += int(hitDie/2)
			else:
				baseHitpoints += int(hitDie/2)+1
		elif rerollOne:
			baseHitpoints += randint(2,hitDie)
		else:
			baseHitpoints += randint(1,hitDie)
	def applyPaladin1(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(12,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyPaladin2(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(12,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyPaladin3(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(12,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyPaladin4(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(12,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyPaladin5(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(12,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyPaladin6(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(12,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRanger1(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(10,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRanger2(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(10,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRanger3(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(10,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRanger4(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(10,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRanger5(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(10,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRanger6(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(10,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRogue1(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(6,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRogue2(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(6,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRogue3(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(6,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRogue4(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(6,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRogue5(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(6,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyRogue6(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(6,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applySorcerer1(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applySorcerer2(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applySorcerer3(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applySorcerer4(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applySorcerer5(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applySorcerer6(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyWizard1(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyWizard2(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyWizard3(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyWizard4(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyWizard5(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
	def applyWizard6(rerollOne=False,increaseByAverage=False):
		level += 1
		increaseHitpoints(4,rerollOne=rerollOne,increaseByAverage=increaseByAverage)
