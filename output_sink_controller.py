#!/usr/bin/python3
import sys
import subprocess
import re

sink_names = {'Speakers':'alsa_output.pci-0000_00_1b.0.iec958-stereo'}

def get_output_sink_name():
    info = subprocess.Popen(["pactl", "info"], stdout=subprocess.PIPE).communicate()[0]
    match = re.search(b'Default Sink: ([^\n]*)', info)
    output = match.group(1)
    if b'stereo' in output:
        return "Speakers"
    else:
        return None

def set_output_sink(output_name):
    if output_name in sink_names:
        subprocess.Popen(["pactl", "set-default-sink", sink_names[output_name]])
        return True
    else:
        print("Error: The output sink name '" + output_name + "' was not found")
        return False

def enough_arguments(requiredNumberOfArguments):
  enoughArguments = (len(sys.argv) >= requiredNumberOfArguments)
  if not enoughArguments:
    print("Error: Not enough arguments provided")
  return enoughArguments

if len(sys.argv) >= 2:
    command = sys.argv[1]
    if command == 'get':
        sys.stdout.write(get_output_sink_name())
    elif command == 'set':
        if enough_arguments(3):
            output_name = sys.argv[2]
            sys.stdout.write(set_output_sink(output_name))
    else:
        print("Error: Command " + command + " not recognised")
