#Ejercicio1

n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = f'tabla-{n}.txt'

with open(file_name,mode='w') as f:
    for i in range (1,13):
        f.write (f'{n} x {i} = {n*i}\n')


#Ejercicio 2

n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())


#Ejercicio 3

n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
else:
    lines = f.readlines()
    print(lines[m - 1])


#EXPRESIONES REGULARES

#1
from modulo import datos
import re
path = './data/re/short_tweets.csv'

s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
s





#2


s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
s

#3

analisis_sentimientos = datos.read_pandas(path,780,782)

for tweet in analisis_sentimientos:
    print(tweet)
    
    

#4



regex = r""

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    
    if re.match(regex, example):
        
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))   

        

