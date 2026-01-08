Removedor de Fundo e Redimensionador de Imagens

Este script em Python automatiza o processo de remoção de fundo de imagens utilizando a API do remove.bg, além de redimensionar automaticamente as imagens processadas para um tamanho padrão.

É ideal para padronização de imagens de produtos, especialmente para uso em e-commerce, catálogos e marketplaces.

Funcionalidades

Seleção de pasta de entrada contendo imagens (.jpg, .jpeg, .png)

Seleção de pasta de saída para salvar as imagens processadas

Remoção automática do fundo das imagens via API remove.bg

Conversão e salvamento das imagens no formato PNG

Redimensionamento automático para 1200x1200 pixels

Processamento em lote de todas as imagens da pasta selecionada

Tratamento de erros e exibição de mensagens de status no console

Tecnologias Utilizadas

Python 3

requests – comunicação com a API

Pillow (PIL) – manipulação e redimensionamento de imagens

tkinter – seleção gráfica de arquivos e pastas

API remove.bg

Pré-requisitos

Python instalado

Instalação das dependências:

pip install requests pillow


Definir a variável de ambiente com sua chave da API do remove.bg:

Windows (PowerShell)
setx apiKey "SUA_API_KEY_AQUI"

Linux / macOS
export apiKey="SUA_API_KEY_AQUI"

Como Usar

Execute o script:

python script.py


Selecione a pasta de entrada com as imagens

Selecione a pasta de saída

O script irá:

Remover o fundo das imagens

Redimensioná-las para 1200x1200

Salvar o resultado na pasta de destino

Estrutura de Saída

As imagens são salvas no formato .png

Mantêm o nome original do arquivo

Fundo removido e dimensões padronizadas

Observações

Cada imagem processada consome créditos da API do remove.bg

Certifique-se de que sua chave de API está válida

O script processa apenas arquivos de imagem suportados

Exemplo de Uso

Indicado para:

Padronização de imagens de produtos

Criação de anúncios em marketplaces

Automatização do tratamento de imagens em lote