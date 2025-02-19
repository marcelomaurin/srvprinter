import configparser
import os

# Obtém o diretório onde o script está localizado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "serial.cfg")

# Valores padrão
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
    """Carrega a configuração do arquivo ou cria um novo com valores padrão."""
    config = configparser.ConfigParser()
    
    # Se o arquivo existir, lê as configurações
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
    else:
        # Se não existir, cria um novo com os valores padrão
        config.read_dict(DEFAULT_CONFIG)
        save_config(config)
    
    return config

def save_config(config):
    """Salva as configurações no arquivo serial.cfg."""
    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)

def get_config_value(section, key):
    """Obtém um valor específico do arquivo de configuração."""
    config = load_config()
    return config.get(section, key, fallback=DEFAULT_CONFIG[section][key])

if __name__ == "__main__":
    # Exemplo: Carregar configurações e exibir os valores
    config = load_config()
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            print(f"{key} = {value}")
