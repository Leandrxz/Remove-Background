Removedor de Fundo de Imagens

Script em Python desenvolvido para remover automaticamente o fundo de imagens utilizando a API do remove.bg, além de redimensionar os arquivos para um tamanho padrão.

Funcionalidade:

Remove o fundo de imagens (.jpg, .jpeg, .png)
Redimensiona as imagens para 1200x1200
Salva o resultado em formato PN
Processa várias imagens de uma pasta automaticamente

Tecnologias
Python
API remove.bg
Pillow (PIL)
Requests
Tkinter

Como usar
Execute o script
Selecione a pasta com as imagens
Selecione a pasta de saída
As imagens serão processadas automaticamente
Configuração da API

A chave da API do remove.bg deve ser armazenada em um arquivo .env, utilizando a variável:
apiKey=SUA_CHAVE_DE_API

Certifique-se de que o arquivo .env esteja configurado corretamente antes de executar o script.
