import sys, os, time, json

settings = json.load(open("settings.json"))

#Event Handlers
def changeWorkingDirectory(command):
	#Command Format
	#cwd {directory}
	parsed_command = parseCommand(command)
	settings["working_directory"] = command[1]

def putFileInDropboxFolder(command):
	return

#Functions
def parseCommand(command):
	return command.split(" ")

def exitProgram():
	json.dump(settings, open("settings.json", "w"))
	sys.exit()

#Uses the key to find the event handler
commands_dict = {"cwd": changeDirectory}

while True:
	command = input("ev3-version-control>>> ")
	if command == "stop" or command == "quit" or command == "exit":
		exitProgram()
	for entry in commands_dict:
		if entry == command:
			commands_dict[entry](command)