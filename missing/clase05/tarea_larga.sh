#!/bin/bash
# Simula un trabajo largo (como la tarea de un agente) para practicar
# jobs, fg, bg y tmux. Uso: bash tarea_larga.sh 30
n=${1:-30}
for i in $(seq 1 "$n"); do
  echo "paso $i de $n"
  sleep 1
done
echo "terminado"
