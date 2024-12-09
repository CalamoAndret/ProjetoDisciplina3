from PIL import Image
import numpy as np

# Constantes
AREA_BRASIL_HECTARES = 851576700  # Área total do Brasil em hectares

# Função para calcular os dados da imagem
def analisar_imagem(caminho_imagem):
    # Carregar a imagem e converter para escala de cinza
    imagem = Image.open(caminho_imagem)
    imagem = imagem.convert("L")  # Converter para tons de cinza
    dados = np.array(imagem)      # Converter a imagem em array numpy

    # Contar os pixels
    total_pixels = dados.size
    pixels_sem_dados = np.sum(dados == 0)
    pixels_soja = np.sum(dados == 39)
    pixels_pastagem = np.sum(dados == 15)

    # Pixels relevantes (sem os sem dados)
    pixels_relevantes = total_pixels - pixels_sem_dados

    # Cálculo de áreas em hectares
    proporcao_soja = pixels_soja / pixels_relevantes
    proporcao_pastagem = pixels_pastagem / pixels_relevantes

    area_soja = proporcao_soja * AREA_BRASIL_HECTARES
    area_pastagem = proporcao_pastagem * AREA_BRASIL_HECTARES

    # Resultados
    return {
        "total_pixels": total_pixels,
        "pixels_sem_dados": pixels_sem_dados,
        "pixels_soja": pixels_soja,
        "pixels_pastagem": pixels_pastagem,
        "area_soja_hectares": area_soja,
        "area_pastagem_hectares": area_pastagem,
    }

caminho_imagem = "Im_satelite.jpg"

resultado = analisar_imagem(caminho_imagem)

# Exibir os resultados
print("Resultados da Análise:")
print(f"Total de Pixels: {resultado['total_pixels']}")
print(f"Pixels sem Dados (Código 0): {resultado['pixels_sem_dados']}")
print(f"Pixels de Soja (Código 39): {resultado['pixels_soja']}")
print(f"Pixels de Pastagem (Código 15): {resultado['pixels_pastagem']}")
print(f"Área de Soja (hectares): {resultado['area_soja_hectares']:.2f}")
print(f"Área de Pastagem (hectares): {resultado['area_pastagem_hectares']:.2f}")
