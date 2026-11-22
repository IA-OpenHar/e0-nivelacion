#!/usr/bin/env bash

touch "mi pagina.html" index.html
find . -name '*.html' -print0 |xargs -0 zip paginas.zip