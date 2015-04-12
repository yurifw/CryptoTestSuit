# CryptoTestSuit

StrictAvalancheCriterion
========================
Para usar, substitua a variável tested_sbox com a sbox que você deseja testar. No momento este script funciona apenas para s-boxes 8x8 e que funcionem como a do AES (4 primeiros bits definem a linha e os 4 últimos definem a coluna).

Nonlinearity
============
Para utilizar o script, troque a váriavel chamada s\_box, coloque o valor correto para as váriaveis entry\_size e output\_size e implemente corretamente a função subbytes, que deve receber como parametro a entrada da s-box e deve retornar a saída da s-box. Este script depende do pacote bitarray.
