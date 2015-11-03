# CryptoTestSuit

StrictAvalancheCriterion
========================
Para usar, implemente a função booleana que deseja testar no lugar da função funcao\_testada, alem disso altere os parametros tamanho\_entrada, tamanho\_saida e sample\_size

Nonlinearity
============
Para utilizar o script, troque a váriavel chamada s\_box, coloque o valor correto para as váriaveis entry\_size e output\_size e implemente corretamente a função subbytes, que deve receber como parametro a entrada da s-box e deve retornar a saída da s-box. Este script depende do pacote bitarray.

Resistance to Differential Cryptanalysis
========================================
Assim como o script para SAC, é necessário implementar a S-Box e alterar os parâmetros de tamanho de entrada e saída (em bits) da S-Box.

PatternFinding
==============
Utilizado para encontrar padrões no algoritmo de expansão de chaves. Recebe como parametro um diretório, o script pega cada arquivo de texto neste diretório e transfotma em uma string, cada string é dividida em blocos de 4, 6 e 8 caracteres. Depois o script conta a ocorrência de repetições deste bloco na string que foi dividida. Isto é feito para cada arquivo com extensão txt no diretorio, o resultado final é a soma de repetições
