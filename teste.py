import streamlit as st

# =========================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================
st.set_page_config(
    page_title="Empresas Parceiras",
    page_icon="🌐",
    layout="wide"
)

# =========================================
# TÍTULO
# =========================================
st.title("🌎 Empresas Parceiras")
st.write("Confira algumas empresas incríveis abaixo.")

# =========================================
# COLUNAS
# =========================================
col1, col2, col3 = st.columns(3)

# =========================================
# EMPRESA 1
# =========================================
with col1:
    st.image("empresa1.png", use_container_width=True)
    st.subheader("🚀 SpaceX")
    st.write("Empresa de tecnologia espacial fundada por Elon Musk.")
    st.link_button(
        "Acessar Site",
        "https://www.spacex.com"
    )

# =========================================
# EMPRESA 2
# =========================================
with col2:
    st.image("empresa2.png", use_container_width=True)
    st.subheader("🍎 Apple")
    st.write("Empresa mundialmente conhecida por iPhones e Macs.")
    st.link_button(
        "Acessar Site",
        "https://www.apple.com"
    )

# =========================================
# EMPRESA 3
# =========================================
with col3:
    st.image("empresa3.png", use_container_width=True)
    st.subheader("🎬 Netflix")
    st.write("Plataforma líder de filmes e séries online.")
    st.link_button(
        "Acessar Site",
        "https://www.netflix.com"
    )

# =========================================
# RODAPÉ
# =========================================
st.write("---")
st.write("Desenvolvido por Dinaldo Jorge")
