scoreCost = [0,1,2,3,4,5,6,8,10,13,16] # Ability score - 8 to get point cost

def abilityScorePointBuy(totalPoints,con,dex,str,cha,int,wis): # I should rewrite this/move this method
	totalPoints -= scoreCost[con-8]
	totalPoints -= scoreCost[dex-8]
	totalPoints -= scoreCost[str-8] # I should change str & int 
	totalPoints -= scoreCost[cha-8]
	totalPoints -= scoreCost[int-8]
	totalPoints -= scoreCost[wis-8]
	if totalPoints < 0:
		return
	assignAbilityScores(con=con,dex=dex,str=str,cha=cha,int=int,wis=wis)
def pointBuyCost(con,dex,str,cha,int,wis):
	totalPoints = 0
	totalPoints += scoreCost[con-8]
	totalPoints += scoreCost[dex-8]
	totalPoints += scoreCost[str-8] # I should change str & int 
	totalPoints += scoreCost[cha-8]
	totalPoints += scoreCost[int-8]
	totalPoints += scoreCost[wis-8]
	return totalPoints