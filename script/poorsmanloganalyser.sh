#!/bin/bash

LOG_FILE="/home/pi/kalliope_config/kalliope.log"

nb_trigger=$(cat "$LOG_FILE" | grep "Say something!" | wc -l)
nb_match=$(cat "$LOG_FILE" | grep "Order matched in the brain" | wc -l)
nb_audio_issue=$(cat "$LOG_FILE" | grep "Google Speech Recognition could not understand audio" | wc -l)
nb_no_synapse=$(cat "$LOG_FILE" | grep "No synapse match the captured order" | wc -l)

audio="Aussi loin que je me souvienne, j'ai reçu $nb_trigger ordres vocaux. Je n'ai pas compris $nb_no_synapse ordres et eu $nb_audio_issue problème audio"

echo "$audio"
