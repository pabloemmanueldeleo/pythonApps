import random
import os
import msvcrt
#c=msvcrt.getch()
bola8 = ['No se que decirte man.',
        'Loco preguntame otra cosa',
        'Sos un puto genio',
        'Que pashiooooo jake?',
        'Puede ser']

while True:

    x=raw_input("HAZME UNA PREGUNTA. \n")
    if x=="":
        '\n'
        print "seguire esperando..."
    elif x=='chau':
        print '\n'
        print 'CHAU NOS VEMOS\n'
        break
    else:
        print '--RESPUESTA: '+ random.choice(bola8)
        print '\n'
os.system("pause")