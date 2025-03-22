# 🖥️ Web Scraping de Processadores Intel na Kabum

Este projeto realiza web scraping no site da **Kabum** utilizando **Selenium**, com o objetivo de extrair e listar todos os processadores **Intel** disponíveis.

---

## 🚀 Tecnologias Utilizadas

- **Python** 🐍
- **Selenium** 🌐
- **Pandas** 🗂️
- **WebDriver Manager** ⚙️

---

## ⚙️ Funcionalidades

✅ Acessa o site da Kabum  
✅ Filtra os processadores da marca Intel  
✅ Percorre todas as páginas de resultados  
✅ Extrai nome e preço dos produtos  
✅ Salva os dados em um arquivo CSV  

---

## 📦 Instalação e Uso

### 🔧 Pré-requisitos
Certifique-se de ter instalado:
- Python 3+
- Google Chrome
- ChromeDriver compatível com a versão do seu navegador

### 📥 Instalação das Dependências
```bash
pip install selenium webdriver-manager pandas
```

### ▶️ Como Executar
```bash
python scraper.py
```

---

## 📝 Exemplo de Código

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import math
import re
import pandas as pd

# Configuração do Navegador
options = Options()
options.add_argument("--lang=pt-BR")
options.add_argument("--disable-notifications")
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

driver.get("https://www.kabum.com.br/hardware/processadores/processador-intel")

# Coleta de dados e paginação...
```

---

## 📜 Licença
Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

💡 _Sinta-se à vontade para contribuir e melhorar este projeto!_ 🚀

