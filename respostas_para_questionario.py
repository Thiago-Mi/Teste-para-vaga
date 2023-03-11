# 1) Observe o trecho de código abaixo:

# INDICE = 13
# SOMA = 0 
# K = 0

# enquanto K < INDICE faça

# {

# K = K + 1;

# SOMA = SOMA + K;

# }

# imprimir(SOMA);



# Ao final do processamento, qual será o valor da variável SOMA?

# SOMA será 91


# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def Fibonacci(numero):
    auxiliar = 0
    anterior_1 = 0
    anterior_2 = 1
    while auxiliar <= numero:
        anterior_1 = anterior_1 + anterior_2
        anterior_2 = anterior_1 + anterior_2
        if anterior_1 == numero or anterior_2 == numero:
            return "Numero pertence a sequência de Fibonacci"
        auxiliar = anterior_1
    return "Numero não pertence a sequência de Fibonacci"

Fibonacci(98)
# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;



# 3) Descubra a lógica e complete o próximo elemento:



# a) 1, 3, 5, 7, 9

# b) 2, 4, 8, 16, 32, 64, 128

# c) 0, 1, 4, 9, 16, 25, 36, 49

# d) 4, 16, 36, 64, 256

# e) 1, 1, 2, 3, 5, 8, 13

# f) 2,10, 12, 16, 17, 18, 19, 200



# 4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?



# IMPORTANTE:

# a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

# b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

# c) Explique como chegou no resultado.

# Ambos se encontram a mesma distancia de Ribeirão Preto já que eles estam no mesmo lugar, porém a conta é essa, o carro que sai de Ribeirão Preto RP = v1.t e o caminhão de franca  CF = 100 - v2.t, temos tempo de viagem como 100km/80km/h = 1,25h
# como ele perde tempo nos pedágios o v2 = 100/1,42 = 70,6km/h já que 1,25 + 5min = 1,42h, tendo o tempo igual teremos RP/v1 = CF-100/-v2 = 60,9km

# 5) Escreva um programa que inverta os caracteres de um string.


# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;


def inverter_string(palavra:str):
    palavraInversa = ""
    i=len(palavra)
    while i>0:
        palavraInversa= palavraInversa + palavra[i-1]
        i=i-1
    return print(palavraInversa)

inverter_string("palavra")