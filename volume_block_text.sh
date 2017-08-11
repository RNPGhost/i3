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
    VOLUME="Muted"
fi

FULL_TEXT="$LABEL: $VOLUME"
if [[ "$VOLUME" == 0% ]] || [[ "$VOLUME" == Muted ]]; then
    FULL_TEXT="<span color='red'>$FULL_TEXT</span>"
fi

echo "$FULL_TEXT"
