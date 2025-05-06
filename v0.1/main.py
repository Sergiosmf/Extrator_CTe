from extrator import CTEExtractor
import pandas as pd

def main():
    # Caminho para o PDF
    caminho_pdf = "/Users/sergiomendes/Documents/pdf/CT-e 000001068.pdf"

    # Instanciar a classe
    extrator = CTEExtractor(caminho_pdf)

    # Extrair os dados
    try:
        dados = extrator.extrair_tudo()
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        return

    # Exibir os resultados
    print("Dados extraídos:")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

    # (Opcional) salvar como CSV
    df = pd.DataFrame([dados])
    df.to_csv("/Users/sergiomendes/Documents/csv/resultado_cte.csv", index=False)
    

    print("\nArquivo 'resultado_cte.csv' gerado com sucesso.")

if __name__ == "__main__":
    main()
 