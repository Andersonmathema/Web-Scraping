import streamlit as st
from json import loads
from pandas import read_csv

st.markdown('''
# Exibidor de arquivos
            
## Suba um arquivo e vejamos o que acontece 😆❤️
''')

arquivo = st.file_uploader(
    'Suba seu arquivo aqui!',
    type=['jpeg','png', 'py','wav', 'mp3', 'mp4', 'csv', 'json']
)
if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'application', 'json':
            st.json(loads(arquivo.read()))
        case 'image', _:
            st.image(arquivo)
        case 'text', 'csv':
            df = read_csv(arquivo)
            st.dataframe(df)
            st.line_chart(df)
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
        case 'audio',_:
            st.audio(arquivo)
        case 'video', 'mp4':
            st.video(arquivo)
else:
    st.error('Ainda não tenho arquivo!')