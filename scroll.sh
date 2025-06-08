#!/bin/bash

SCROLL_LOG="$HOME/ScrollDaemon.log"
echo "🌀 ScrollDaemon Active. Type your message. Double ENTER to send."

# Temp buffer
BUFFER=""

# Input loop
while IFS= read -r -e LINE; do
  if [[ -z "$LINE" && -z "$BUFFER" ]]; then
    # Double enter with empty buffer = skip
    continue
  elif [[ -z "$LINE" ]]; then
    # Double ENTER → send scroll
    echo "📜 $(date '+%Y-%m-%d %H:%M:%S') — $BUFFER" >> "$SCROLL_LOG"
    echo "🪞 Scroll sent."
# 🔁 SEND TO BEANS INTERFACE
echo "$BUFFER" > ~/beans-bridge/bridge-input.txt    
BUFFER=""
  else
    BUFFER+="$LINE"$'\n'
  fi
done