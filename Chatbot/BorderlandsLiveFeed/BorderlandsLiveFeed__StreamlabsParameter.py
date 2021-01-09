import os
import re
import codecs
import json


ScriptName = "Borderlands Live Feed"
Website = "https://github.com/mopioid/Borderlands-LiveFeed"
Description = "Accesses character data in BL2 & TPS provided by Borderlands Live Feed."
Creator = "mopioid"
Version = "2.0"


def Log(content):
	try:
		Parent.Log(ScriptName, str(content))
	except NameError:
		print(content)


Characters = {
	"Gunzerker":    "a Gunzerker",
	"Commando":     "a Commando",
	"Assassin":     "an Assassin",
	"Siren":        "a Siren",
	"Mechromancer": "a Mechromancer",
	"Psycho":       "a Psycho",
	"Fragtrap":     "a Fragtrap",
	"Enforcer":     "an Enforcer",
	"Gladiator":    "a Gladiator",
	"Lawbringer":   "a Lawbringer",
	"Baroness":     "a Baroness",
	"Doppel":       "a Doppelganger"
}

def GetName(output):
	character = None
	characterClass = output.get('class')
	if type(characterClass) is str:
		character = Characters.get(characterClass)

	name = output.get('name')
	if type(name) is not str or name == "" or character is None:
		return None

	return "%s named '%s'" % (character, name)

def GetSkin(output):
	customizations = []

	head = output.get('head')
	if type(head) is str:
		customizations.append("'%s' head" % head)

	skin = output.get('skin')
	if type(skin) is str:
		customizations.append("'%s' skin" % skin)

	customizationCount = len(customizations)
	if customizationCount == 0:
		return None
	if customizationCount == 1:
		return customizations[0]
	if customizationCount == 2:
		return customizations[0] + " with the " + customizations[1]

SkillURLs = {
	"Gunzerker":    "http://bl2skills.com/gunzerker.html#",
	"Commando":     "http://bl2skills.com/commando.html#",
	"Assassin":     "http://bl2skills.com/assassin.html#",
	"Siren":        "http://bl2skills.com/siren.html#",
	"Mechromancer": "http://bl2skills.com/mechromancer.html#",
	"Psycho":       "http://bl2skills.com/psycho.html#",
	"Fragtrap":     "http://thepresequel.com/Claptrap/",
	"Enforcer":     "http://thepresequel.com/Wilhelm/",
	"Gladiator":    "http://thepresequel.com/Athena/",
	"Lawbringer":   "http://thepresequel.com/Nisha/",
	"Baroness":     "http://thepresequel.com/Aurelia/",
	"Doppel":       "http://thepresequel.com/Jack/"
}

def GetBuild(output):
	character = output.get('class')
	if type(character) is not str:
		return None

	skillURL = SkillURLs.get(character)
	if type(skillURL) is not str:
		return None

	skills = output.get('skills')
	if type(skills) is not list or len(skills) == 0:
		return None

	return skillURL + "".join(str(skill) for skill in skills)

Playthroughs = ["Normal Mode", "TVHM", "UVHM"]

def GetLevel(output):
	level = output.get('level')
	if type(level) is not int or level < 1:
		return None

	playthrough = output.get('playthrough')
	if type(playthrough) is not int or playthrough < 0:
		return None

	result = "level " + str(level)

	OPLevel = output.get('OPLevel')
	if type(OPLevel) is not int or OPLevel < 0:
		OPLevel = 0

	if OPLevel > 0:
		result += ", OP " + str(OPLevel)
	else:
		result += " in " + Playthroughs[playthrough]

	currentPlaythrough = output.get('currentPlaythrough')
	if type(currentPlaythrough) is not int or currentPlaythrough < 0:
		currentPlaythrough = playthrough

	if currentPlaythrough != playthrough:
		result += ", currently playing in " + Playthroughs[currentPlaythrough]
	elif playthrough == 2:
		currentOPLevel = output.get('currentOPLevel')
		if type(currentOPLevel) is not int or currentOPLevel < 0:
			currentOPLevel = OPLevel
	
		if currentOPLevel != OPLevel:
			result += ", currently playing at OP " + str(currentOPLevel)
		elif level == 80 and OPLevel < 10 and output.get('map') == "TestingZone_P":
			result += ", going for OP " + str(currentOPLevel + 1)

	return result

def GetWeapons(output):
	weapons = output.get('weapons')
	if type(weapons) is not list:
		return None
	weapons = list(filter(lambda weapon: type(weapon) is str, output['weapons']))

	weaponCount = len(weapons)
	if weaponCount == 0:
		return "None"
	if weaponCount == 1:
		return "'%s'" % weapons[0]
	if weaponCount == 2:
		return "'%s' and '%s'" % (weapons[0], weapons[1])
	if weaponCount == 3:
		return "'%s', '%s', and '%s'" % (weapons[0], weapons[1], weapons[2])
	if weaponCount == 4:
		return "'%s', '%s', '%s', and '%s'" % (weapons[0], weapons[1], weapons[2], weapons[3])

def GetGear(output):
	gear = []

	shield = output.get('shield')
	if type(shield) is str:
		if shield.endswith(" Shield"):
			shield = shield[:-7]
		gear = ["'%s' shield" % shield]

	grenade = output.get('grenade')
	if type(grenade) is str:
		gear.append("'%s' grenade mod" % grenade)

	classMod = output.get('classMod')
	if type(classMod) is str:
		if classMod.endswith(" Class Mod"):
			classMod = classMod[:-10]
		gear.append("'%s' class mod" % classMod)

	relic = output.get('relic')
	if type(relic) is str:
		if relic.endswith(" Relic"):
			relic = relic[:-6]
		gear.append("'%s' relic" % relic)

	gearCount = len(gear)
	if gearCount == 0:
		return "None"
	if gearCount == 1:
		return gear[0]
	if gearCount == 2:
		return gear[0] + " and " + gear[1]
	if gearCount == 3:
		return "%s, %s, and %s" % (gear[0], gear[1], gear[2])
	if gearCount == 4:
		return "%s, %s, %s, and %s" % (gear[0], gear[1], gear[2], gear[3])


Parameters = {
	'name': GetName,
	'skin': GetSkin,
	'build': GetBuild,
	'level': GetLevel,
	'weapons': GetWeapons,
	'gear': GetGear,
}

OutputPath = os.path.expandvars("%APPDATA%\\BorderlandsLiveFeed\\Output.json")

def Init():
	parameters = list(Parameters.keys())

	# Compile a regular expression we will use to determine whether any of our
	# parameters exist in a string.
	global ParametersPattern
	ParametersPattern = re.compile("\\$bl(" + "|".join(parameters) + ")", re.IGNORECASE)

	# Create a dictionary of compiled regular expressions for each of our
	# parameters, each one keyed by the parameter itself.
	global ParameterPatterns
	ParameterPatterns = {}
	for parameter in parameters:
		ParameterPatterns[parameter] = re.compile("\\$bl" + parameter, re.IGNORECASE)

def Parse(string, user, target, message):
	# Attempt to find one of our parameters in the string.
	parameterMatch = ParametersPattern.search(string)
	# If the string does not contain one of our parameters, return it as-is.
	if parameterMatch == None:
		return string

	with codecs.open(OutputPath, encoding='utf-8-sig', mode='r') as outputFile:
		output = json.load(outputFile, encoding='utf-8-sig')

	# Our parameter is captured in the first group of the pattern.
	parameter = parameterMatch.group(1)

	result = Parameters[parameter](output)
	if result is None:
		result = "unknown, try again later"
	
	# Retrieve the regular expression for the specific parameter.
	parameterPattern = ParameterPatterns[parameter]
	# Use the expression to replace the parameter with the 
	return parameterPattern.sub(result, string)


with codecs.open(OutputPath, encoding='utf-8-sig', mode='r') as outputFile:
	output = json.load(outputFile, encoding='utf-8-sig')
for parameter in Parameters:
	Log(parameter + ": " + Parameters[parameter](output))
