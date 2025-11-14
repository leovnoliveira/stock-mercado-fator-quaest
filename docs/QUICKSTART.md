# 🚀 Guia Rápido - Monitor DI Futuro

## Opção 1: Teste Local (5 minutos) ⚡

```bash
# 1. Instalar dependências
pip install streamlit pandas plotly selenium webdriver-manager

# 2. Coletar dados
python dados_di.py

# 3. Executar app
streamlit run app.py
```

Abra: http://localhost:8501

---

## Opção 2: Deploy Streamlit Cloud (GRATUITO!) 🎉

### Passos:

1. **Faça upload no GitHub**
   - Crie um repositório
   - Adicione: `app.py`, `dados_di.py`, `requirements.txt`, pasta `data/`

2. **Deploy no Streamlit**
   - Acesse: https://streamlit.io/cloud
   - Login com GitHub
   - Clique "New app"
   - Selecione seu repo → Deploy!

3. **Pronto!** 🎊
   - URL: `https://seu-usuario-repo.streamlit.app`

### Importante:
- Execute `python dados_di.py` localmente antes
- Faça commit do arquivo `data/dados_di.csv`
- O Streamlit Cloud não executa web scraping automaticamente

---

## Opção 3: Docker (Avançado) 🐳

```bash
# Build e executar
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar
docker-compose down
```

Acesse: http://localhost:8501

---

## Atualizar Dados

### Manual
```bash
python dados_di.py
```

### Automático (GitHub Actions)
- Configure o workflow em `.github/workflows/update-data.yml`
- Roda automaticamente seg-sex às 10h

---

## Troubleshooting

**App não abre?**
```bash
streamlit run app.py --server.port 8502
```

**Sem dados?**
```bash
# Verifique se o arquivo existe
ls data/dados_di.csv

# Execute a coleta
python dados_di.py
```

**Erro do Chrome?**
```bash
pip install --upgrade webdriver-manager
```

---

## 📁 Estrutura Mínima

```
seu-projeto/
├── app.py              # App Streamlit ✅
├── dados_di.py         # Coleta dados ✅
├── requirements.txt    # Dependências ✅
└── data/
    └── dados_di.csv   # Dados (gerado)
```

---

## 🎯 Recomendação

**Para começar**: Use **Streamlit Cloud**
- ✅ Gratuito
- ✅ Simples
- ✅ Rápido

**Para produção**: Use **Docker + VPS**
- ✅ Controle total
- ✅ Automação
- ✅ Escalável

---

## 📚 Mais Informações

Veja o [README.md](README.md) completo para:
- Instruções detalhadas
- Configurações avançadas
- Customização
- Troubleshooting completo

---

**Dúvidas?** Abra uma [issue](seu-repo/issues)!

**Boa sorte!** 🚀
