#!/usr/bin/python
import itertools


s_box = s_box = ((0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76),
(0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0),
(0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15),
(0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75),
(0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84),
(0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF),
(0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8),
(0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2),
(0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73),
(0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB),
(0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79),
(0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08),
(0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A),
(0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E),
(0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF),
(0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16))


entry_size = 8
output_size = 8


def subbytes(byte):
    # definir aqui a sbox
    col = byte >> 4
    row = byte & 15
    return s_box[row][col]




def combinacoes(limite, qtd_variaveis):
    return itertools.combinations(range(1,limite+1), qtd_variaveis)

def bitfield(n, min_size):
    return [1 if digit=='1' else 0 for digit in bin(n)[2:].zfill(min_size)] # [2:] to chop off the "0b" part

def print_funcoes_lineares(n):
    """exibe na tela a saida de todas as funcoes lineares com n variaves de entrada"""
    funcoes = "\nFuncoes lineares para %i entradas (simbolo + representa ou exclusivo) \n0\n1\n" %n
    for i in range(1, n+1):
        for c in combinacoes(n,i):
            aux = ""
            for j in c:
                aux += "x%i "
            # print aux % c
            # print aux % c + "+1"
            funcoes += aux %c +"\n"
            funcoes += aux %c + "+1\n"
    print funcoes.replace(" x", " + x")
    # melhorias: colocar o index de cada saida, por exemplo f1 =  saida, f2 = saida


def sbox_truth_table(verbose):
    tt_rows = 2 ** entry_size  # numero de linhas da tabela verdade
    tt_cols = entry_size + output_size
    tt = [[0 for col in range(tt_cols)] for row in range(tt_rows)]
    for lin in range(tt_rows):
        tt[lin] = bitfield(lin, entry_size)
        tt[lin].extend(bitfield(subbytes(lin), output_size))
    if verbose:
        print "\nTabela verdade da SBOX\nxi para o i-esimo bit de entrada e yi para o i-esimo bit de saida\n"
        for i in range(len(tt[0])):
            if i < entry_size:
                print "x%i" % (i+1),
            else:
                print "y%i" % (i-entry_size+1),
        print ""
        for lin in range(len(tt)):
            for col in range(len(tt[0])):
                print "%i " % tt[lin][col],
            print ""
    return tt



def tt_vetores_lineares(n, verbose):
    """exibe na tela a tabela verdade para cada funcao linear"""
    truth_table = [[0 for col in range(2**(n+1))] for row in range(2**n)]  # iniciando a tabela com 0
    r = 0
    def funcao(array, indices):
        """esta funcao tem que receber como parametro um array de booleanos (1 ou 0) e um
        array que diga quais indices serao considerados. a funcao deve fazer um ou exclusivo com todos os indices considerados
        e retornar o resultado (ou 0 ou 1) """
        result = 0
        for i in indices:
            result ^= array[i-1]  # -1 pq o metodo combinacoes retorna sequencias que comecam do 1 ao inves do 0
        return result

    # tamanho dos vetores lineares :(2**n)
    # qtd de vetores lineares: 2**(n+1)
    for lin in range(len(truth_table)):
        truth_table[lin] = bitfield(lin, entry_size)
        truth_table[lin].append(0)          # adicionando linha referente a funcao 1, que tem como todas as saidas 0
        truth_table[lin].append(1)          # adicionando linha referente a funcao 2, que tem como todas as saidas 1
        for i in range(entry_size):
            for c in combinacoes(entry_size, i+1):   # +1 para executar uma iteracao com todas as variaveis
                r = funcao(truth_table[lin], c)
                truth_table[lin].append(r)
                truth_table[lin].append(r ^ 1)

    if verbose:
        print "\nTabela verdade das funcoes lineares\nxi para o i-esimo bit de entrada e fi para a i-esima funcao\n"
        for i in range(len(truth_table[0])):
            if i < entry_size:
                print "x{0:02d}".format(i+1),
            else:
                print "f{0:02d}".format(i-entry_size+1),
        print ""

        for lin in range(len(truth_table)):
            for col in range(len(truth_table[0])):
                print " %i " %truth_table[lin][col],
            print ""
    return truth_table;


def hamming_distance(a, b):
    # calcula a distancia de hamming entre o vetor a e o vetor b, ambos devem ter o mesmo tamanho e devem estar no formato de bitfield
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance+=1

    return distance


def rotate(matrix):
    return zip(*matrix[::1])


def nonlinearity(verbose):
    if verbose:
        print "S-box: (em hexadecimal)"
        for i in range(len(s_box)):
            for j in range(len(s_box[0])):
                print "{0:02x}".format(s_box[i][j]),
            print ""

    tt_sbox = sbox_truth_table(verbose)
    if verbose: print_funcoes_lineares(entry_size)
    tt_vetor_linear = tt_vetores_lineares(entry_size, verbose)

    vetores_verdade = rotate(tt_sbox)[entry_size:]
    vetores_lineares = rotate(tt_vetor_linear)[entry_size:]

    if verbose:
        print "\nVetores verdade:"
        for lin in range(len(vetores_verdade)):
            print "v%i =" % lin,
            for col in range(len(vetores_verdade[0])):
                print vetores_verdade[lin][col] ,
            print ""
        print "\nVetores lineares:"
        for lin in range(len(vetores_lineares)):
            print "v%i =" % (lin+1),
            for col in range(len(vetores_lineares[0])):
                print vetores_lineares[lin][col] ,
            print ""
    """ja obteve e imprimiu os dados necessarios para o calculo, agora deve-se calcular a menor distancia de hamming
    entre cada vetor verdade e todos os vetores lineares, o menor resultado e a nao linearidade"""
    result = 9999

    for i in range(len(vetores_verdade)):
        for j in range(len(vetores_lineares)):
            a = hamming_distance(vetores_verdade[i], vetores_lineares[j])
            if a < result : result = a
            

    print "\nNao linearidade: %i" %result

nonlinearity(True)
# print bitfield(subbytes(13),output_size)
