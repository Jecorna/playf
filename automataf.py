alfabeto = []
estados = []
aceptacion = []
aux = []
transicion = {}
#transicion = {("1","a"):"d", ("0","a"):"b", ("1","b"):"c", ("0","b"):"a", ("1","c"):"b", ("0","c"):"d", ("1","d"):"a", ("0","d"):"c"}
cadena = []
visitado = ' '

arch = open("atmta2.txt", "r")

for caracter in arch.readline():
    if(caracter != ','):
        if(caracter != '\n'):
            estados.append(caracter)

for caracter in arch.readline():
    if(caracter != ','):
        if(caracter != '\n'):
            alfabeto.append(caracter)

for caracter in arch.readline():
    if(caracter != ','):
        if(caracter != '\n'):
            aceptacion.append(caracter)

for caracter in arch.readline():
    if(caracter != ','):
        if(caracter != '\n'):
            visitado = caracter

for caracter in arch.readline():
    if(caracter != ','):
        if(caracter != '\n'):
            aux.append(caracter)

var1 = ""
var2 = ""
i = 0

for caracter in aux:
    if(i == 0):
        var1 = caracter
        i = i +1
    elif(i == 1):
        var2 = caracter
        i = i +1
    else:
        transicion[var1 , var2 ] = caracter
        i = 0
    
    
for caracter in arch.readline():
    if(caracter != ','):
        if(caracter != '\n'):
            cadena.append(caracter)
    
for entrada in cadena:
    visitado = transicion[entrada,visitado]
    print visitado
    
if(aceptacion,visitado):
    print "estado de aceptacion"

else:
    print "no aceptada"
