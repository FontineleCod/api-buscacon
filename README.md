# 🔍 API Buscacon

Uma API em Python com web scraping utilizando Selenium, criada para buscar concursos públicos disponíveis por estado no site [PCI Concursos](https://www.pciconcursos.com.br/).

---

Funcionalidades

- Consulta concursos por estado (ex: PA, SP, RN)
- Coleta de:
  - Nome do concurso
  - Detalhes (data, cargo, salário, escolaridade, vagas)
- Visual moderno no terminal (cores e organização)

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- WebDriver Chrome
- Git

---

Como executar localmente

1. Clone o repositório

```bash
git clone https://github.com/FontineleCod/api-buscacon.git
cd api-buscacon
```

2. Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Para Windows
```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

4. Execute a aplicação

```bash
python main.py
```

---

Organização do Projeto

```
api-buscacon/
│
├── scraper.py        # Script de scraping com Selenium
├── main.py           # Executável principal da API
├── requirements.txt  # Bibliotecas necessárias
└── README.md         # Este arquivo
```

---

Autor

Desenvolvido com 💻 e ☕ por [Marcelo Fontinele](https://github.com/FontineleCod)

---

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
```
