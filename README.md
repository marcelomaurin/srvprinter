# 🖨️ Servidor de Impressora Térmica via Web API

Este projeto implementa um **servidor Web API** para controlar uma **impressora térmica** via protocolo **ESC/POS**. Ele recebe comandos via HTTP e os encaminha para a impressora conectada à porta serial.

Repositório: [github.com/marcelomaurin/srvprinter](https://github.com/marcelomaurin/srvprinter)

---

## 📥 Instalação

### 🐧 **Linux**
1️⃣ Clone o repositório:
   ```sh
   git clone https://github.com/marcelomaurin/srvprinter.git
   cd srvprinter/src
   ```

2️⃣ Instale as dependências:
   ```sh
   make install
   ```

3️⃣ Inicie o servidor:
   ```sh
   make start
   ```

4️⃣ Para executar manualmente:
   ```sh
   ./srvprinter.sh
   ```

---

### 🖥️ **Windows**
1️⃣ Clone o repositório:
   ```sh
   git clone https://github.com/marcelomaurin/srvprinter.git
   cd srvprinter/src
   ```

2️⃣ Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

3️⃣ Execute o servidor:
   ```sh
   srvprinter.bat
   ```

---

## 📡 Uso da API

### 🔹 **Verificar status da impressora**
```sh
curl http://localhost:8102/status
```
**Resposta esperada (JSON)**:
```json
{
  "status": "ok",
  "printer_connected": true
}
```

### 🔹 **Enviar um texto para impressão**
```sh
curl -X POST http://localhost:8102/print      -H "Content-Type: application/json"      -d '{"command": "TEXT:Olá Mundo!|32|center"}'
```

### 🔹 **Imprimir código de barras**
```sh
curl -X POST http://localhost:8102/print      -H "Content-Type: application/json"      -d '{"command": "BARCODE:123456789012"}'
```

### 🔹 **Imprimir um QR Code**
```sh
curl -X POST http://localhost:8102/print      -H "Content-Type: application/json"      -d '{"command": "QRCODE:https://github.com"}'
```

---

## 🔄 **Protocolo de Comunicação**

Os comandos enviados seguem o seguinte formato:

| Comando   | Descrição |
|-----------|----------|
| `TEXT:<texto>|<colunas>|<alinhamento>` | Imprime um texto formatado |
| `BIGTXT:<texto>` | Imprime um texto grande e centralizado |
| `MICROTXT:<texto>` | Imprime um texto pequeno |
| `BARCODE:<código>` | Imprime um código de barras (EAN13) |
| `QRCODE:<link>` | Imprime um QR Code |
| `IMAGE:<caminho>` | Imprime uma imagem |
| `PICCUT:PARTIAL` | Corta parcialmente o papel |
| `PICCUT:FULL` | Corta completamente o papel |

---

## ⚙️ **Configuração (`serial.cfg`)**

O arquivo `serial.cfg` define os parâmetros do servidor e está localizado na **pasta `src`**.

Agora, o sistema reconhece automaticamente se está sendo executado no **Linux** ou **Windows**, ajustando as configurações corretamente.

### 🐧 **Configuração Padrão no Linux**
```ini
[GENERAL]
log_file = /var/log/thermal_printer.log
baud_rate = 9600
serial_port = /dev/ttyUSB0
host = 0.0.0.0
port = 8102
debug = True
```

### 🖥️ **Configuração Padrão no Windows**
```ini
[GENERAL]
log_file = C:\srvprinter\logs\thermal_printer.log
baud_rate = 9600
serial_port = COM3
host = 0.0.0.0
port = 8102
debug = True
```

Se necessário, você pode editar manualmente esses valores no arquivo `serial.cfg`.

---

## 🛑 **Como Parar o Servidor**
No **Linux/macOS**, pressione `CTRL + C`.  
No **Windows**, feche a janela do terminal.

---

## 🛠️ **Manutenção**
Para **limpar** o ambiente:
```sh
make clean
```

Para **atualizar as dependências**:
```sh
pip install --upgrade -r requirements.txt
```

---

## 👨‍💻 **Créditos**
- **Autor:** [Marcelo Maurin](https://github.com/marcelomaurin)
- **Licença:** https://maurinsoft.com.br/plano-de-negocios-customizacao-de-software-open-source/
- **GitHub:** [Repositório do Projeto](https://github.com/marcelomaurin/srvprinter)

---
🚀 **Agora você pode imprimir diretamente via API!** 🚀
