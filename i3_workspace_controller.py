#!/usr/bin/python3
import sys
import subprocess
import json

NAME_SEPERATOR = '-'

def create_default_workspaces():
    subprocess.Popen(["i3-msg", "workspace", "1"])
    for i in range(len(get_workspaces()), 0, -1):
        subprocess.Popen(["i3-msg", "rename workspace " + str(i) + " to " + get_default_workspace_name(i)])
    subprocess.Popen(["i3-msg", "workspace " + get_default_workspace_name(1)])

def move_to_workspace(targetWorkspace, moveContainer=False, focus=False):
    targetWorkspaceNumber = targetWorkspace
    if targetWorkspace == 'next':
        targetWorkspaceNumber = get_current_workspace_number() + 1
    elif targetWorkspace == 'prev':
        targetWorkspaceNumber = get_current_workspace_number() - 1
        if targetWorkspaceNumber == 0:
            return
    
    targetWorkspaceName = get_target_workspace_name(targetWorkspaceNumber)
    if moveContainer:
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
    return (get_sorting_prefix(1) + chr(64 + monitorNumber) + NAME_SEPERATOR + "1")

def get_target_workspace_name(workspaceNumber):
    sortingPrefix = get_sorting_prefix(workspaceNumber)
    monitorPrefix = get_current_monitor_prefix()
    return sortingPrefix + monitorPrefix + NAME_SEPERATOR + str(workspaceNumber)

def get_sorting_prefix(workspaceNumber):
    return str(workspaceNumber) + ':'

def get_current_monitor_prefix():
    return get_focused_workspace_name().split(':')[1].split(NAME_SEPERATOR)[0]

def get_focused_workspace_name():
    return get_focused_workspace()['name']

def get_focused_workspace():
    handle = subprocess.Popen(["i3-msg","-t","get_workspaces"], stdout=subprocess.PIPE)
    output = handle.communicate()[0]
    data = json.loads(output.decode())
    data = sorted(data, key=lambda k: k['name'])
    for i in data:
        if(i['focused']):
            return i

def get_current_workspace_number():
    return get_workspace_number(get_focused_workspace_name())

def get_workspace_number(workspaceName):
    return int(workspaceName.split(NAME_SEPERATOR)[1])

def enough_arguments(requiredNumberOfArguments):
    enoughArguments = (len(sys.argv) >= requiredNumberOfArguments)
    if not enoughArguments:
        print("Error: Not enough arguments provided")
    return enoughArguments

if enough_arguments(2):
    command = sys.argv[1]
    if command == 'start_up':
        if len(get_workspaces()) > 1:
            create_default_workspaces()
    elif command == 'focus':
        if enough_arguments(3):
            workspace = sys.argv[2]
            move_to_workspace(workspace, focus=True)
    elif command == 'move':
        if enough_arguments(3):
            workspace = sys.argv[2]
            move_to_workspace(workspace, moveContainer=True)
    elif command == 'move_and_focus':
        if enough_arguments(3):
            workspace = sys.argv[2]
            move_to_workspace(workspace, moveContainer=True, focus=True)
    else:
        print("Error: Command '" + command + "' not recognised")
