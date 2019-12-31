Fila1=[]
Fila2=[]
print("digite la cantidad de personas")
N = int(input())
for i in range(N):
    print("ingrese alguno de estos comandos:")
    print("a. Agregar cliente a fila de depósito")
    print("b. Agregar cliente a fila de apertura de cuenta")
    print("c. Atender cliente")
    print("d. Listar clientes en fila")
    inst = input()
    if inst[0] == 'a' or inst[0] == 'A':
        valor = input("ingrese algun valor")
        Fila1.append(valor)
        print("usuario agregado a fila de depósito")
    elif inst[0] == 'b' or inst[0] == 'B' :
        valor = input("ingrese algun valor")
        Fila2.append(valor)
        print("usuario agregado a fila de apertura de cuenta")
    elif inst[0] == 'c' or inst[0] == 'C' :
        if 0 == len(Fila1) and 0 == len(Fila2):
            print("Ya no quedan clientes que atender")
            break
        elif 0 == len(Fila1) and 0<len(Fila2):
            while 0<len(Fila2):
                print("usuario atendido "+Fila2[0]) 
                Fila2.pop(0)       
            print("Ya no quedan clientes que atender")
            break
        elif 0<len(Fila1) and 0 ==len(Fila2):
            while 0<len(Fila1):
                print("usuario atendido "+Fila1[0]) 
                Fila1.pop(0)       
            print("Ya no quedan clientes que atender")
            break
        elif 0 < len(Fila1) and 0 < len(Fila2):
            while 0<10:
                if 0<len(Fila1):
                    print("usuario atendido "+Fila1[0]) 
                    Fila1.pop(0)
                elif 0<len(Fila2):
                    print("usuario atendido "+Fila2[0]) 
                    Fila2.pop(0)
                else:
                    print("Ya no quedan clientes que atender")
                    break
            break
                    
    elif inst[0] == 'd' or inst[0] == 'D' :
        print(f'usuarios que estan en deposito {Fila1} y usuarios que estan en apertura de cuenta {Fila2}' )
        N+=1
