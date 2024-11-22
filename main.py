import os

# Função para listar arquivos XML em um diretório
def listar_arquivos_xml(caminho):
    arquivos_xml = []
    for arquivo in os.listdir(caminho):
        if arquivo.endswith(".xml"):
            arquivos_xml.append(arquivo)
    return arquivos_xml

# Função para manipular o nome do arquivo cancelado removendo "Cancelamento_110111" e os dois últimos caracteres
def manipular_nome_arquivo(nome_arquivo):
    nome_modificado = nome_arquivo.replace("Cancelamento_110111", "")
    # Remover os dois últimos caracteres (antes da extensão .xml)
    nome_modificado = nome_modificado[:-6] + ".xml"
    return nome_modificado

# Solicitar caminhos de pasta via input no CMD
def obter_caminho_pasta(tipo_pasta):
    return input(f"Digite o caminho da pasta com as notas {tipo_pasta}: ")

def main():
    # Solicitar os caminhos das pastas via CMD
    caminho_autorizadas = obter_caminho_pasta('autorizadas')
    caminho_canceladas = obter_caminho_pasta('canceladas')

    # Listar os arquivos XML de cada pasta
    arquivos_autorizadas = listar_arquivos_xml(caminho_autorizadas)
    arquivos_canceladas = listar_arquivos_xml(caminho_canceladas)

    # Exibir os arquivos encontrados
    print("Arquivos XML na pasta de notas autorizadas:")
    print(arquivos_autorizadas)

    print("\nArquivos XML na pasta de notas canceladas (antes de manipulação):")
    print(arquivos_canceladas)

    # Remover "Cancelamento_110111" e os dois últimos caracteres dos arquivos cancelados
    arquivos_canceladas_modificados = [manipular_nome_arquivo(arquivo) for arquivo in arquivos_canceladas]

    # Exibir os arquivos cancelados após a manipulação
    print("\nArquivos XML na pasta de notas canceladas (após remover 'Cancelamento_110111' e os dois últimos caracteres):")
    print(arquivos_canceladas_modificados)

    # Comparar e excluir arquivos autorizados correspondentes aos cancelados modificados
    for arquivo_cancelado in arquivos_canceladas_modificados:
        if arquivo_cancelado in arquivos_autorizadas:
            caminho_arquivo_autorizado = os.path.join(caminho_autorizadas, arquivo_cancelado)
            try:
                # Exclui o arquivo da pasta de notas autorizadas
                os.remove(caminho_arquivo_autorizado)
                print(f"Arquivo removido da pasta de notas autorizadas: {arquivo_cancelado}")
            except Exception as e:
                print(f"Erro ao tentar remover o arquivo {arquivo_cancelado}: {e}")

    print("Processo de exclusão concluído.")

if __name__ == "__main__":
    main()
