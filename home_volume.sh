#!/bin/bash

SOUND_DEVICE_NAME="$(~/.config/i3/output_sink_controller.py get)"
VOLUME="$(/usr/local/libexec/i3blocks/volume)"
echo -n "$SOUND_DEVICE_NAME: $VOLUME"
