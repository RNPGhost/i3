#!/usr/bin/python3
import sys
import subprocess
import json

MAX_WORKSPACES_PER_MONITOR = 10
NAME_SEPERATOR = '-'

def create_default_workspaces():
  for i in range(get_workspaces().__len__(), 0, -1):
    subprocess.Popen(["i3-msg", "workspace " + str(i)])
    newWorkspaceName = get_default_workspace_name(i)
    subprocess.Popen(["i3-msg", "workspace " + newWorkspaceName])

def focus_workspace(workspaceNumber):
  targetWorkspaceName = get_target_workspace_name(workspaceNumber)
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

if len(sys.argv) < 2:
  print("Error: Not enough arguments")
else:
  command = sys.argv[1]
  if command == 'startup':
    if get_workspaces().__len__() > 1:
      create_default_workspaces()
  elif command == 'focus':
    if len(sys.argv) > 2:
      workspaceNumber = sys.argv[2]
      focus_workspace(workspaceNumber)
  else:
    print("Error: Command '" + command + "' not recognised")
