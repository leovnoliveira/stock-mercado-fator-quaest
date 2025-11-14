# 🚀 Tutorial Completo: Deploy no Streamlit Cloud

## Por que Streamlit Cloud?

- ✅ **100% GRATUITO** (sem cartão de crédito)
- ✅ Deploy em **2 minutos**
- ✅ HTTPS automático com certificado SSL
- ✅ Domínio gratuito: `seu-app.streamlit.app`
- ✅ Atualizações automáticas via Git
- ✅ Sem necessidade de servidor ou VPS

---

## 📋 Pré-requisitos

- Conta no GitHub (gratuita)
- Arquivos do projeto
- 5 minutos do seu tempo

---

## 🎬 Passo a Passo Detalhado

### Etapa 1: Preparar o Repositório GitHub (5 min)

#### 1.1 Criar novo repositório
1. Acesse: https://github.com
2. Clique em "New repository" (botão verde)
3. Preencha:
   - **Repository name**: `monitor-di-futuro`
   - **Description**: `Aplicação Streamlit para monitorar taxas DI Futuro da B3`
   - **Visibilidade**: Public (para usar Streamlit Cloud gratuito)
   - **Inicializar**: ✅ Add a README file
4. Clique em "Create repository"

#### 1.2 Coletar dados localmente
```bash
# No seu computador, execute:
python dados_di.py

# Isso cria o arquivo: data/dados_di.csv
```

⚠️ **Importante**: O Streamlit Cloud não executa web scraping automaticamente, então você precisa coletar os dados localmente primeiro.

#### 1.3 Upload dos arquivos

**Opção A: Via interface web do GitHub**

1. No seu repositório, clique em "Add file" → "Upload files"
2. Arraste os seguintes arquivos:
   ```
   ✅ app.py
   ✅ dados_di.py
   ✅ requirements.txt
   ✅ .gitignore
   ```
3. Crie a pasta `data/` e faça upload de:
   ```
   ✅ dados_di.csv (gerado pelo script)
   ```
4. (Opcional) Crie pasta `.streamlit/` e faça upload de:
   ```
   ✅ config.toml
   ```
5. (Opcional) Crie pasta `.github/workflows/` e faça upload de:
   ```
   ✅ update-data.yml
   ```
6. Clique em "Commit changes"

**Opção B: Via Git (linha de comando)**

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/monitor-di-futuro.git
cd monitor-di-futuro

# Copie os arquivos para o diretório
cp /caminho/dos/arquivos/* .

# Adicione e commit
git add .
git commit -m "Adicionar aplicação Monitor DI"
git push origin main
```

#### 1.4 Verificar estrutura

Seu repositório deve ficar assim:
```
monitor-di-futuro/
├── .github/
│   └── workflows/
│       └── update-data.yml
├── .streamlit/
│   └── config.toml
├── data/
│   └── dados_di.csv
├── app.py
├── dados_di.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

### Etapa 2: Deploy no Streamlit Cloud (2 min)

#### 2.1 Acessar Streamlit Cloud
1. Vá para: https://streamlit.io/cloud
2. Clique em "Sign up" ou "Get started"

#### 2.2 Conectar com GitHub
1. Clique em "Continue with GitHub"
2. Autorize o Streamlit Cloud a acessar seus repositórios
3. (Primeira vez) Preencha informações básicas:
   - Nome
   - Email
   - Aceite os termos

#### 2.3 Criar novo app
1. No dashboard, clique em "New app"
2. Preencha os campos:
   
   **Repository**
   - Selecione: `seu-usuario/monitor-di-futuro`
   
   **Branch**
   - Deixe: `main` (ou `master` se for o caso)
   
   **Main file path**
   - Digite: `app.py`
   
   **App URL (opcional)**
   - Customize se quiser: `monitor-di-quaest.streamlit.app`
   - Ou deixe o padrão: `seu-usuario-monitor-di-futuro.streamlit.app`

3. (Opcional) Advanced settings:
   - **Python version**: 3.10 (recomendado)
   - **Secrets**: Deixe em branco por enquanto

4. Clique no botão **"Deploy!"**

#### 2.4 Aguardar o deploy
1. Você verá uma tela de loading com logs
2. O processo leva **1-3 minutos**
3. Você verá:
   ```
   Installing dependencies from requirements.txt...
   ✓ streamlit installed
   ✓ pandas installed
   ✓ plotly installed
   ...
   Starting up...
   ✓ App is live!
   ```

#### 2.5 Testar o app
1. Quando aparecer "Your app is live!", clique no link
2. Ou acesse: `https://seu-app.streamlit.app`
3. Você verá sua aplicação rodando! 🎉

---

### Etapa 3: Configurações Opcionais

#### 3.1 Domínio customizado
1. No Streamlit Cloud, vá em Settings → General
2. Em "App URL", clique em "Edit"
3. Escolha um novo nome (ex: `quaest-di-monitor`)
4. Salve (pode levar alguns minutos)

#### 3.2 Secrets (dados sensíveis)
Se precisar de credenciais:
1. Vá em Settings → Secrets
2. Adicione no formato TOML:
   ```toml
   [database]
   host = "seu-host"
   password = "sua-senha"
   ```
3. No código, acesse com:
   ```python
   import streamlit as st
   st.secrets["database"]["host"]
   ```

#### 3.3 Recursos e limites
- No plano gratuito:
  - 1 GB de RAM
  - 1 CPU core
  - Sleeps após 7 dias sem uso
  - Reativa automaticamente ao acessar

---

### Etapa 4: Atualização Automática de Dados

#### Opção A: Manual (simples)
1. Execute localmente: `python dados_di.py`
2. Commit e push o novo `dados_di.csv`
3. Streamlit Cloud atualiza automaticamente

```bash
python dados_di.py
git add data/dados_di.csv
git commit -m "Atualizar dados DI"
git push
```

#### Opção B: GitHub Actions (automático)
Já está configurado no arquivo `.github/workflows/update-data.yml`!

1. Verifique se o arquivo está no repositório
2. GitHub Actions vai rodar automaticamente:
   - Segunda a sexta
   - Às 10h (horário de Brasília)
3. Coleta dados e faz commit automático
4. Streamlit Cloud detecta e atualiza

**Ativar GitHub Actions:**
1. Vá no seu repositório
2. Clique na aba "Actions"
3. Se aparecer botão verde, clique em "I understand, enable Actions"

---

## 🔄 Fluxo de Atualização

```
┌─────────────────────┐
│  GitHub Actions     │
│  (seg-sex às 10h)   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Executa            │
│  dados_di.py        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Commit automático  │
│  dados_di.csv       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Streamlit Cloud    │
│  detecta mudança    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  App atualizado!    │
│  ✅                 │
└─────────────────────┘
```

---

## 🎨 Personalização

### Alterar cores
1. Edite `.streamlit/config.toml`
2. Commit e push
3. Aguarde rebuild automático

### Adicionar funcionalidades
1. Edite `app.py`
2. Commit e push
3. Streamlit Cloud rebuilda automaticamente

---

## 📊 Monitoramento

### Ver logs
1. No Streamlit Cloud dashboard
2. Clique no seu app
3. Vá em "Manage app" → "Logs"
4. Veja logs em tempo real

### Analytics (opcional)
1. Vá em Settings → Analytics
2. Veja:
   - Número de visitantes
   - Tempo de uso
   - Erros

---

## 🐛 Troubleshooting

### App não inicia
**Problema**: Erro ao instalar dependências
**Solução**:
```bash
# Verifique requirements.txt
# Teste localmente primeiro:
pip install -r requirements.txt
streamlit run app.py
```

### App fica em "Sleeping"
**Problema**: App não usado por 7 dias
**Solução**: 
- É normal no plano gratuito
- Acesse o link e ele reativa automaticamente
- Ou upgrade para plano pago

### Dados não aparecem
**Problema**: Arquivo `dados_di.csv` não existe
**Solução**:
1. Execute `python dados_di.py` localmente
2. Commit o arquivo gerado
3. Push para o GitHub

### GitHub Actions falha
**Problema**: Permissões
**Solução**:
1. Vá em Settings → Actions → General
2. Em "Workflow permissions"
3. Selecione "Read and write permissions"
4. Salve

---

## 💰 Custos

### Plano Gratuito (Community)
- ✅ Apps ilimitados (públicos)
- ✅ 1 GB RAM por app
- ✅ 1 CPU core
- ✅ HTTPS incluído
- ⚠️ App dorme após 7 dias sem uso
- ⚠️ Não tem apps privados

### Plano Pago (quando crescer)
- **Team**: $20/mês/membro
  - Apps privados
  - 4 GB RAM
  - Sem sleep
  - Suporte prioritário

---

## 📈 Checklist Final

Antes de considerar o deploy completo:

- [ ] App funciona localmente
- [ ] Todos os arquivos no GitHub
- [ ] dados_di.csv commitado
- [ ] Deploy no Streamlit Cloud feito
- [ ] App abrindo sem erros
- [ ] Dados aparecendo corretamente
- [ ] GitHub Actions configurado (opcional)
- [ ] Testado atualização de dados
- [ ] Documentação README atualizada
- [ ] Link compartilhado com equipe

---

## 🎉 Pronto!

Seu app está no ar em:
`https://seu-app.streamlit.app`

### Próximos passos:
1. ✅ Compartilhe o link com sua equipe
2. ✅ Configure atualizações automáticas
3. ✅ Monitore os logs
4. ✅ Colete feedback
5. ✅ Itere e melhore

---

## 📚 Recursos úteis

- **Streamlit Docs**: https://docs.streamlit.io
- **Deploy Guide**: https://docs.streamlit.io/deploy
- **Community Forum**: https://discuss.streamlit.io
- **Status Page**: https://streamlitstatus.com

---

## 💡 Dicas finais

1. **Teste sempre localmente primeiro**
   ```bash
   streamlit run app.py
   ```

2. **Use o mesmo Python localmente e no Cloud**
   - Recomendado: Python 3.10

3. **Mantenha requirements.txt limpo**
   - Só as dependências necessárias
   - Versões compatíveis

4. **Monitore o uso**
   - Fique de olho nos logs
   - Observe o tempo de resposta

5. **Documente bem**
   - README atualizado
   - Comentários no código
   - Instruções claras

---

**Boa sorte com seu deploy! 🚀**

Se tiver dúvidas, consulte a documentação ou abra uma issue no GitHub.
