# Definições
PYTHON = python3
VENV = venv
ACTIVATE = source $(VENV)/bin/activate
REQ_FILE = requirements.txt
SCRIPT = srvprinter.py

# Criação do ambiente virtual 
.PHONY: venv
venv:
	@echo "Criando ambiente virtual..."
	@$(PYTHON) -m venv $(VENV)
	@echo "Ativando ambiente virtual..."
	@$(ACTIVATE) && pip install --upgrade pip
	@echo "Instalando dependências..."
	@$(ACTIVATE) && pip install -r $(REQ_FILE)

# Rodar o servidor
.PHONY: run
run:
	@echo "Executando o servidor..."
	@$(ACTIVATE) && $(PYTHON) $(SCRIPT)

# Limpeza do projeto
.PHONY: clean
clean:
	@echo "Removendo arquivos temporários..."
	@rm -rf $(VENV)
	@rm -f *.log
	@rm -f serial.cfg

# Instalação e execução
.PHONY: install
install: venv

.PHONY: start
start: install run
