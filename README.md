# Extrator_CTe

Este projeto tem como obbjetivo principal o desenvolvimento de uma aplicação em Python capaz de extrair automaticamente informações relevantes de documentos de **Conhecimento de Transporte Eletrônico** (CT-e) em formato PDF. O projeto possui fins didáticos, servindo como um estudo prático de manipulação de PDFs, extração de texto estruturado e automação de tarefas rotineiras no transporte e logística.

# Objetivos
 - Automatizar a leitura de arquivos PDF de CT-es.
 - Extrair dados chave.
 - Armazenar e estruturar dados para análise.

# Aspectos Técnicos
 - Linguagem: Python 3.10+
 - Bibliotecas utilizadas:
    - pdfplumber – para leitura de PDFs.
    - re – expressões regulares para identificar padrões como CNPJ, datas, valores.
    - Biblioteca para armazenamento ainda a ser discutida.
  

# Funcionalidades
 - Nomes do remetente e destinatario
 - Origem e destino
 - CPF/CNPJ das partes
 - Valor do serviço (frete)
 - Data de emissão
 - Placa do veiculo
 - Chave de acesso do CT-e

# Observações
Este projeto assume que os PDF's de entrada são gerados digitalmente com texto acessível via **pdfplumber**.
