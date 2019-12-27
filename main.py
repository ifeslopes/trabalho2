import cv2
import numpy as np 
from processamento_imagens import *


def le_config(nome_arquivo):
    f = open(nome_arquivo, "r")
    linhas = f.readlines()
    f.close()
    return linhas


def le_kernel(operacoes, linha_cmd_conv):
    palavras = operacoes[linha_cmd_conv].rsplit()
            
    # le as dimensoes do kernel
    nl = int(palavras[1])
    nc = int(palavras[2])
    
    # faz o kernel receber uma matriz de zeros
    # com as dimensoes descritas no arquivo
    kernel = np.zeros((nl, nc))

    for y in range(nl):
        linha_kernel = operacoes[linha_cmd_conv + y + 1].rsplit()
        for x in range(nc):
            kernel[y, x] = float(linha_kernel[x])

    return nl, kernel


def executa_operacoes(imagem, operacoes):
    i = 0
    while i < len(operacoes):
        if "convolucao" in operacoes[i]:
            nl, kernel = le_kernel(operacoes, i)
            print('Operacao: Convolucao')
            print("kernel:")
            print(kernel)
            print()
            imagem = convolucao(imagem, kernel)
            # salta tantas linhas quanto o numero de linhas do kernel
            i += nl + 1
        else:
            if "cinza" in operacoes[i]:
                print('Operacao: cinza')
                imagem = cinza(imagem)
            else:
                # se nao for convolucao, nem cinza, entao sera multiplicacao ou limiar. Em ambos os
                # casos, vamos precisar quebrar a linha em 2 partes, o nome da operacao, e o valor.
                palavras = operacoes[i].rsplit()
                operacao = palavras[0]
                valor = float(palavras[1])
                
                if operacao == "multiplicar":
                    print('Operacao: multiplicar', valor)
                    imagem = multiplicacao(imagem, valor)
                else:
                    print('Operacao: limiar', valor)
                    imagem = limiar(imagem, valor)

            # vai para proxima linha tanto se a operacao for 
            # cinza, quanto se for multiplicacao ou limiar.
            i += 1

    return imagem


def main():
    # le linhas do arquivo de configuracao
    linhas = le_config("config.txt")
    
    # separa os nomes dos arquivos e as operacoes
    nome_imagem_entrada = linhas[0].rstrip()
    nome_imagem_saida = linhas[1].rstrip()
    operacoes = linhas[2:]

    # le imagem de entrada
    imagem_entrada = cv2.imread(nome_imagem_entrada)

    # executa operacoes listadas no arquivo config
    imagem_saida = executa_operacoes(imagem_entrada, operacoes)

    # salva imagem de saida
    cv2.imwrite(nome_imagem_saida, imagem_saida)
    #cv2.imshow("imagem", imagem)
    cv2.imshow("imagem", imagem_entrada)
    cv2.imshow(nome_imagem_saida, imagem_saida)
    cv2.waitKey(-1)



if __name__ == "__main__":
    main()