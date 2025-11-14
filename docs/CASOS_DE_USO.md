# 📊 Casos de Uso Práticos - Monitor DI Futuro

## Visão Geral

Este guia apresenta exemplos práticos de como usar a aplicação para diferentes análises e tomadas de decisão.

---

## 🎯 Caso de Uso 1: Análise de Tendência de Mercado

### Objetivo
Identificar se as expectativas de taxa de juros estão aumentando ou diminuindo ao longo do tempo.

### Como fazer:
1. Acesse a aba **"📈 Visão Geral"**
2. Observe o gráfico de linhas com múltiplos períodos
3. Compare as curvas:
   - **Hoje** vs **1 Ano Atrás**
   - **3 Anos Atrás** vs **5 Anos Atrás**

### O que observar:
- **Curva subindo**: Mercado espera juros mais altos
- **Curva descendo**: Mercado espera juros mais baixos
- **Inversão da curva**: Vencimentos curtos com taxa maior que longos (recessão?)

### Exemplo de interpretação:
```
Se a curva "Hoje" está acima de "1 Ano Atrás":
→ As expectativas de juros aumentaram no último ano
→ Possível indicação de inflação ou política monetária restritiva
```

---

## 🎯 Caso de Uso 2: Análise de Oportunidade de Investimento

### Objetivo
Identificar vencimentos com melhores taxas para investimento.

### Como fazer:
1. Vá para **"📊 Análise por Período"**
2. Selecione "Hoje" no dropdown
3. Observe o gráfico de barras
4. Identifique vencimentos com taxas mais altas

### Estratégia:
- **Taxa mais alta + prazo adequado** = Melhor relação risco/retorno
- **Compare com metas de investimento**
- **Considere liquidez vs. rentabilidade**

### Exemplo prático:
```
Cenário: Você tem R$ 100.000 para investir por 2 anos

1. Olhe vencimentos entre 18-30 meses
2. Identifique a maior taxa nesse intervalo
3. Compare com CDI atual
4. Considere spread de risco

Taxa encontrada: 12.5% a.a. (venc. Jan-27)
CDI atual: 11.75%
Spread: +0.75 p.p.
→ Oportunidade interessante se aceita baixa liquidez
```

---

## 🎯 Caso de Uso 3: Comparação Histórica de Política Monetária

### Objetivo
Entender como a política monetária mudou ao longo dos anos.

### Como fazer:
1. Acesse **"🔥 Heatmap Comparativo"**
2. Observe as cores:
   - 🔴 Vermelho = Taxas altas
   - 🟢 Verde = Taxas baixas
3. Compare colunas (períodos diferentes)
4. Compare linhas (mesmo vencimento em diferentes épocas)

### Análise:
```
Coluna "10 Anos Atrás" toda vermelha:
→ Período de juros muito altos (Selic elevada)
→ Contexto: Crise? Inflação alta?

Coluna "Hoje" mais verde:
→ Juros menores que no passado
→ Possível ciclo de flexibilização monetária
```

---

## 🎯 Caso de Uso 4: Planejamento Financeiro Empresarial

### Objetivo
Planejar captação de recursos ou aplicações de tesouraria.

### Como fazer:
1. Identifique necessidade/disponibilidade de caixa
2. Vá para **"📊 Análise por Período"** → Hoje
3. Encontre vencimento que coincida com necessidade
4. Use métricas:
   - Taxa Mínima: Piso de mercado
   - Taxa Média: Referência
   - Taxa Máxima: Teto de mercado

### Exemplo - Captação:
```
Empresa precisa de R$ 5MM em 12 meses

Análise da curva DI:
- Vencimento: Jan-26 (12 meses)
- Taxa DI: 11.8% a.a.
- Banco oferece: CDI + 2.5% = 14.3% a.a.

Decisão:
→ Se pode esperar: Não captar agora (caro)
→ Se urgente: Negociar spread menor
→ Alternativa: Captar em prazo menor e rolar
```

### Exemplo - Aplicação:
```
Tesouraria com R$ 10MM disponíveis por 6 meses

Análise:
- DI Jul-25: 11.2% a.a.
- DI Jan-26: 11.8% a.a.
- Diferença: +0.6 p.p.

Decisão:
→ Estender prazo para Jan-26 se não precisa de liquidez
→ Ganho extra de ~R$ 30k (0.6% s/ 10MM / 2)
```

---

## 🎯 Caso de Uso 5: Análise de Risco de Carteira

### Objetivo
Avaliar exposição de uma carteira de renda fixa às mudanças de juros.

### Como fazer:
1. Liste os vencimentos da sua carteira
2. Na aba **"📋 Dados Brutos"**:
   - Filtre vencimentos específicos
   - Compare taxas "Hoje" vs períodos anteriores
3. Calcule variação de valor

### Análise de duration:
```
Carteira exemplo:
- R$ 5MM em Jan-26 (12m) @ 11.5%
- R$ 3MM em Jan-27 (24m) @ 12.0%
- R$ 2MM em Jan-28 (36m) @ 12.3%

Se taxas subirem 1 p.p.:
- Jan-26: Perda ~1% (R$ 50k)
- Jan-27: Perda ~2% (R$ 60k)
- Jan-28: Perda ~3% (R$ 60k)
Total: R$ 170k de MTM negativo

→ Considerar hedge ou reduzir duration
```

---

## 🎯 Caso de Uso 6: Relatório para Comitê de Investimentos

### Objetivo
Preparar análise para apresentação executiva.

### Como fazer:
1. **Visão Geral** → Screenshot do gráfico de linhas
2. **Métricas** → Copie tabela comparativa
3. **Análise por Período** → Gráfico de barras "Hoje"
4. **Dados Brutos** → Exporte CSV

### Template de relatório:
```markdown
## Análise DI Futuro - [Data]

### Executive Summary
- Taxa curto prazo (12m): X.XX%
- Taxa média (24m): X.XX%
- Variação vs 1 ano: +/-X.XX p.p.

### Principais Insights
1. [Tendência observada]
2. [Oportunidades identificadas]
3. [Riscos relevantes]

### Recomendações
- [ ] Ação 1
- [ ] Ação 2
- [ ] Ação 3

[Anexar gráficos da aplicação]
```

---

## 🎯 Caso de Uso 7: Arbitragem e Trading

### Objetivo
Identificar oportunidades de arbitragem na curva de juros.

### Como fazer:
1. Olhe para a curva em **"Visão Geral"**
2. Identifique anomalias:
   - Vencimento "fora da curva"
   - Inversões incomuns
   - Spreads incomuns entre vencimentos próximos

### Oportunidades:
```
Cenário 1: Vencimento com taxa anormal
Jan-26: 11.5%
Fev-26: 12.2%  ← ANOMALIA (muito alto)
Mar-26: 11.7%

Estratégia:
→ Vender Fev-26 (caro)
→ Comprar Jan-26 + Mar-26 (baratos)
→ Spread trade

Cenário 2: Curva invertida
12 meses: 12.0%
24 meses: 11.5%  ← Inversão

Estratégia:
→ Se acredita em normalização: Comprar 24m
→ Se acredita em crise: Comprar 12m
```

---

## 🎯 Caso de Uso 8: Hedging de Operações Estruturadas

### Objetivo
Determinar estratégia de hedge para produtos estruturados.

### Exemplo - Swap Pré x CDI:
```
Cliente contratou Swap:
- Recebe: 12% a.a. pré-fixado
- Paga: CDI
- Prazo: 24 meses
- Nocional: R$ 50MM

Análise na aplicação:
1. Taxa DI 24m hoje: 11.8%
2. Expectativa: Taxas caindo

Estratégia de hedge:
→ Se DI atual < Taxa pré (11.8% < 12%): Cliente ganha
→ Banco precisa hedge: Vender DI futuro 24m
→ Quantidade: Proporcional ao nocional e duration
```

---

## 🎯 Caso de Uso 9: Análise Macroeconômica

### Objetivo
Usar curva DI como indicador antecedente de economia.

### Indicadores:
1. **Inclinação da curva**
   ```
   Curva íngreme (longo > curto):
   → Expectativa de crescimento econômico
   → Inflação futura?
   
   Curva invertida (curto > longo):
   → Possível recessão
   → Corte de juros esperado
   ```

2. **Nível absoluto**
   ```
   Taxas muito altas:
   → Política monetária restritiva
   → Combate à inflação
   
   Taxas baixas:
   → Estímulo econômico
   → Crescimento esperado
   ```

3. **Volatilidade**
   ```
   Compare períodos no heatmap:
   Mudanças bruscas = Incerteza alta
   Curvas estáveis = Mercado confiante
   ```

---

## 🎯 Caso de Uso 10: Due Diligence de Investimentos

### Objetivo
Avaliar produtos de renda fixa antes de investir.

### Checklist:
1. **Compare com DI**
   ```
   Produto oferecido: CDB 120% CDI, 2 anos
   Taxa DI 24m: 11.8%
   Taxa equivalente: 11.8% × 1.20 = 14.16%
   
   Análise:
   → Se DI puro paga 11.8%
   → CDB paga 14.16%
   → Premium: +2.36 p.p.
   → Justifica o risco de crédito?
   ```

2. **Análise de cenários**
   ```
   Cenário Base (DI hoje): 11.8%
   Cenário Alta: +1 p.p. = 12.8%
   Cenário Baixa: -1 p.p. = 10.8%
   
   Retorno CDB 120% CDI:
   Base: 14.16%
   Alta: 15.36%
   Baixa: 12.96%
   
   → Ainda atrativo no cenário baixa?
   ```

---

## 📊 Métricas Chave para Monitorar

### Diariamente:
- [ ] Taxa DI 12 meses (referência curto prazo)
- [ ] Variação vs dia anterior
- [ ] Spread entre vencimentos

### Semanalmente:
- [ ] Movimento da curva completa
- [ ] Comparação com semana anterior
- [ ] Identificar tendências

### Mensalmente:
- [ ] Análise histórica completa
- [ ] Performance vs benchmark
- [ ] Ajuste de estratégia

---

## 🎓 Dicas Profissionais

1. **Contexto é fundamental**
   - Nunca analise DI isoladamente
   - Considere: Selic, inflação, PIB, câmbio

2. **Use múltiplos períodos**
   - Compare sempre com histórico
   - Entenda o "normal" vs "anormal"

3. **Combine com outras fontes**
   - Notícias econômicas
   - Relatórios de bancos
   - Focus BACEN

4. **Documente suas análises**
   - Exporte os dados
   - Mantenha histórico de decisões
   - Aprenda com acertos e erros

5. **Automatize monitoramento**
   - Configure alertas (futura feature)
   - Revise dados diariamente
   - Mantenha disciplina

---

## 📈 Próximos Passos

Depois de dominar esses casos de uso:

1. [ ] Integre com seu processo de análise
2. [ ] Crie dashboards personalizados
3. [ ] Automatize relatórios
4. [ ] Compartilhe insights com equipe
5. [ ] Refine estratégias baseado em dados

---

**Lembre-se**: Esta aplicação é uma ferramenta. O valor está na sua análise e interpretação dos dados! 💡

