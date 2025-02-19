#!/bin/bash

# Obtém o diretório onde o script está localizado
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Navega até a pasta do script
cd "$DIR"

echo "Iniciando o servidor da impressora térmica..."
python3 srvprinter.py
 