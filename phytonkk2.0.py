import streamlit as st 
st.title('Calculadora de Combustível ⛽')
st.subheader('Gasolina x Etanol 🤑💸 ')
# ctrl + S   salvar
gasolina = st.number_input('Digite o valor da Gasolina 🦖', min_value = 0.0)
etanol = st.number_input('Digite o valor do Etanol 🍀', min_value = 0.0 )

if gasolina >0:
    resultado = etanol/gasolina
    if resultado < 0.70:
      msg = 'Abastece com Etanol pae 😎🤙'
    else:
       msg = 'Abastece com Gasolina ent vampeta 🤨🫳'
else:
   st.warning("Digite um valor acima de 0")   

if st.button('Calcular'):
   st.info(msg)


