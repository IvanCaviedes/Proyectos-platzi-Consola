Fila1=[]
while True:
    inst = str(input('''
    ¿Que desea hacer?
    
    a. Agregar plato al lavabo
    b. Agregar lavar plato
    c. Listar platos en la pila
    '''))
    if inst[0] == 'a' or inst[0] == 'A':
        valor = input("ingrese algun valor")
        Fila1.append(valor)
        print("Plato agregado al lavaplatos")
    elif inst[0] == 'b' or inst[0] == 'B' :
        if 0 == len(Fila1):
            print("Ya no quedan platos")
            break
        elif 0 < len(Fila1):
            while 0<len(Fila1):
                print("plato lavado "+Fila1[-1]) 
                Fila1.pop(-1)       
            print("Ya no quedan platos")
            break
    elif inst[0] == 'c' or inst[0] == 'C' :
        for k in Fila1:
            print(f'el plato {k} queda en el lavabo')
