import sys, os, time, json
settingsJson = json.load(open("settings.json"))
store_dir = settingsJson["store_directory"]
working_dir = settingsJson["working_directory"]

#Event Handlers
def changeDirectory(command):
	#Command Format
	#cwd {directory}
	parsed_command = parseCommand(command)

def putInDropboxFolder(command):
	return

#Functions
def parseCommand(command):
	return command.split(" ")

#Uses the key to find the event handler
commands_dict = {}

while True:
	command = input("ev3-version-control>>> ")
	if command == "stop" or command == "quit" or command == "exit":
		sys.exit()