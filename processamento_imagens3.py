import numpy as np
import cv2

def convolucao(img, kernel):

    k= kernel
    
    

    output = cv2.filter2D(img, -1, k)
    imagem =output
    return imagem


def cinza(ima):
    imagem_cinza = np.copy(ima)
    for i in range(imagem_cinza.shape[0]):
        for j in range(imagem_cinza.shape[1]):
            verme =int( imagem_cinza[i, j, 0])
            verde = int(imagem_cinza[i, j, 1])
            azul = int( imagem_cinza[i, j, 2]) 
            media=(verme + verde + azul) / 3
            imagem_cinza[i, j, 0] = media
            imagem_cinza[i, j, 1] = media
            imagem_cinza[i, j, 2] = media
    return imagem_cinza


def limiar(ima, valor):
    imagem_cinza = np.copy(ima)
    
    def limit_2(x, valor):
        if x < valor:
            return 0
        elif x > valor:
            return 255
        else:
            return x

   
    for i in range(imagem_cinza.shape[0]):
        for j in range(imagem_cinza.shape[1]):   
                        imagem_cinza[i, j, 0] = limit_2(imagem_cinza[i,j, 0], valor)
                        imagem_cinza[i, j, 1] = limit_2(imagem_cinza[i,j, 1],valor)
                        imagem_cinza[i, j, 2] = limit_2(imagem_cinza[i,j, 2], valor)
    return imagem_cinza
    


def multiplicacao(imagem, valor):

    def limit(x):
        if x < 0:
            return 0
        elif x > 255:
            return 255
        else:
            return x



    imagem_mais_clara = np.copy(imagem)

                # esse loop soma 70 nos valores de todos os pixels. Como os
                # valores dos pixels vao ficar maiores (mais proximos de 255), 
                # a imagem resultante sera mais clara.
                
    for i in range(imagem_mais_clara.shape[0]):
        for j in range(imagem_mais_clara.shape[1]):
            imagem_mais_clara[i, j, 0] = limit(imagem[i, j, 0] * valor)
            imagem_mais_clara[i, j, 1] = limit(imagem[i, j, 1] * valor)
            imagem_mais_clara[i, j, 2] = limit(imagem[i, j, 2] * valor)
        imagem = imagem_mais_clara
    return imagem

