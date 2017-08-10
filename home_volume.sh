#!/bin/bash

SOUND_DEVICE_NAME="$(~/.config/i3/output_sink_controller.py get)"
VOLUME="$(/usr/local/libexec/i3blocks/volume)"
if [ $VOLUME = "MUTE" ]; then
    VOLUME="<span color='red'>Muted</span>"
elif [ $VOLUME = "0%" ]; then
    VOLUME="<span color='red'>$VOLUME</span>"
fi
echo "$SOUND_DEVICE_NAME: $VOLUME"
