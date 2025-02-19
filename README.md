# - Servidor de Impressora T�rmica via Web API

Este projeto implementa um **servidor Web API** para controlar uma **impressora t�rmica** via protocolo **ESC/POS**. Ele recebe comandos via HTTP e os encaminha para a impressora conectada � porta serial.

Reposit�rio: [github.com/marcelomaurin/srvprinter](https://github.com/marcelomaurin/srvprinter)

---

## - Instala��o

### - **Linux**
1- Clone o reposit�rio:
   ```sh
   git clone https://github.com/marcelomaurin/srvprinter.git
   cd srvprinter/src
   ```

2- Instale as depend�ncias:
   ```sh
   make install
   ```

3- Inicie o servidor:
   ```sh
   make start
   ```

4- Para executar manualmente:
   ```sh
   ./srvprinter.sh
   ```

---

### - **Windows**
1- Clone o reposit�rio:
   ```sh
   git clone https://github.com/marcelomaurin/srvprinter.git
   cd srvprinter/src
   ```

2- Instale as depend�ncias:
   ```sh
   pip install -r requirements.txt
   ```

3- Execute o servidor:
   ```sh
   srvprinter.bat
   ```

---

## - Uso da API

### - **Verificar status da impressora**
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

### - **Enviar um texto para impress�o**
```sh
curl -X POST http://localhost:8102/print      -H "Content-Type: application/json"      -d '{"command": "TEXT:Ol� Mundo!|32|center"}'
```

### - **Imprimir c�digo de barras**
```sh
curl -X POST http://localhost:8102/print      -H "Content-Type: application/json"      -d '{"command": "BARCODE:123456789012"}'
```

### - **Imprimir um QR Code**
```sh
curl -X POST http://localhost:8102/print      -H "Content-Type: application/json"      -d '{"command": "QRCODE:https://github.com"}'
```

---

## - **Protocolo de Comunica��o**

Os comandos enviados seguem o seguinte formato:

| Comando   | Descri��o |
|-----------|----------|
| `TEXT:<texto>|<colunas>|<alinhamento>` | Imprime um texto formatado |
| `BIGTXT:<texto>` | Imprime um texto grande e centralizado |
| `MICROTXT:<texto>` | Imprime um texto pequeno |
| `BARCODE:<c�digo>` | Imprime um c�digo de barras (EAN13) |
| `QRCODE:<link>` | Imprime um QR Code |
| `IMAGE:<caminho>` | Imprime uma imagem |
| `PICCUT:PARTIAL` | Corta parcialmente o papel |
| `PICCUT:FULL` | Corta completamente o papel |

---

## - **Configura��o (`serial.cfg`)**

O arquivo `serial.cfg` define os par�metros do servidor e est� localizado na **pasta `src`**:

```ini
[GENERAL]
log_file = /var/log/thermal_printer.log 
baud_rate = 9600
serial_port = /dev/ttyUSB0
host = 0.0.0.0
port = 8102
debug = True
```

---

## - **Como Parar o Servidor**
No **Linux/macOS**, pressione `CTRL + C`.  
No **Windows**, feche a janela do terminal.

---

## - **Manuten��o**
Para **limpar** o ambiente:
```sh
make clean
```

Para **atualizar as depend�ncias**:
```sh
pip install --upgrade -r requirements.txt
```

---

## -- **Cr�ditos**
- **Autor:** [Marcelo Maurin](https://github.com/marcelomaurin)
- **Licen�a:** https://maurinsoft.com.br/plano-de-negocios-customizacao-de-software-open-source/
- **GitHub:** [Reposit�rio do Projeto](https://github.com/marcelomaurin/srvprinter)

---
- **Agora voc� pode imprimir diretamente via API!** -
