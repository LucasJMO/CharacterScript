from enum import Enum
# Given that there could wind up being a lot of Enums (Size, Race, Language, Age, etc) I decided it would be best to split them off into
# their own file, as Character.py was already becoming very long and unwieldy 
class Classes(Enum):
	BARBARIAN=1
	BARD=2
	CLERIC=3
	FIGHTER=4
	PALADIN=5
	RANGER=6
	ROGUE=7
	SORCERER=9
	WIZARD=10

class Size(Enum):
	FINE=1
	DIMINUTIVE=2
	TINY=3
	SMALL=4
	MEDIUM=5
	LARGE=6
	HUGE=7
	GARGANTUAN=8
	COLOSSAL=9

class Race(Enum):
	DWARF=1
	ELF=2
	GNOME=3
	HALFELF=4
	HALFLING=5
	HALFORC=6
	HUMAN=7