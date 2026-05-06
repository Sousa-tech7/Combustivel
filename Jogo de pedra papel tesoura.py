import streamlit as st 
st.title('Jogo de Pedra Papel Tesoura')

itens = ["👊", "🖐️", "✌️"]
import random 
usuario = input("Escolha 👊 (pedra), 🖐️ (papel) ou ✌️ (tesoura): ")
computador = random.choice(itens)

print(f"\nVocê escolheu: {usuario}")
print(f"Computador escolheu: {computador}")

if usuario == computador:
    print("Empate!!")

elif (usuario == "👊" and computador == "✌️") or \
     (usuario == "🖐️" and computador == "👊") or \
     (usuario == "✌️" and computador == "🖐️"):
    print("Você venceu! 🎉")

elif usuario not in itens:
    print("Escolha inválida! ❌")

else:
    print("Computador venceu! 🤖")