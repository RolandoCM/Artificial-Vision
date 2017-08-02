import csv
arch = open('entrenamiento.csv', 'w')

for k in xrange(0,2):
    archivo = open('descriptors/objeto'+str(k)+'.csv')
    for i in archivo:
        arch.writelines(i)
    archivo.close()
    print k


arch.close()
archivo.close()
