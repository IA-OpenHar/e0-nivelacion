#!/usr/bin/env bash

rm -f salida.log errores.log
contador=0

while true; do
    contador=$((contador + 1))
    ./fallo.sh >> salida.log 2>> errores.log
    if [[ $? -ne 0 ]]; then
        break
    fi
done

cat salida.log errores.log
echo "Fallo en la ejecucion numero $contador"
