import configparser
import os

# Obt�m o diret�rio onde o script est� localizado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "serial.cfg")

# Valores padr�o
DEFAULT_CONFIG = {
    "GENERAL": {
        "log_file": "/var/log/thermal_printer.log",
        "baud_rate": "9600",
        "serial_port": "/dev/ttyUSB0",
        "host": "0.0.0.0",
        "port": "8102", 
        "debug": "True"
    }
}

def load_config():
    """Carrega a configura��o do arquivo ou cria um novo com valores padr�o."""
    config = configparser.ConfigParser()
    
    # Se o arquivo existir, l� as configura��es
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
    else:
        # Se n�o existir, cria um novo com os valores padr�o
        config.read_dict(DEFAULT_CONFIG)
        save_config(config)
    
    return config

def save_config(config):
    """Salva as configura��es no arquivo serial.cfg."""
    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)

def get_config_value(section, key):
    """Obt�m um valor espec�fico do arquivo de configura��o."""
    config = load_config()
    return config.get(section, key, fallback=DEFAULT_CONFIG[section][key])

if __name__ == "__main__":
    # Exemplo: Carregar configura��es e exibir os valores
    config = load_config()
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            print(f"{key} = {value}")
