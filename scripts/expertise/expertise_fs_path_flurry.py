import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'force_sensitive_1a':
		return

	actor.addSkill('expertise_fs_path_flurry')


	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'force_sensitive_1a':
		return

	actor.removeSkill('expertise_fs_path_flurry')


	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):

	actor.addAbility('fs_flurry_1')

	return

def removeAbilities(core, actor, player):

	actor.removeAbility('fs_flurry_1')

	return
