#!/usr/bin/python3
import sys
import subprocess
import json

NAME_SEPERATOR = '-'

def create_default_workspaces():
  for i in range(get_workspaces().__len__(), 0, -1):
    subprocess.Popen(["i3-msg", "workspace " + str(i)])
    newWorkspaceName = get_default_workspace_name(i)
    subprocess.Popen(["i3-msg", "workspace " + newWorkspaceName])

def focus_workspace(workspaceNumber):
  targetWorkspaceName = get_target_workspace_name(workspaceNumber)
  subprocess.Popen(["i3-msg", "workspace " + targetWorkspaceName])

def move_to_workspace(workspaceNumber, focus):
  targetWorkspaceName = get_target_workspace_name(workspaceNumber)
  subprocess.Popen(["i3-msg", "move to workspace " + targetWorkspaceName])
  if focus:
    subprocess.Popen(["i3-msg", "workspace " + targetWorkspaceName])

def get_workspaces():
  handle = subprocess.Popen(["i3-msg", "-t", "get_workspaces"], stdout=subprocess.PIPE)
  output = handle.communicate()[0]
  data = json.loads(output.decode())
  data = sorted(data, key=lambda k: k['name'])
  arr = []
  for i in data:
    arr.append(i['name'])
  return arr

def get_default_workspace_name(monitorNumber):
  return (chr(64 + monitorNumber) + NAME_SEPERATOR + "1")

def get_target_workspace_name(workspaceNumber):
  return get_focused_workspace().split(NAME_SEPERATOR)[0] + NAME_SEPERATOR + str(workspaceNumber)

def get_focused_workspace():
  handle = subprocess.Popen(["i3-msg","-t","get_workspaces"], stdout=subprocess.PIPE)
  output = handle.communicate()[0]
  data = json.loads(output.decode())
  data = sorted(data, key=lambda k: k['name'])
  for i in data:
    if(i['focused']):
      return i['name']

def enough_arguments(requiredNumberOfArguments):
  enoughArguments = (len(sys.argv) >= requiredNumberOfArguments)
  if not enoughArguments:
    print("Error: Not enough arguments provided")
  return enoughArguments

if enough_arguments(2):
  command = sys.argv[1]
  if command == 'start_up':
    if get_workspaces().__len__() > 1:
      create_default_workspaces()
  elif command == 'focus':
    if enough_arguments(3):
      workspaceNumber = sys.argv[2]
      focus_workspace(workspaceNumber)
  elif command == 'move':
    if enough_arguments(3):
      workspaceNumber = sys.argv[2]
      move_to_workspace(workspaceNumber, False)
  elif command == 'move_and_focus':
    if enough_arguments(3):
      workspaceNumber = sys.argv[2]
      move_to_workspace(workspaceNumber, True)
  else:
    print("Error: Command '" + command + "' not recognised")
