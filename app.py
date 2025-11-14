import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import os

# Configuração da página
st.set_page_config(
    page_title="Monitor DI Futuro - B3",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
    }
    h1 {
        color: #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data(ttl=3600)
def carregar_dados():
    """Carrega os dados do CSV"""
    try:
        # Tenta carregar do diretório data
        df = pd.read_csv('data/dados_di.csv')
    except:
        try:
            # Tenta carregar do diretório atual
            df = pd.read_csv('dados_di.csv')
        except:
            return None
    return df

def preparar_dados(df):
    """Prepara os dados para visualização"""
    # Mapeamento dos períodos
    periodo_map = {
        'hoje': 'Hoje',
        'um_ano_atras': '1 Ano Atrás',
        'tres_anos_atras': '3 Anos Atrás',
        'cinco_anos_atras': '5 Anos Atrás',
        'dez_anos_atras': '10 Anos Atrás'
    }
    
    df['periodo_label'] = df['data_preco'].map(periodo_map)
    
    # Converte data_vencimento para datetime para ordenação
    df['data_vencimento_dt'] = pd.to_datetime(df['data_vencimento'], format='%b-%y', errors='coerce')
    
    return df

def criar_grafico_linha(df):
    """Cria gráfico de linha com evolução das taxas DI"""
    fig = go.Figure()
    
    periodos = df['periodo_label'].unique()
    cores = px.colors.qualitative.Set2
    
    for i, periodo in enumerate(periodos):
        dados_periodo = df[df['periodo_label'] == periodo].sort_values('data_vencimento_dt')
        
        fig.add_trace(go.Scatter(
            x=dados_periodo['data_vencimento'],
            y=dados_periodo['preco'],
            mode='lines+markers',
            name=periodo,
            line=dict(width=2, color=cores[i % len(cores)]),
            marker=dict(size=6),
            hovertemplate='<b>%{x}</b><br>Taxa: %{y:.5f}<extra></extra>'
        ))
    
    fig.update_layout(
        title='Evolução das Taxas DI Futuro por Período',
        xaxis_title='Vencimento',
        yaxis_title='Taxa',
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        height=500,
        template='plotly_white'
    )
    
    return fig

def criar_grafico_barras(df, periodo_selecionado):
    """Cria gráfico de barras para um período específico"""
    dados = df[df['periodo_label'] == periodo_selecionado].sort_values('data_vencimento_dt')
    
    fig = go.Figure(data=[
        go.Bar(
            x=dados['data_vencimento'],
            y=dados['preco'],
            marker_color='lightblue',
            text=dados['preco'].round(5),
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Taxa: %{y:.5f}<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title=f'Taxas DI Futuro - {periodo_selecionado}',
        xaxis_title='Vencimento',
        yaxis_title='Taxa',
        height=400,
        template='plotly_white'
    )
    
    return fig

def criar_heatmap(df):
    """Cria heatmap comparativo entre períodos"""
    # Pivot para criar matriz
    pivot = df.pivot(index='data_vencimento', columns='periodo_label', values='preco')
    
    # Ordena as colunas
    ordem_colunas = ['Hoje', '1 Ano Atrás', '3 Anos Atrás', '5 Anos Atrás', '10 Anos Atrás']
    pivot = pivot[[col for col in ordem_colunas if col in pivot.columns]]
    
    fig = go.Figure(data=go.Heatmap(
        z=pivot.values,
        x=pivot.columns,
        y=pivot.index,
        colorscale='RdYlGn_r',
        text=pivot.values.round(5),
        texttemplate='%{text}',
        textfont={"size": 10},
        hovertemplate='Período: %{x}<br>Vencimento: %{y}<br>Taxa: %{z:.5f}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Heatmap Comparativo de Taxas DI',
        xaxis_title='Período',
        yaxis_title='Vencimento',
        height=600,
        template='plotly_white'
    )
    
    return fig

def calcular_metricas(df, periodo):
    """Calcula métricas para um período específico"""
    dados = df[df['periodo_label'] == periodo]
    
    if len(dados) == 0:
        return None, None, None, None
    
    taxa_min = dados['preco'].min()
    taxa_max = dados['preco'].max()
    taxa_media = dados['preco'].mean()
    taxa_mediana = dados['preco'].median()
    
    return taxa_min, taxa_max, taxa_media, taxa_mediana

def main():
    # Título
    st.title("📊 Monitor DI Futuro - B3")
    st.markdown("---")
    
    # Carregar dados
    with st.spinner('Carregando dados...'):
        df = carregar_dados()
    
    if df is None or df.empty:
        st.error("⚠️ Não foi possível carregar os dados. Execute o script de coleta primeiro!")
        st.info("Execute: `python dados_di.py` para coletar os dados.")
        st.stop()
    
    # Preparar dados
    df = preparar_dados(df)
    
    # Sidebar
    st.sidebar.header("⚙️ Configurações")
    
    # Seleção de visualização
    tipo_visualizacao = st.sidebar.radio(
        "Tipo de Visualização:",
        ["📈 Visão Geral", "📊 Análise por Período", "🔥 Heatmap Comparativo", "📋 Dados Brutos"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"**Última atualização:** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    st.sidebar.markdown(f"**Total de registros:** {len(df)}")
    
    # Conteúdo principal
    if tipo_visualizacao == "📈 Visão Geral":
        st.header("Visão Geral das Taxas DI")
        
        # Métricas resumidas
        col1, col2, col3, col4 = st.columns(4)
        
        dados_hoje = df[df['periodo_label'] == 'Hoje']
        if len(dados_hoje) > 0:
            with col1:
                st.metric("Taxa Mínima (Hoje)", f"{dados_hoje['preco'].min():.5f}")
            with col2:
                st.metric("Taxa Máxima (Hoje)", f"{dados_hoje['preco'].max():.5f}")
            with col3:
                st.metric("Taxa Média (Hoje)", f"{dados_hoje['preco'].mean():.5f}")
            with col4:
                st.metric("Nº Vencimentos", len(dados_hoje))
        
        st.markdown("---")
        
        # Gráfico principal
        fig = criar_grafico_linha(df)
        st.plotly_chart(fig, use_container_width=True)
        
        # Análise comparativa
        st.subheader("📊 Comparação entre Períodos")
        
        col1, col2 = st.columns(2)
        
        periodos = ['Hoje', '1 Ano Atrás', '3 Anos Atrás', '5 Anos Atrás', '10 Anos Atrás']
        metricas_df = []
        
        for periodo in periodos:
            if periodo in df['periodo_label'].values:
                min_val, max_val, media, mediana = calcular_metricas(df, periodo)
                if min_val is not None:
                    metricas_df.append({
                        'Período': periodo,
                        'Mínima': f"{min_val:.5f}",
                        'Máxima': f"{max_val:.5f}",
                        'Média': f"{media:.5f}",
                        'Mediana': f"{mediana:.5f}"
                    })
        
        if metricas_df:
            st.dataframe(pd.DataFrame(metricas_df), use_container_width=True, hide_index=True)
    
    elif tipo_visualizacao == "📊 Análise por Período":
        st.header("Análise Detalhada por Período")
        
        periodos_disponiveis = df['periodo_label'].unique().tolist()
        periodo_selecionado = st.selectbox(
            "Selecione o período:",
            periodos_disponiveis
        )
        
        # Métricas do período
        col1, col2, col3, col4 = st.columns(4)
        min_val, max_val, media, mediana = calcular_metricas(df, periodo_selecionado)
        
        with col1:
            st.metric("Taxa Mínima", f"{min_val:.5f}")
        with col2:
            st.metric("Taxa Máxima", f"{max_val:.5f}")
        with col3:
            st.metric("Taxa Média", f"{media:.5f}")
        with col4:
            st.metric("Taxa Mediana", f"{mediana:.5f}")
        
        st.markdown("---")
        
        # Gráfico de barras
        fig = criar_grafico_barras(df, periodo_selecionado)
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabela de dados
        st.subheader("📋 Dados Detalhados")
        dados_periodo = df[df['periodo_label'] == periodo_selecionado][['data_vencimento', 'preco']].sort_values('data_vencimento')
        dados_periodo['preco'] = dados_periodo['preco'].apply(lambda x: f"{x:.5f}")
        st.dataframe(dados_periodo, use_container_width=True, hide_index=True)
    
    elif tipo_visualizacao == "🔥 Heatmap Comparativo":
        st.header("Heatmap Comparativo de Taxas")
        
        st.markdown("""
        Este heatmap permite visualizar as diferenças nas taxas DI entre diferentes períodos históricos.
        Cores mais quentes (vermelhas) indicam taxas mais altas, enquanto cores mais frias (verdes) indicam taxas mais baixas.
        """)
        
        fig = criar_heatmap(df)
        st.plotly_chart(fig, use_container_width=True)
        
        # Análise de variação
        st.subheader("📈 Variação entre Períodos")
        
        if 'Hoje' in df['periodo_label'].values and '1 Ano Atrás' in df['periodo_label'].values:
            hoje = df[df['periodo_label'] == 'Hoje'].set_index('data_vencimento')['preco']
            um_ano = df[df['periodo_label'] == '1 Ano Atrás'].set_index('data_vencimento')['preco']
            
            # Encontra vencimentos comuns
            vencimentos_comuns = hoje.index.intersection(um_ano.index)
            
            if len(vencimentos_comuns) > 0:
                variacao = (hoje[vencimentos_comuns] - um_ano[vencimentos_comuns]) * 100
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(
                        "Variação Média (pp)",
                        f"{variacao.mean():.2f}",
                        delta=f"{variacao.mean():.2f} pp"
                    )
                with col2:
                    st.metric(
                        "Maior Variação (pp)",
                        f"{variacao.abs().max():.2f}",
                        delta=f"{variacao.abs().max():.2f} pp"
                    )
    
    else:  # Dados Brutos
        st.header("Dados Brutos")
        
        st.markdown("### 📥 Download dos Dados")
        col1, col2 = st.columns(2)
        
        with col1:
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name=f"dados_di_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        
        st.markdown("---")
        
        # Filtros
        st.subheader("🔍 Filtros")
        col1, col2 = st.columns(2)
        
        with col1:
            periodos_filtro = st.multiselect(
                "Períodos:",
                df['periodo_label'].unique().tolist(),
                default=df['periodo_label'].unique().tolist()
            )
        
        with col2:
            vencimentos_filtro = st.multiselect(
                "Vencimentos:",
                df['data_vencimento'].unique().tolist(),
                default=[]
            )
        
        # Aplicar filtros
        df_filtrado = df[df['periodo_label'].isin(periodos_filtro)]
        if vencimentos_filtro:
            df_filtrado = df_filtrado[df_filtrado['data_vencimento'].isin(vencimentos_filtro)]
        
        # Mostrar dados
        st.markdown(f"**Registros exibidos:** {len(df_filtrado)}")
        st.dataframe(
            df_filtrado[['data_vencimento', 'preco', 'periodo_label']].sort_values(['periodo_label', 'data_vencimento']),
            use_container_width=True,
            hide_index=True
        )

if __name__ == "__main__":
    main()
