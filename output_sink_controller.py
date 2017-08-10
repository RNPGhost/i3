#!/usr/bin/python3
import sys
import subprocess
import re

readable_name_to_sink_name = {'Speakers':'alsa_output.pci-0000_00_1b.0.iec958-stereo'}
sink_name_to_readable_name = {'alsa_output.pci-0000_00_1b.0.iec958-stereo':'Speakers'}

def get_output_sink_name():
    info = subprocess.Popen(["pactl", "info"], stdout=subprocess.PIPE).communicate()[0]
    match = re.search(b'Default Sink: ([^\n]*)', info)
    sink_name = match.group(1).decode("utf-8")
    if sink_name in sink_name_to_readable_name:
        return sink_name_to_readable_name[sink_name]
    else:
        return None

def set_output_sink(output_name):
    if output_name in readable_name_to_sink_name:
        subprocess.Popen(["pactl", "set-default-sink", readable_name_to_sink_name[output_name]])
        return True
    else:
        print("Error: The output sink name '" + output_name + "' was not found")
        return False

def number_of_output_sinks():
    sinks_list = subprocess.Popen(["pacmd", "list-sinks"], stdout=subprocess.PIPE).communicate()[0]
    match = re.search(b'([0-9]*) sink\(s\) available', sinks_list)
    return match.group(1).decode("utf-8")

def enough_arguments(required_number_of_arguments):
  enoughArguments = (len(sys.argv) >= required_number_of_arguments)
  if not enoughArguments:
    print("Error: Not enough arguments provided")
  return enoughArguments

if len(sys.argv) >= 2:
    command = sys.argv[1]
    if command == 'get':
        print(get_output_sink_name())
    elif command == 'set':
        if enough_arguments(3):
            output_name = sys.argv[2]
            print(set_output_sink(output_name))
    elif command == 'number_available':
        print(number_of_output_sinks())
    else:
        print("Error: Command " + command + " not recognised")
