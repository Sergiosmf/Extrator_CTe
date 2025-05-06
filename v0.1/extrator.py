import pdfplumber  
import re

class CTEExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = ""
        self.linhas = []

    def carregar_pdf(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            page = pdf.pages[0]
            self.text = page.extract_text() or ""
            self.linhas = self.text.splitlines() if self.text else []
    

    def extrair_remetente(self):
        match = re.search(r'REMETENTE\s+(.+?)\s+DESTINATÁRIO', self.text, re.DOTALL)
        return match.group(1).strip().upper() if match else "Remetente não encontrado"

    def extrair_chave_acesso(self):
        match = \
        re.search(r'(\d{4}\s\d{4}\s\d{4}\s\d{4}\s\d{4}\s\d{4}\s\d{4}\s\d{4}\s\d{4}\s\d{4}\s\d{4})', self.text) 
        return match.group(1) if match else "Chave de acesso não encontrada"

    def extrair_origem_destino(self):
        origem = destino = None
        for i, linha in enumerate(self.linhas):
            if "ORIGEM DA PRESTAÇÃO" in linha.upper() and i + 1 < len(self.linhas):
                trecho = ' '.join(self.linhas[i:i+3])
                cidades = re.findall(r'[A-Z][a-z]+ - [A-Z]{2}', trecho)
                if cidades:
                    origem = cidades[0]
            if "DESTINO DA PRESTAÇÃO" in linha.upper() and i + 1 < len(self.linhas):
                trecho = ' '.join(self.linhas[i:i+3])
                cidades = re.findall(r'[A-Z][a-z]+ - [A-Z]{2}', trecho)
                if cidades:
                    destino = cidades[-1]
        return origem or "Origem não encontrada", destino or "Destino não encontrada"
    
    def extrair_destinatario(self):
        match = re.search(r'DESTINATÁRIO\s+(.+?)\s+ENDEREÇO', self.text)
        return match.group(1).title().strip().upper() if match else "Destinatário não encontrado"

    def extrair_placa(self):
        match = re.search(r'PLACA[:\s]+([A-Z]{3}-[0-9A-Z]{4})', self.text)
        return match.group(1) if match else "Placa não encontrada"

    def extrair_valor_servico(self):
        match = re.search(r'VALOR TOTAL DO SERVIÇO\s*[:\s]*R?\$?\s*([\d\.,]+)', self.text)
        return match.group(1) if match else "Valor do serviço não encontrado"

    def extrair_data_emissao(self):
        match = re.search(r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}', self.text)
        return match.group(0) if match else "Data de emissão não encontrada"

    def extrair_cpf_cnpj_remetente_destinatario(self):
        # Extrai todos os CPFs e CNPJs do texto
        encontrados = re.findall(r'\d{3}\.\d{3}\.\d{3}-\d{2}|\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', self.text)

        # Segunda e terceira ocorrências são os que nos interessam
        cpf_cnpj_remetente = encontrados[1] if len(encontrados) > 1 else "Remetente não encontrado"
        cpf_cnpj_destinatario = encontrados[2] if len(encontrados) > 2 else "Destinatário não encontrado"

        return cpf_cnpj_remetente, cpf_cnpj_destinatario

    
    def extrair_tudo(self):
        self.carregar_pdf()
        origem, destino = self.extrair_origem_destino()
        remetente_doc, destinatario_doc = self.extrair_cpf_cnpj_remetente_destinatario()
        return {
            "CHAVE_ACESSO": self.extrair_chave_acesso(),
            "REMETENTE": self.extrair_remetente(),
            "CPF/CNOJ REMETENTE": remetente_doc,
            "ORIGEM": origem,
            "DESTINO": destino,
            "DESTINATARIO": self.extrair_destinatario(),
            "CPF/CNPJ DESTINATARIO": destinatario_doc,
            "PLACA": self.extrair_placa(),
            "VALOR_SERVICO": self.extrair_valor_servico(),
            "DATA_EMISSAO": self.extrair_data_emissao()
        }

    def __repr__(self):
        return f"CTEExtractor({self.pdf_path})"

# Classe CTEExtractor para extração de informações de arquivos PDF de \
# \ Conhecimento de Transporte Eletrônico (CT-e).
# Métodos:
#     __init__(pdf_path):
#         Inicializa a classe com o caminho do arquivo PDF.
#     carregar_pdf():
#         Carrega o texto da primeira página do PDF e o divide em linhas.
#     extrair_remetente():
#         Extrai o nome do remetente do CT-e com base em um padrão de texto.
#     extrair_chave_acesso():
#         Extrai a chave de acesso do CT-e com base em um padrão de texto.
#     extrair_origem_destino():
#         Extrai as cidades de origem e destino da prestação de serviço.
#     extrair_destinatario():
#         Extrai o nome do destinatário do CT-e com base em um padrão de texto.
#     extrair_placa():
#         Extrai a placa do veículo do CT-e com base em um padrão de texto.
#     extrair_valor_servico():
#         Extrai o valor total do serviço do CT-e com base em um padrão de texto.
#     extrair_data_emissao():
#         Extrai a data e hora de emissão do CT-e com base em um padrão de texto.
#     extrair_cpf_cnpj_remetente_destinatario():
#         Extrai os CPFs e CNPJs do remetente e destinatário do CT-e.
#     extrair_tudo():
#         Executa todos os métodos de extração e retorna um dicionário com os dados extraídos.
#     __repr__():
#         Retorna uma representação em string da classe, incluindo o caminho do arquivo PDF.
