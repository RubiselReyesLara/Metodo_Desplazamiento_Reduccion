'''
################################################################## ######## ##### ### ##
METODO DE DESPLAZAMIENTO REDUCCION (MDR) en PILAS SEMANTICAS DE UN ANALIZADOR SEMANTICO#
## Este script pide una entrada W por ejemplo: x + x * (x + x). Donde se indica ### # ##
## y un conjunto de reglas como: E->E+E. Retorna la ejecución del algoritmo e   ### # ##
## indica si la cadena se acepta o no --------------------------------------------------
#### NOTA: Para indicar terminales con mas de un caracter colocarlo entre comilla doble,
#### por ejemplo: id -> "id" -----------------------------------------------------------
# ## AUTOR: Rubisel RL -----------------------------------------------------------------
################################################################## ######## ##### ### ##
'''
print('#################################### MDR ########################################')
# Declaracion de variables
reglas = list()
entrada_preparada = list()
pila = str()
iterador_regla = 0
accion = 'Desplazar'

#### Ingresar W y reglas
W = input('Ingrese la cadena de entrada W: ')
it_regla = 0
while True:
    it_regla += 1
    reglas.append(input('\nIngrese la regla de producción {0}:'.format(it_regla)))
    if input('¿Agregar otra regla? Presione cualquier tecla, si no, presione 1: ') == '1':
        break

#### Imprimir reglas
print('\n------------------------------------------------------------------------------\n',
      'Reglas:')
for regla in reglas:
    print(regla)
print('------------------------------------------------------------------------------\n')

# Valor crudo => E->E+E; Transformado a [E, E+E]
reglas_produccion = [[regla[:regla.find('>') - 1] for regla in reglas], # E
                     [regla[regla.find('>') + 1:] for regla in reglas]] # E+E

simbolo_inicial = reglas_produccion[0][0]
'''
################################################################## ######## ##### ### ###
GENERACION DE ENTRADA ###################################################################
################################################################## ######## ##### ### ###
'''
if '"' in W: #Si la cadena tiene terminales indicadas entre comillas dobles...
    index_W = 0 # Index de W
    indexes_comillas = 0 # Indicador de index para la lista de indexes de comillas W
    
    # Obtener indexes de cada comilla doble en W
    indexes_comillas_W = [index for index, caracter in enumerate(W) if caracter == '"']
    
    # Verificar que la entrada cruda tenga terminales definidas correctamente
    if len(indexes_comillas_W) % 2 != 0:
        print('Error en la cadena W. No cerro o abrio una variable con "')
        exit()
    
    while index_W < len(W):
        if W[index_W] == '"': # SI el caracter actual es una comilla doble...
            # Agrego a entrada_preparada todo aquel valor de W que se encuentre 
            # entre el index(n) y el index (n + 1) indicado en los indexes de ""
            entrada_preparada.append(W[indexes_comillas_W[indexes_comillas] + 1: 
                                    indexes_comillas_W[indexes_comillas + 1]]) 
            
            # El valor del index_W cambia al ultimo valor indicado en los indexes de ""
            index_W = indexes_comillas_W[indexes_comillas + 1] + 1 
            # Se suma 2, debido a que la lista de index de "" va indicando de dos en dos
            indexes_comillas += 2
        else:
            entrada_preparada.append(W[index_W])
            index_W += 1
else:
    entrada_preparada = [caracter for caracter in W]

'''
################################################################## ######## ##### ### ###
CALCULO MDR #############################################################################
################################################################## ######## ##### ### ###
'''
entrada_preparada.append('$') # Primer simbolo en la entrada, por regla inicial
print('| {:10} | {:^30} | {:^30} |'.format('Pila', 'Entrada', 'Accion'))

for index_caracter in range(-1, len(entrada_preparada) - 1): # Iteracion sobre la entrada
    pila += entrada_preparada[index_caracter] # Desplazamiento terminal de entrada actual
    print('| {:10} | {:^30} | {:^30} |'
          .format(pila, ''.join(entrada_preparada[index_caracter + 1 :]), accion))
    
    # Iterar sobre cada regla para verificar si la actual se encuentra en la pila, si se
    while iterador_regla < len(reglas_produccion[1]): # encuentra, se reemplaza
        if reglas_produccion[1][iterador_regla] in pila:
            accion = 'Reemplazar con {0}->{1}'.format(
                                                    reglas_produccion[0][iterador_regla], 
                                                    reglas_produccion[1][iterador_regla])
            print('| {:10} | {:^30} | {:^30} |'
                  .format(pila, ''.join(entrada_preparada[index_caracter + 1 :]), accion))
            
            pila = pila.replace(reglas_produccion[1][iterador_regla], 
                                reglas_produccion[0][iterador_regla])
            iterador_regla = 0 # Reiniciar si hay otra posibilidad de reduccion
        else:
            accion = 'Desplazar'
            iterador_regla += 1
    iterador_regla = 0

'''
################################################################## ######## ##### ### #
RESULTADO #############################################################################
################################################################## ######## ##### ### #
'''
if pila[1:] == simbolo_inicial:
    print('Se acepta la cadena W = ',W)
else:
    print('NO se acepta la cadena W = ',W)