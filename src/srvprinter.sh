#!/bin/bash

# Obt�m o diret�rio onde o script est� localizado
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Navega at� a pasta do script
cd "$DIR"

echo "Iniciando o servidor da impressora t�rmica..."
python3 srvprinter.py
 