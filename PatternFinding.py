#!/usr/bin/python
import os
import argparse

def read_file(path):
    string = ""
    f = open(path)
    for c in f.read():
        if c != '\n':
            string += c
    return string


def read_directory(path):
    extension = "txt"
    list_of_files = [file for file in os.listdir(path) if file.lower().endswith(extension)]
    return list_of_files


def chunk(string, size):
    chunks = []
    for i in range(0, len(string), size):
        chunks.append(string[i:i+size])
    return chunks


def count_pattern(string, block_size): #may be optimized
    counter=0
    chunks = chunk(string, block_size)
    while len(chunks) != 0:
        pattern = chunks.pop(0)

        matches = 0 #amount of matches for the current pattern
        for i in range(len(chunks)):
            if chunks[i] == pattern:
                matches += 1

        counter += matches
        for i in range(matches):
            chunks.remove(pattern)

    return counter




parser = argparse.ArgumentParser(description="Recebe como parametro um diretorio, o script pega cada arquivo de texto neste diretorio e transfotma em uma string, cada string e dividida em blocos de 4, 6 e 8 caracteres. Depois o script conta a ocorrencia de repeticoes deste bloco na string que foi dividida. Isto e feito para cada arquivo com extensao txt no diretorio, o resultado final e a soma de repeticoes")
parser.add_argument('-d','--directory', help='diretorio contendo os arquivos',required=True)
args = parser.parse_args()

directory = args.directory

total = 0
directories = read_directory(directory)
for path in directories:
    block_sizes=[4, 8, 16,]
    for size in block_sizes:
        total+=count_pattern(read_file(directory+os.sep+path), size)
print total


