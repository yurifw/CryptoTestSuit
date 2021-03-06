#!/usr/bin/python
import random


input_size = 8 #em bits
output_size = 8 #em bits
sample_size = pow(2,8)  # tamanho maximo = 2 ^ input_size

def funcao_testada(plain_text):
    """Esta funcao deve receber como entrada um bit array e deve ter como saida um bit array, utilize a funcao to_bit_array para implementar mais facilmente"""
    tested_s_box = ((0x52, 0xf3, 0x7e, 0x1e, 0x90, 0xbb, 0x2c, 0x8a, 0x1c, 0x85, 0x6d, 0xc0, 0xB2, 0x1b, 0x40, 0x23),
     (0xf6, 0x73, 0x29, 0xd9, 0x39, 0x21, 0xcf, 0x3d, 0x9a, 0x8a, 0x2f, 0xcf, 0x7b, 0x04, 0xe8, 0xc8),
     (0x85, 0x7b, 0x7c, 0xaf, 0x86, 0x2f, 0x13, 0x65, 0x75, 0xd3, 0x6d, 0xd4, 0x89, 0x8e, 0x65, 0x05),
     (0xea, 0x77, 0x50, 0xa3, 0xc5, 0x01, 0x0b, 0x46, 0xbf, 0xa7, 0x0c, 0xc7, 0x8e, 0xf2, 0xb1, 0xcb),
     (0xe5, 0xe2, 0x10, 0xd1, 0x05, 0xb0, 0xf5, 0x86, 0xe4, 0x03, 0x71, 0xa6, 0x56, 0x03, 0x9e, 0x3e),
     (0x19, 0x18, 0x52, 0x16, 0xb9, 0xd3, 0x38, 0xd9, 0x04, 0xe3, 0x72, 0x6b, 0xba, 0xe8, 0xbf, 0x9d),
     (0x1d, 0x5a, 0x55, 0xff, 0x71, 0xe1, 0xa8, 0x8e, 0xfe, 0xa2, 0xa7, 0x1f, 0xdf, 0xb0, 0x03, 0xcd),
     (0x08, 0x53, 0x6f, 0xb0, 0x7f, 0x87, 0x8b, 0x02, 0xB1, 0x92, 0x81, 0x27, 0x40, 0x2e, 0x1a, 0xee),
     (0x10, 0xca, 0x82, 0x4f, 0x09, 0xaa, 0xc7, 0x55, 0x24, 0x6c, 0xE2, 0x58, 0xbc, 0xe0, 0x26, 0x37),
     (0xed, 0x8d, 0x2a, 0xd5, 0xed, 0x45, 0xc3, 0xec, 0x1c, 0x3e, 0x2a, 0xb3, 0x9e, 0xb7, 0x38, 0x82),
     (0x23, 0x2d, 0x87, 0xea, 0xda, 0x45, 0x24, 0x03, 0xe7, 0x19, 0xe3, 0xd3, 0x4e, 0xdd, 0x11, 0x4e),
     (0x81, 0x91, 0x91, 0x59, 0xa3, 0x80, 0x92, 0x7e, 0xdb, 0xc4, 0x20, 0xec, 0xdb, 0x55, 0x7f, 0xa8),
     (0xc1, 0x64, 0xab, 0x1b, 0xfd, 0x60, 0x05, 0x13, 0x2c, 0xa9, 0x76, 0xa5, 0x1d, 0x32, 0x8e, 0x1e),
     (0xc0, 0x65, 0xcb, 0x8b, 0x93, 0xe4, 0xae, 0xbe, 0x5f, 0x2c, 0x3b, 0xd2, 0x0f, 0x9f, 0x42, 0xcc),
     (0x6c, 0x80, 0x68, 0x43, 0x09, 0x23, 0xc5, 0x6d, 0x1d, 0x18, 0xbd, 0x5e, 0x1b, 0xB4, 0x85, 0x49),
     (0xbc, 0x0d, 0x1f, 0xa6, 0x6b, 0xd8, 0x22, 0x01, 0x7a, 0xc0, 0x55, 0x16, 0xb3, 0xcf, 0x05, 0x00))
    row = pow(2,0)*plain_text[3] + pow(2,1)*plain_text[2] + pow(2,2)*plain_text[1] + pow(2,3) * plain_text[0]
    col = pow(2,0)*plain_text[7] + pow(2,1)*plain_text[6] + pow(2,2)*plain_text[5] + pow(2,3) * plain_text[4]
    result = []*1
    result.append(tested_s_box[row][col])
    return to_bit_array(result)


def test():
    qtd_0, qtd_1 = (0, 0)
    for i in range(sample_size):
        X = [] * (input_size+1)  # X[0] eh a entrada original, os outros diferem de X[0] apenas em 1 bit
        Y = [] * (output_size+1) # Y[0] eh a saida da funcao recebendo x[0] como entrada e por ai vai
        V = [] * output_size

        #X.append( to_bit_array ([random.randint(0,255) for r in xrange(input_size/8)])) #gerou uma sequencia de bits aleatoria, do tamanho da entrada, X[0] e a entrada padrao que sera testada
        array = [] #se quiser gerar aleatoriamente, apagar esta linha e descomentar a linha acima
        array.append(i)   #se quiser gerar aleatoriamente, apagar esta linha tb
        X.append( to_bit_array (array))  #se quiser gerar aleatoriamente, apagar esta linha tb
        Y.append(funcao_testada(X[0]))

        for j in range(input_size):
            X.append(X[0][:]) #o [:] serve para passar a lista por valor, e nao por referencia
            X[-1][len(X)-2] ^= 1 # preparando X0 a X8 (X0 eh a entrada sendo testada, Xi eh o bit alterado
            Y.append(funcao_testada(X[j+1]))#Y[i+1] = funcao_testada(X[i+1])
            V.append(xor(Y[0], Y[j+1]))

        #print "\n"
        for i in range(len(V)):
            for j in range(len(V[0])):
                if V[i][j] == 1: qtd_1 += 1
                else: qtd_0 += 1
    result = float(qtd_1) / float((qtd_0 + qtd_1))
    print "SAC: %0.9f" % result



def to_bit_array(array):
    def bitfield(n, min_size):
        return [1 if digit == '1' else 0 for digit in bin(n)[2:].zfill(min_size)] # [2:] to chop off the "0b" part
    result = []
    for i in range(len(array)):
        result.extend(bitfield(array[i], 8))
    return result

def bit_array_2_decimal(bitarray):
    array = [0] * (len(bitarray)/8)

    for i in range(0,len(bitarray),8):
        decimal = pow(2,7)*bitarray[i] + pow(2,6)*bitarray[i+1] + pow(2,5)*bitarray[i+2] + pow(2,4)*bitarray[i+3] + pow(2,3)*bitarray[i+4] + pow(2,2)*bitarray[i+5]  + pow(2,1)*bitarray[i+6] + pow(2,0)*bitarray[i+7]
        array[i/8] = decimal
    return array

def xor(a, b):
    if len(a) != len(b): raise IndexError
    result = [None] * len(a)
    for i in range(len(a)):
        result[i] = a[i] ^ b[i]
    return result

test()
