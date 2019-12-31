Fila1=[]
print("digite la cantidad de platos")
N = int(input())
for i in range(N):
    print("ingrese alguno de estos comandos:")
    print("a. Agregar plato al lavabo")
    print("b. Agregar lavar plato")
    print("c. Listar platos en la pila")
    inst = input()
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
        print(f'platos en el lavabo{Fila1}' )
        N+=1
