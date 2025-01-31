import random
import numpy as np
populacao = [5.0, 3.9, 9.8, 3.7, 1.9, 10.0, 8.1, 7.9, 7.0, 5.8, 2.9, 3.1, 2.2, 1.1, 1.7, 9.4, 9.5, 10.0, 9.9, 9.8, 3.8, 6.9, 6.7, 9.4, 0.1, 0.5, 0.6, 0.1, 0.0, 0.3, 0.4]
amostra = []

def amostra_aleatoria(populacao):
    tamanho_pop = len(populacao)
    amostra = random.sample(populacao, tamanho_pop//2)
    return amostra

def amostra_estratificada(populacao):
    um_cinco = []
    cinco_dez = []
    for i in populacao:
        if i <= 5.0:
            um_cinco.append(i)
        else:
            cinco_dez.append(i)
    #aqui fazemos a divisao da populacao em dois estratos de 1-5 e de 5.1-10
    print(f"Estrato de 1-5  {um_cinco}")
    print(f'Estrato de 5.1-10  {cinco_dez}')
    #agora chamamos a amostragem aleatoria para cada lista que criamos
    amostra_um_cinco = amostra_aleatoria(um_cinco)
    amostra_cinco_dez = amostra_aleatoria(cinco_dez)
    amostra_estratificada = amostra_um_cinco + amostra_cinco_dez
    return amostra_estratificada

def verifica_vies(populacao, amostra):
    media_populacao = np.mean(populacao)
    media_amostra = np.mean(amostra)

    vies = media_amostra = media_populacao
    return vies
    
amostragem_aleatoria_resultado = amostra_aleatoria(populacao)
amostragem_estratificada_resultado = amostra_estratificada(populacao)

print(f"Resultado da amostra aleatoria: {amostragem_aleatoria_resultado}\n")
print(f"Resultado da amostra estratificada: {amostragem_estratificada_resultado}\n")
print("-------------------------------------------")
print(f'Vies da amostra aleatoria: {verifica_vies(populacao, amostragem_aleatoria_resultado)}\n')
print(f'Vies da amostra estratificada: {verifica_vies(populacao, amostragem_estratificada_resultado)}\n')


