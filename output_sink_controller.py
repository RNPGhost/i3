#!/usr/bin/python3
import subprocess
import re

def get_output_sink_name():
        info = subprocess.Popen(["pactl", "info"], stdout=subprocess.PIPE).communicate()[0]
        match = re.search(b'Default Sink: ([^\n]*)', info)
        output = match.group(1)
        if b'stereo' in output:
            return "Speakers"
        else:
            return "Volume"
