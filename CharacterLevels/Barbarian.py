def applyBarbarianLevel(character):
	if character.barbarianLevel == 1:
		character.BAB += 1
		character.fortitude += 2
		character.barbarianFastMovement += 10
		character.barbarianRagesPerDay += 1
		if character.level == 1:
			character.barbarianIlliterate = True
	elif character.barbarianLevel == 2:
		character.BAB += 1
		character.fortitude += 1
		if character.uncannyDodge == True:
			character.improvedUncannyDodge = True
		character.uncannyDodge = True
	elif character.barbarianLevel == 3:
		character.BAB += 1
		character.reflex += 1
		character.will += 1
		character.trapSense += 1
	elif character.barbarianLevel == 4:
		character.BAB += 1
		character.fortitude += 1
		character.barbarianRagesPerDay += 1
	elif character.barbarianLevel == 5:
		character.BAB += 1
		character.improvedUncannyDodge = True
	elif character.barbarianLevel == 6:
		character.BAB += 1
		character.fortitude += 1
		character.reflex += 1
		character.will += 1
		character.trapSense += 1
	elif character.barbarianLevel == 7:
		character.BAB += 1
		barbarianDamageReduction += 1
	elif character.barbarianLevel == 8:
		character.BAB += 1
		character.fortitude += 1
		character.barbarianRagesPerDay += 1
	elif character.barbarianLevel == 9:
		character.BAB += 1
		character.reflex += 1
		character.will += 1
		character.trapSense += 1
	elif character.barbarianLevel == 10:
		character.BAB += 1
		character.fortitude += 1
		character.barbarianDamageReduction += 1
	elif character.barbarianLevel == 11:
		character.BAB += 1
		character.barbarianGreaterRage = True
	elif character.barbarianLevel == 12:
		character.BAB += 1
		character.fortitude += 1
		character.reflex += 1
		character.will += 1
		character.barbarianRagesPerDay += 1
		character.trapSense += 1
	elif character.barbarianLevel == 13:
		character.BAB += 1
		character.barbarianDamageReduction += 1
	elif character.barbarianLevel == 14:
		character.BAB += 1
		character.fortitude += 1
		character.barbarianIndomitableWill = True
	elif character.barbarianLevel == 15:
		character.BAB += 1
		character.reflex += 1
		character.will += 1
		character.trapSense += 1
	elif character.barbarianLevel == 16:
		character.BAB += 1
		character.fortitude += 1
		character.barbarianDamageReduction += 1
		character.barbarianRagesPerDay += 1
	elif character.barbarianLevel == 17:
		character.BAB += 1
		character.barbarianTirelessRage = True
	elif character.barbarianLevel == 18:
		character.BAB += 1
		character.fortitude += 1
		character.reflex += 1
		character.will += 1
		character.trapSense += 1
		character.barbarianDamageReduction += 1
	elif character.barbarianLevel == 19:
		character.BAB += 1
		character.barbarianDamageReduction += 1
	elif character.barbarianLevel == 20:
		character.BAB += 1
		character.barbarianMightyRage = True
		character.barbarianRagesPerDay += 1