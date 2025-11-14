# 📊 Monitor DI Futuro - Resumo Executivo

## ✅ O que foi criado

Uma aplicação web completa para visualizar e analisar taxas DI Futuro da B3, com:

### Funcionalidades principais:
- 📈 **Visão Geral**: Comparação de taxas entre períodos históricos
- 📊 **Análise por Período**: Detalhamento de cada período
- 🔥 **Heatmap**: Visualização comparativa em matriz
- 📋 **Dados Brutos**: Exportação e filtragem

### Tecnologias:
- **Frontend**: Streamlit (Python)
- **Visualização**: Plotly (gráficos interativos)
- **Coleta de dados**: Selenium (web scraping B3)
- **Deploy**: Streamlit Cloud (gratuito) ou Docker

---

## 🚀 Como usar - 3 opções

### Opção 1: Teste Local Rápido (5 min)
```bash
pip install streamlit pandas plotly selenium webdriver-manager
python dados_di.py
streamlit run app.py
```
→ Acesse: http://localhost:8501

### Opção 2: Deploy Streamlit Cloud ⭐ RECOMENDADO
**Por quê?**
- ✅ 100% GRATUITO
- ✅ Deploy em 2 minutos
- ✅ HTTPS automático
- ✅ Sem servidor para gerenciar

**Como fazer:**
1. Crie repositório no GitHub
2. Faça upload dos arquivos: `app.py`, `dados_di.py`, `requirements.txt`
3. Execute `python dados_di.py` localmente e commit `data/dados_di.csv`
4. Acesse https://streamlit.io/cloud
5. Login com GitHub → "New app" → Selecione seu repo → Deploy!

**URL final:** `https://seu-usuario-repo.streamlit.app`

### Opção 3: Docker (Controle total)
```bash
docker-compose up -d
```
→ Acesse: http://localhost:8501

---

## 📁 Arquivos importantes

### Essenciais para funcionamento:
- `app.py` - Aplicação Streamlit principal
- `dados_di.py` - Script de coleta de dados
- `requirements.txt` - Dependências Python

### Para deploy:
- `Dockerfile` - Container Docker
- `docker-compose.yml` - Orquestração Docker
- `.streamlit/config.toml` - Configurações do Streamlit

### Automação:
- `.github/workflows/update-data.yml` - GitHub Actions (atualização automática)

### Documentação:
- `README.md` - Documentação completa
- `QUICKSTART.md` - Guia rápido
- `.gitignore` - Arquivos a ignorar no Git

---

## ⚠️ Pontos importantes

### 1. Coleta de dados
O web scraping precisa do Chrome instalado e roda melhor localmente.

**No Streamlit Cloud:**
- Execute `python dados_di.py` localmente
- Commit o arquivo `data/dados_di.csv` no GitHub
- O Streamlit Cloud usa o CSV commitado

**Automação via GitHub Actions:**
- Configure o workflow `.github/workflows/update-data.yml`
- Roda automaticamente segunda a sexta às 10h
- Atualiza os dados no repositório

### 2. Estrutura de dados esperada
O arquivo `data/dados_di.csv` deve ter:
```csv
data_vencimento,preco,data_preco
Jan-26,0.12345,hoje
Fev-26,0.12456,hoje
...
```

### 3. Performance
- Cache configurado (1 hora)
- Gráficos otimizados com Plotly
- App responsivo

---

## 🔄 Atualizando dados

### Manual (local):
```bash
python dados_di.py
```

### Automático (GitHub Actions):
1. Já está configurado em `.github/workflows/update-data.yml`
2. Roda automaticamente seg-sex às 10h (horário UTC 13:00)
3. Commit automático se houver alterações

### Agendado (local):

**Windows Task Scheduler:**
- Programa: `python.exe`
- Argumentos: `dados_di.py`
- Frequência: Diária às 9h

**Linux/Mac crontab:**
```bash
0 9 * * 1-5 cd /caminho/projeto && python dados_di.py
```

---

## 🎨 Personalizações possíveis

### 1. Cores e tema
Edite `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF4B4B"  # Sua cor
backgroundColor = "#0E1117"
```

### 2. Adicionar mais períodos
Em `dados_di.py`, adicione em `datas_referencia`:
```python
'vinte_anos_atras': datetime.now() - timedelta(days=20 * 365)
```

### 3. Novos gráficos
No `app.py`, adicione funções como `criar_grafico_candlestick()`, etc.

---

## 🐛 Troubleshooting comum

| Problema | Solução |
|----------|---------|
| Streamlit não instala | `pip install --upgrade pip` depois `pip install streamlit` |
| Chrome/driver error | `pip install --upgrade webdriver-manager` |
| Dados não aparecem | Execute `python dados_di.py` primeiro |
| Porta 8501 ocupada | Use `--server.port 8502` |
| GitHub Actions falha | Verifique permissões de write no repo |

---

## 📊 Comparação de opções de deploy

| Critério | Streamlit Cloud | Docker Local | Docker VPS |
|----------|----------------|--------------|------------|
| **Custo** | 🟢 Grátis | 🟢 Grátis | 🟡 $5-20/mês |
| **Setup** | 🟢 2 min | 🟡 10 min | 🟡 30 min |
| **Manutenção** | 🟢 Zero | 🟡 Baixa | 🔴 Média |
| **HTTPS** | 🟢 Incluído | 🔴 Manual | 🔴 Manual |
| **Scraping** | 🔴 Limitado | 🟢 Total | 🟢 Total |
| **Recursos** | 🟡 Limitados | 🟢 Ilimitados | 🟢 Customizável |

**Legenda:** 🟢 Ótimo | 🟡 Bom | 🔴 Requer atenção

---

## 🎯 Recomendação final

### Para você (Quaest):

**Cenário 1: MVP/Teste (Começar hoje)**
→ Use **Streamlit Cloud**
- Deploy em 5 minutos
- Sem custos
- Atualize dados manualmente por enquanto

**Cenário 2: Uso interno regular**
→ Use **Streamlit Cloud + GitHub Actions**
- Deploy no Streamlit Cloud (gratuito)
- GitHub Actions atualiza dados automaticamente
- Zero manutenção

**Cenário 3: Produção enterprise**
→ Use **Docker em VPS**
- Controle total
- Scraping automático
- Integração com outros sistemas

---

## 📈 Próximos passos sugeridos

### Curto prazo:
- [ ] Testar localmente
- [ ] Deploy no Streamlit Cloud
- [ ] Configurar GitHub Actions

### Médio prazo:
- [ ] Adicionar autenticação (se necessário)
- [ ] Integrar com banco de dados
- [ ] Adicionar mais visualizações

### Longo prazo:
- [ ] API REST para os dados
- [ ] Dashboard administrativo
- [ ] Alertas automáticos por email

---

## 💡 Dicas profissionais

1. **Comece simples**: Deploy no Streamlit Cloud hoje mesmo
2. **Dados**: Execute coleta localmente, commit no GitHub
3. **Automação**: Configure GitHub Actions depois de testar
4. **Monitoramento**: Use os logs do Streamlit Cloud
5. **Backup**: Mantenha cópias dos dados CSV

---

## 📞 Suporte

### Documentação:
- README.md (completo)
- QUICKSTART.md (rápido)
- Comentários no código

### Recursos online:
- Streamlit Docs: https://docs.streamlit.io
- Streamlit Cloud: https://streamlit.io/cloud
- Plotly Docs: https://plotly.com/python/

### Comunidade:
- Streamlit Forum: https://discuss.streamlit.io
- GitHub Issues: (seu repositório)

---

## ✨ Resumo ultra-rápido

```bash
# 1. Instalar
pip install streamlit pandas plotly selenium webdriver-manager

# 2. Coletar dados
python dados_di.py

# 3. Rodar app
streamlit run app.py
```

**Ou deploy gratuito:**
1. GitHub → Novo repositório
2. Upload: app.py, dados_di.py, requirements.txt, data/
3. streamlit.io/cloud → Deploy
4. ✅ Pronto!

---

**Boa sorte com o projeto! 🚀**

*Qualquer dúvida, consulte o README.md completo ou abra uma issue no GitHub.*
