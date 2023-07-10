import streamlit as st
from ftplib import FTP

# Configurações do servidor FTP
FTP_HOST = 'ftp.i4btech.com.br'
FTP_USER = 'pedro@i4btech.com.br'
FTP_PASS = 'class@003'

def listar_arquivos_ftp(diretorio):
    ftp = FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)

    # Navega para o diretório desejado
    ftp.cwd(diretorio)

    # Obtém a lista de arquivos e diretórios no diretório atual
    arquivos = []
    pastas = []
    ftp.retrlines('LIST', lambda x: arquivos.append(x.split()[-1]) if x.startswith('-') else pastas.append(x.split()[-1]))

    # Fecha a conexão FTP
    ftp.quit()

    return arquivos, pastas

def baixar_arquivo_ftp(arquivo, destino):
    ftp = FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)

    # Baixa o arquivo do servidor FTP
    with open(destino, 'wb') as file:
        ftp.retrbinary('RETR ' + arquivo, file.write)

    # Fecha a conexão FTP
    ftp.quit()

# Interface do Streamlit
st.title('Aplicativo FTP')


# Lista de arquivos e pastas
arquivos, pastas = listar_arquivos_ftp(diretorio_atual)

# Lista de pastas
st.write('Pastas:')
for pasta in pastas:
    if st.button(pasta):
        diretorio_atual = diretorio_atual.rstrip('/') + '/' + pasta
        arquivos, pastas = listar_arquivos_ftp(diretorio_atual)

# Lista de arquivos
st.write('Arquivos:')
for arquivo in arquivos:
    if st.button(arquivo):
        destino = st.text_input('Destino do download', value=arquivo)
        if st.button('Confirmar download'):
            baixar_arquivo_ftp(arquivo, destino)
            st.write('Download concluído!')