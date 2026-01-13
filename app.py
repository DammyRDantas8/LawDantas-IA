import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# 1. SEGURANÇA E CONFIGURAÇÃO
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    # Se não houver .env, tenta pegar dos Secrets do Streamlit Cloud
    api_key = st.secrets.get("GROQ_API_KEY")

if not api_key:
    st.error("ERRO: Chave da API não configurada.")
    st.stop()

client = Groq(api_key=api_key)

# 2. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="LawDantas IA", layout="wide", page_icon="⚖️")

# 3. ESTILO VISUAL (Fundo Vinho, Caixas Cinza, Texto Preto)
st.markdown("""
    <style>
    .stApp { background-color: #1A0505 !important; }
    .stTextArea textarea, .stTextInput input, .resposta-container {
        background-color: #D3D3D3 !important;
        color: #000000 !important;
        font-family: 'Arial', sans-serif !important;
        font-weight: bold !important;
        border: 2px solid #FFFFFF !important;
        border-radius: 10px !important;
    }
    .resposta-container { padding: 20px; margin-top: 20px; }
    h1, h2, h3, p { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. INTERFACE DO USUÁRIO
st.title("⚖️ HubLab Jurídico - LexTech")
st.subheader("LawDantas IA: Assistente Especialista em Direito do Trabalho e OAB")

pergunta = st.text_area("Descreva o caso jurídico ou a questão da OAB:")

if st.button("Analisar Caso"):
    if pergunta.strip():
        try:
            with st.spinner("A IA de Damiana Rodrigues Dantas está analisando..."):
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "Você é uma IA especialista em Direito Brasileiro, Direito do Trabalho e OAB."},
                        {"role": "user", "content": pergunta}
                    ],
                    model="llama3-8b-8192",
                )
                resposta = chat_completion.choices[0].message.content
                st.markdown(f'<div class="resposta-container">{resposta}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Erro na conexão: {e}")
    else:
        st.warning("Por favor, insira um texto para análise.")

# 5. RODAPÉ TÉCNICO
st.markdown("---")
st.caption("Desenvolvido por Damiana Rodrigues Dantas | Bacharel em Direito & Dev IA")
