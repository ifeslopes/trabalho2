# Trabalho2
Técnica de programação processamento de imagem com opencv

### Especificação
O trabalho consiste em desenvolver um programa para processamento de imagens. A entrada do
programa é um arquivo chamado “config.txt” contendo o nome da imagem de entrada, o nome da
imagem de saída, e a lista de operações que devem ser realizadas na imagem.
O programa deve implementar as seguintes operações:
• Multiplicar: as intensidades de cor dos pixels são dadas pela multiplicação dos valores
originais por uma constante utilizada como entrada. Essa função será escrita no arquivo de
configuração como multiplicar <valor> (exemplo: multiplicar 2).
• Transformar para tons de cinza: as intensidades dos pixels são dadas pela média dos 3 canais
de cor. Essa função será escrita no arquivo de configuração como cinza.
• Máscara de limiar: essa operação só pode ser realizada com imagens em tons de cinza. Os
pixels são representados como branco se a cor estiver acima de um valor usado como
entrada. Caso contrário, o pixel é marcado como preto. Essa função será escrita no arquivo
de configuração como limiar <valor> (exemplo: limiar 200).
• Convolução: a imagem de saída é obtida pela convolução da imagem de entrada por um
kernel utilizado como entrada. Essa função será escrita no arquivo de configuração como
convolucao <numero de linhas do kernel> <numero de colunas do kernel> e nas linhas
seguintes, o kernel (veja exemplo 4 abaixo). 
  
##  Regras
• As funções abaixo devem ser implementadas em uma biblioteca chamada
processamento_imagens.py. IMPORTANTE: As funções devem ser implementadas usando
manipulação de matrizes do numpy. Não é permitido usar funções prontas que já fazem as
operações.
o convolucao(imagem, kernel) : a função recebe como entrada uma imagem e um
kernel e gera como saída outra imagem que é o resultado da convolução.
o multiplicacao(imagem, valor) : a função recebe como entrada uma imagem e um valor
e gera como saída outra imagem que é o resultado da multiplicação dos pixels da
imagem pelo valor.
o limiar(imagem, valor) : a função recebe como entrada uma imagem em tons de cinza
(1 canal) e um valor e gera como saída outra imagem cujos pixels são brancos se o
pixel da imagem original for maior que o valor, e preto caso contrário.
o cinza(imagem): a função recebe como entrada uma imagem colorida e retorna a
imagem em tons de cinza.
• Deve ser escrita uma função main que contém o programa principal. Essa função deve estar
em um arquivo chamado programa.py .
• Os alunos podem criar outras bibliotecas e funções se acharem conveniente.
Convolução: a convolução recebe como entrada uma imagem e uma matriz chamada de kernel. Os
pixels da imagem de saída são obtidos realizando a multiplicação ponto a ponto do kernel com uma
parte da imagem de mesmo tamanho do kernel e, em seguida, somando os valores. Na Fig. 1
(abaixo), o pixel azul da imagem da direita é obtido fazendo a multiplicação ponto a ponto entre
kernel (a matriz 3x3 do meio) e a submatriz 3x3 marcada em azul na imagem da esquerda e
somando os valores (veja conta marcada em azul na parte de baixo da imagem). Como ilustrado na
Fig. 2, os demais pixels são obtidos “deslocando a posição” do kernel ao longo da imagem e
repetindo as operações de multiplicação ponto a ponto e soma. 
![imagem](https://github.com/ifeslopes/trabalho2/blob/master/Captura1.png)

![imagem](https://github.com/ifeslopes/trabalho2/blob/master/Captura2.png)

![imagem](https://github.com/ifeslopes/trabalho2/blob/master/capetura3.png)

![imagem](https://github.com/ifeslopes/trabalho2/blob/master/Captura%205.png)
