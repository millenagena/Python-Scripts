seq = input('Digite a sequência: ')
arq = open('seq1.txt', 'w')
arq.write('>seq\n')
arq.write(seq)
arq.close()