import sys, os, time, json

settings = json.load(open("settings.json"))

#Event Handlers
def changeWorkingDirectory(command):
	#Command Format
	#cwd {directory}
	parsed_command = parseCommand(command)
	if len(parsed_command >= 2):
		settings["working_directory"] = command[1]
	else:
		print("There are not enough arguments.")

def putFileInDropboxFolder(command):
	return

def pullFileFromDropboxFolder(command):
	return

def commitChanges(command):
	return

def addChanges(command):
	return

def removeChanges(command):
	return

def revertToPreviousCommit(command):
	return

#Functions
def parseCommand(command):
	return command.split(" ")

def exitProgram():
	json.dump(settings, open("settings.json", "w"), indent=4)
	sys.exit()

#Uses the key to find the event handler
commands_dict = {"cwd": changeWorkingDirectory, "commit": commitChanges, 
				 "add": addChanges, "remove": removeChanges, "revert": revertToPreviousCommit, 
				 "pull": pullFileFromDropboxFolder, "push": putFileInDropboxFolder}

#Main command loop
while True:
	command = input("ev3-version-control>>> ")
	if command == "stop" or command == "quit" or command == "exit":
		exitProgram()
	for entry in commands_dict:
		if entry == command:
			commands_dict[entry](command)