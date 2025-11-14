# Monitor DI Futuro - B3 📊

Aplicação Streamlit para visualização e análise de taxas DI Futuro da B3.

## 🚀 Funcionalidades

- **Visão Geral**: Gráficos comparativos entre diferentes períodos históricos
- **Análise por Período**: Detalhamento de taxas para cada período específico
- **Heatmap Comparativo**: Visualização de diferenças entre períodos
- **Dados Brutos**: Exportação e filtragem de dados

## 📋 Pré-requisitos

- Python 3.8+
- pip
- Google Chrome (para coleta de dados)

## 🔧 Instalação Local

### 1. Clone ou faça download dos arquivos

```bash
git clone git@github.com:leovnoliveira/stock-mercado-fator-quaest.git
cd stock-mercado-fator-quaest
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Colete os dados

```bash
python dados_di.py
```

Este script irá:
- Acessar o site da B3
- Coletar dados de taxas DI para diferentes períodos
- Salvar em `data/dados_di.csv`

### 5. Execute a aplicação

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador em `http://localhost:8501`

## 🌐 Deploy no Streamlit Cloud (RECOMENDADO - GRATUITO!)

### Por que Streamlit Cloud?
- ✅ **100% Gratuito**
- ✅ Deploy em 2 minutos
- ✅ HTTPS automático
- ✅ Atualizações automáticas via Git
- ✅ Não precisa configurar servidor

### Passo a Passo:

#### 1. Prepare seu repositório GitHub

```bash
# Crie um repositório no GitHub
# Faça upload dos seguintes arquivos:
- app.py
- dados_di.py
- requirements.txt
- .streamlit/config.toml (opcional)
- data/dados_di.csv (dados já coletados)
```

#### 2. Acesse Streamlit Cloud
- Vá para: https://streamlit.io/cloud
- Clique em "Sign up" com sua conta GitHub
- **É 100% GRATUITO!** 🎉

#### 3. Deploy da Aplicação
1. Clique em "New app"
2. Selecione seu repositório
3. Branch: `main` (ou `master`)
4. Main file path: `app.py`
5. Clique em "Deploy!"

#### 4. Aguarde o deploy (2-3 minutos)
Seu app estará disponível em: `https://<seu-usuario>-<nome-repo>.streamlit.app`

### ⚠️ Importante: Atualização de Dados

Como o Streamlit Cloud não executa web scraping automaticamente, você tem **duas opções**:

#### Opção A: Upload Manual (MAIS SIMPLES)
1. Execute `python dados_di.py` localmente
2. Faça commit do `data/dados_di.csv` atualizado no GitHub
3. O Streamlit Cloud detecta e atualiza automaticamente

#### Opção B: GitHub Actions (AUTOMATIZADO)
Crie `.github/workflows/update-data.yml`:

```yaml
name: Atualizar Dados DI

on:
  schedule:
    - cron: '0 10 * * 1-5'  # Segunda a sexta às 10h
  workflow_dispatch:  # Permite execução manual

jobs:
  update-data:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install Chrome
      run: |
        wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
        sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
        sudo apt-get update
        sudo apt-get install google-chrome-stable
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run scraper
      run: python dados_di.py
    
    - name: Commit and push if changed
      run: |
        git config --global user.name 'GitHub Action'
        git config --global user.email 'action@github.com'
        git add data/dados_di.csv
        git diff --quiet && git diff --staged --quiet || (git commit -m "Atualizar dados DI" && git push)
```

## 🐳 Deploy com Docker (AVANÇADO)

Use Docker se precisar de total controle ou do web scraping rodando automaticamente.

### 1. Crie o Dockerfile

```dockerfile
FROM python:3.10-slim

# Instalar Chrome e dependências
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p data

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD ["sh", "-c", "python dados_di.py && streamlit run app.py --server.port=8501 --server.address=0.0.0.0"]
```

### 2. Crie o docker-compose.yml

```yaml
version: '3.8'

services:
  streamlit:
    build: .
    container_name: di-monitor
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
    restart: unless-stopped
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### 3. Build e Execute

```bash
# Build
docker-compose build

# Executar
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar
docker-compose down
```

Acesse: `http://localhost:8501`

### Deploy Docker em Servidor (VPS)

```bash
# No servidor (Ubuntu/Debian)
git clone <seu-repo>
cd <diretorio>

# Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo apt install docker-compose

# Deploy
docker-compose up -d

# Configurar firewall (se necessário)
sudo ufw allow 8501
```

## 📊 Estrutura do Projeto

```
.
├── app.py                      # Aplicação Streamlit principal
├── dados_di.py                 # Script de coleta de dados (web scraping)
├── requirements.txt            # Dependências Python
├── .streamlit/
│   └── config.toml            # Configurações do Streamlit
├── data/
│   └── dados_di.csv           # Dados coletados (gerado)
├── Dockerfile                  # Para deploy Docker (opcional)
├── docker-compose.yml          # Para deploy Docker (opcional)
├── .github/
│   └── workflows/
│       └── update-data.yml    # GitHub Actions (opcional)
└── README.md                   # Este arquivo
```

## 🔄 Atualizando os Dados

### Localmente - Manual
```bash
python dados_di.py
```

### Localmente - Agendado

**Linux (crontab)**:
```bash
crontab -e

# Adicione (executar todo dia útil às 9h):
0 9 * * 1-5 cd /caminho/do/projeto && /caminho/do/venv/bin/python dados_di.py
```

**Windows (Task Scheduler)**:
1. Abra Task Scheduler
2. Criar Tarefa Básica
3. Nome: "Atualizar Dados DI"
4. Gatilho: Diariamente às 9:00
5. Ação: Iniciar programa
   - Programa: `C:\caminho\do\venv\Scripts\python.exe`
   - Argumentos: `dados_di.py`
   - Iniciar em: `C:\caminho\do\projeto`

**macOS (launchd)**:
Crie `~/Library/LaunchAgents/com.usuario.di-update.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.usuario.di-update</string>
    <key>ProgramArguments</key>
    <array>
        <string>/caminho/do/venv/bin/python</string>
        <string>/caminho/do/projeto/dados_di.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
</dict>
</plist>
```

Depois: `launchctl load ~/Library/LaunchAgents/com.usuario.di-update.plist`

## 🎨 Customização

### Cores e Tema

Edite `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF4B4B"              # Cor dos botões e destaques
backgroundColor = "#0E1117"           # Fundo principal
secondaryBackgroundColor = "#262730"  # Fundo dos cards
textColor = "#FAFAFA"                 # Cor do texto
font = "sans serif"                   # Fonte
```

### Adicionar mais períodos

Em `dados_di.py`, adicione em `datas_referencia`:
```python
datas_referencia = {
    'hoje': datetime.now(),
    'um_ano_atras': datetime.now() - timedelta(days=365),
    'quinze_anos_atras': datetime.now() - timedelta(days=15 * 365),  # NOVO
    # ...
}
```

## 🐛 Troubleshooting

### "No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### Erro do Chrome/ChromeDriver
```bash
pip install --upgrade webdriver-manager
```

### "Permission denied" ao executar script
```bash
chmod +x dados_di.py
```

### Streamlit não abre no navegador
```bash
streamlit run app.py --server.port 8502  # Tente outra porta
```

### Dados não aparecem no app
1. Verifique se `data/dados_di.csv` existe
2. Execute `python dados_di.py` primeiro
3. Verifique permissões da pasta `data/`

### Docker: Container não inicia
```bash
# Ver logs
docker-compose logs

# Rebuild forçado
docker-compose build --no-cache
docker-compose up -d
```

## 🚀 Comparação: Streamlit Cloud vs Docker

| Característica | Streamlit Cloud | Docker (VPS) |
|---------------|-----------------|--------------|
| **Custo** | Gratuito | $5-20/mês (VPS) |
| **Setup** | 2 minutos | 30 minutos |
| **Manutenção** | Zero | Média |
| **Escalabilidade** | Automática | Manual |
| **HTTPS** | Incluído | Precisa configurar |
| **Domínio Custom** | Possível | Sim |
| **Recursos** | Limitados | Customizáveis |
| **Ideal para** | MVP, protótipos | Produção enterprise |

**Recomendação**: Comece com Streamlit Cloud (gratuito) e migre para Docker/VPS apenas se precisar de mais controle ou recursos.

## 📈 Próximos Passos

- [ ] Adicionar autenticação de usuários
- [ ] Implementar cache Redis para dados
- [ ] Criar API REST para os dados
- [ ] Adicionar mais visualizações (candlestick, etc)
- [ ] Exportar relatórios em PDF
- [ ] Integrar com outras fontes de dados

## 📝 Licença

MIT License - use livremente!

## 👨‍💻 Autor

**Leonardo** - Quaest  
Sistema Lupa - Field Monitoring System

## 🤝 Contribuindo

Pull requests são bem-vindos! Para mudanças importantes:

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📞 Suporte

- 📧 Email: [seu-email]
- 🐛 Issues: [GitHub Issues](seu-repo/issues)
- 💬 Discussões: [GitHub Discussions](seu-repo/discussions)

---

**💡 Dica Final**: Para a melhor experiência com mínimo esforço, use o **Streamlit Cloud** - é gratuito, confiável e você faz deploy em minutos! 🚀

**Happy coding!** 🎉
