#!/usr/bin/python3

from flask import Flask, request, jsonify
from escpos.printer import Serial
from PIL import Image
import logging
from config_manager import get_config_value

# Carrega configurações do serial.cfg
log_file = get_config_value("GENERAL", "log_file")
baud_rate = int(get_config_value("GENERAL", "baud_rate"))
serial_port = get_config_value("GENERAL", "serial_port")
host = get_config_value("GENERAL", "host")
port = int(get_config_value("GENERAL", "port"))
debug = get_config_value("GENERAL", "debug").lower() == "true"

# Configuração do log
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Inicializa a impressora
try:
    printer = Serial(serial_port, baudrate=baud_rate, timeout=1)
except Exception as e:
    printer = None
    logging.error(f'Erro ao inicializar a impressora: {e}')

# Configuração do Flask
app = Flask(__name__)

# Função para ajustar texto ao número de colunas
def format_text(text, columns, align='left'):
    if align == 'left':
        return text.ljust(columns)[:columns]
    elif align == 'center':
        return text.center(columns)[:columns]
    elif align == 'right':
        return text.rjust(columns)[:columns]
    return text.ljust(columns)[:columns]

# Função para processar os comandos ESC/POS
def process_command(command):
    if not printer:
        return {'status': 'error', 'message': 'Impressora não inicializada'}
    
    try:
        if command.startswith("TEXT:"):
            parts = command[len("TEXT:"):].strip().split("|")
            text = parts[0].strip()
            columns = int(parts[1]) if len(parts) > 1 else 32
            align = parts[2].strip() if len(parts) > 2 else 'left'
            formatted_text = format_text(text, columns, align)
            printer.set(align='left')
            printer.text(formatted_text + "\n")

        elif command.startswith("BIGTXT:"):
            text = command[len("BIGTXT:"):].strip()
            printer.set(text_type='B', align='center', width=2, height=2)
            printer.text(text + "\n")

        elif command.startswith("MICROTXT:"):
            text = command[len("MICROTXT:"):].strip()
            printer.set(text_type='NORMAL', align='left', width=1, height=1)
            printer.text(text + "\n")

        elif command.startswith("BARCODE:"):
            barcode = command[len("BARCODE:"):].strip()
            printer.barcode(barcode, 'EAN13', function_type='B')

        elif command.startswith("QRCODE:"):
            qrcode = command[len("QRCODE:"):].strip()
            printer.qr(qrcode)

        elif command.startswith("IMAGE:"):
            image_path = command[len("IMAGE:"):].strip()
            img = Image.open(image_path)
            printer.image(img)

        elif command.startswith("PICCUT:"):
            cut_type = command[len("PICCUT:"):].strip().upper()
            if cut_type == "PARTIAL":
                printer.cut(mode='PART')
            elif cut_type == "FULL": 
                printer.cut(mode='FULL')
            else:
                logging.warning(f"Tipo de corte inválido: {cut_type}")

        else:
            logging.warning(f"Comando não reconhecido: {command}")
            return {'status': 'error', 'message': f'Comando não reconhecido: {command}'}
        
        printer.set()  # Reseta configurações após cada comando
        logging.info(f'Comando processado: {command}')
        return {'status': 'success', 'message': f'Comando executado: {command}'}
    
    except Exception as e:
        logging.error(f'Erro ao processar comando: {command} - {e}')
        return {'status': 'error', 'message': str(e)}

# Rota para receber comandos via Web API
@app.route('/print', methods=['POST'])
def print_text():
    try:
        data = request.json
        if 'command' not in data:
            return jsonify({'status': 'error', 'message': 'Comando não especificado'}), 400
        
        command = data['command']
        response = process_command(command)
        return jsonify(response)
    
    except Exception as e:
        logging.error(f'Erro na API: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Rota para testar conexão com a impressora
@app.route('/status', methods=['GET'])
def check_status():
    return jsonify({'status': 'ok', 'printer_connected': printer is not None})

# Inicializa o servidor Flask na porta configurada
if __name__ == '__main__':
    app.run(host=host, port=port, debug=debug)
