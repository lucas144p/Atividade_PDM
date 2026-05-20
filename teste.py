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
    st.image("empresa1.jpg", use_container_width=True)
    st.subheader("Mc Donalds")
    st.write("McDonald's Corporation é uma rede multinacional estadunidense de fast food.")
    st.link_button(
        "Acessar Site",
        "https://www.mcdonalds.com.br/"
    )

# =========================================
# EMPRESA 2
# =========================================
with col2:
    st.image("empresa2.jpg", use_container_width=True)
    st.subheader("Bobs")
    st.write("Fundado em 1952 no burburinho de Copacabana, o Bob's é a primeira rede de franquias do Brasil.")
    st.link_button(
        "Acessar Site",
        "https://bobs.com.br/"
    )

# =========================================
# EMPRESA 3
# =========================================
with col3:
    st.image("empresa3.png", use_container_width=True)
    st.subheader("Burguer King")
    st.write("O Burger King é uma rede de fast-food fundada em 1954 nos Estados Unidos por James McLamore e David Edgerton.
    ")
    st.link_button(
        "Acessar Site",
        "https://www.burgerking.com.br"
    )

# =========================================
# RODAPÉ
# =========================================
st.write("---")
st.write("Desenvolvido por Lucas Andrade")
