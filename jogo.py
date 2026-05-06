import streamlit as st
import random

st.title("✊🖐️✌️ Pedra, Papel ou Tesoura!")

# Lista de opções
itens = ["👊", "🖐️", "✌️"]

# Seleção do usuário via selectbox
usuario = st.selectbox("Escolha sua jogada:", ["👊", "🖐️", "✌️"])

# Botão para jogar
if st.button("Jogar"):
    computador = random.choice(itens)

    st.write(f"Você escolheu: {usuario}")
    st.write(f"Computador escolheu: {computador}")

    if usuario == computador:
        st.success("Empate!! 🤝")
    elif (usuario == "👊" and computador == "✌️") or \
         (usuario == "🖐️" and computador == "👊") or \
         (usuario == "✌️" and computador == "🖐️"):
        st.balloons()  # Pequena animação divertida
        st.success("Você venceu! 🎉")
    else:
        st.error("Computador venceu! 🤖")