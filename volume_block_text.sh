#!/bin/bash

OUTPUT_SINK_CONTROLLER=~/.config/i3/output_sink_controller.py

LABEL=♪
NUMBER_OF_SINKS="$("$OUTPUT_SINK_CONTROLLER" number_available)"
if [[ "$NUMBER_OF_SINKS" != 1 ]]; then
  SOUND_DEVICE_NAME="$("$OUTPUT_SINK_CONTROLLER" get)"
  if [[ "$SOUND_DEVICE_NAME" != None ]]; then
    LABEL="$SOUND_DEVICE_NAME"
  fi
fi

VOLUME="$(/usr/local/libexec/i3blocks/volume)"
if [[ "$VOLUME" == MUTE ]]; then
    VOLUME="<span color='red'>Muted</span>"
elif [[ "$VOLUME" == 0% ]]; then
    VOLUME="<span color='red'>$VOLUME</span>"
fi

echo "$LABEL: $VOLUME"
