#!/usr/bin/env python3

#
# Title: Playfair Cipher by Monthly vel k1k9
# Description: Encyption and decryption Playfair cipher
# Date: 20.08.2021
#
import re
regex = re.compile(r'[a-ik-zA-IK-Z]')

def _generateTable(key):
    key = ''.join(dict.fromkeys(key.upper().replace("J","I").replace(" ","")))
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # without J
    for k in key: alphabet = alphabet.replace(k, '')
    alphabet = key+alphabet
    # Generating table 5x5 based on preparied alphabet
    table = []
    for row in range(5):
        table.append([])
        for column in range(5):
            index = 0 if row==0 and column==0 else index+1
            table[row].append(alphabet[index])
    return table

def _createBigrams(plaintext):
    plaintext = plaintext.upper().replace("J","I")
    bigrams = []
    bigram = ""

    for char in range(0, len(plaintext)+1):
        if len(bigram) == 2:
            bigrams.append(bigram)
            bigram = ""
        try:
            if regex.match(plaintext[char]):
                bigram += plaintext[char]
        except: pass
    
    if len(bigram) == 1: bigrams.append(bigram+"X")
    return bigrams

def encrypt(plaintext, key):
    table = _generateTable(key)
    bigrams = _createBigrams(plaintext)
    encrypted = ""

    for bigram in bigrams:
        # Find bigram in table
        for row in range(5):
            for column in range(5):
                if bigram[0] == table[row][column]: b0 = [row, column]
                if bigram[1] == table[row][column]: b1 = [row, column]
        
        # Playfair: bigram elements in same row
        if b0[0] == b1[0]:
            b0[1] = b0[1]+1 if b0[1]<4 else 0
            b1[1] = b1[1]+1 if b1[1]<4 else 0
            newBigram = table[b0[0]][b0[1]] + table[b1[0]][b1[1]] 
            encrypted += newBigram

        # Playfair: bigram elements in same column
        elif b0[1] == b1[1]:
            b0[0] = b0[0] + 1 if b0[0]<4 else 0
            b1[0] = b1[0] + 1 if b1[0]<4 else 0
            newBigram = table[b0[0]][b0[1]] + table[b1[0]][b1[1]] 
            encrypted += newBigram

        # Playfair: if bigram elements doesnt match to previous conditions
        else:
            oldb0 = b0[1]
            b0[1] = b1[1]
            b1[1] = oldb0
            newBigram = table[b0[0]][b0[1]] + table[b1[0]][b1[1]] 
            encrypted += newBigram
    
    # Created encrypted bigrams add to orginal message
    # skipping orginal alphabet characters
    fullEncrypted = ""
    index = 0
    for char in plaintext.upper():
        if regex.match(char):
            fullEncrypted += encrypted[index]
            index += 1
        else: fullEncrypted += char
    # Check is none one left
    if index == len(encrypted)-1:
        fullEncrypted += encrypted[index]
    return fullEncrypted

def decrypt(plaintext, key):
    table = _generateTable(key)
    bigrams = _createBigrams(plaintext)
    decrypted = ""

    for bigram in bigrams:
        # Find bigram in table
        for row in range(5):
            for column in range(5):
                if bigram[0] == table[row][column]: b0 = [row, column]
                if bigram[1] == table[row][column]: b1 = [row, column]

        # CTFLearn purpose: bigram elements are the same
        if bigram[0] == bigram[1]:
            row = b0[0]-1 if b0[0]>0 else 4
            column = b0[1]-1 if b0[1]>0 else 4
            decrypted += table[row][column] + table[row][column]
        
        # Playfair: bigram elements in same row
        elif b0[0] == b1[0]:
            b0[1] = b0[1]-1 if b0[1]>0 else 4
            b1[1] = b1[1]-1 if b1[1]>0 else 4
            newBigram = table[b0[0]][b0[1]] + table[b1[0]][b1[1]] 
            decrypted += newBigram

        # Playfair: bigram elements in same column
        elif b0[1] == b1[1]:
            b0[0] = b0[0] - 1 if b0[0]>0 else 4
            b1[0] = b1[0] - 1 if b1[0]>0 else 4
            newBigram = table[b0[0]][b0[1]] + table[b1[0]][b1[1]] 
            decrypted += newBigram

        # Playfair: if bigram elements doesnt match to previous conditions
        else:
            oldb0 = b0[1]
            b0[1] = b1[1]
            b1[1] = oldb0
            newBigram = table[b0[0]][b0[1]] + table[b1[0]][b1[1]] 
            decrypted += newBigram
    
    # Created decrypted bigrams add to orginal message
    # skipping orginal alphabet characters
    fulldecrypted = ""
    index = 0
    for char in plaintext.upper():
        if regex.match(char):
            fulldecrypted += decrypted[index]
            index += 1
        else: fulldecrypted += char
    # Check is none one left
    if index == len(decrypted)-1:
        fulldecrypted += decrypted[index]
    return fulldecrypted
