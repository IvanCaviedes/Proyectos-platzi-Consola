Fila1=[]
Fila2=[]
while True:
    inst = str(input('''
    ¿Que desea hacer?
    
    a. Agregar cliente a fila de depósito
    b. Agregar cliente a fila de apertura de cuenta
    c. Atender cliente
    d. Listar clientes en fila
    '''))
    if inst[0] == 'a' or inst[0] == 'A':
        valor = input("Ingrese Nombre del Cliente para agregar a depocito: ")
        Fila1.append(valor)
        print("usuario agregado a fila de depósito")
    elif inst[0] == 'b' or inst[0] == 'B' :
        valor = input("Ingrese Nombre del Cliente para agregar a apertura de cuenta: ")
        Fila2.append(valor)
        print("usuario agregado a fila de apertura de cuenta")
    elif inst[0] == 'c' or inst[0] == 'C' :
        if 0 == len(Fila1) and 0 == len(Fila2):
            print("Ya no quedan clientes que atender")
            break
        elif 0 == len(Fila1) and 0<len(Fila2):
            while 0<len(Fila2):
                print("usuario atendido fila de apertura de cuenta "+Fila2[0]) 
                Fila2.pop(0)       
            print("Ya no quedan clientes que atender")
            break
        elif 0<len(Fila1) and 0 ==len(Fila2):
            while 0<len(Fila1):
                print("usuario atendido fila de depósito "+Fila1[0]) 
                Fila1.pop(0)       
            print("Ya no quedan clientes que atender")
            break
        elif 0 < len(Fila1) and 0 < len(Fila2):
            while 0<10:
                if 0<len(Fila1):
                    print("usuario atendido fila de depósito "+Fila1[0]) 
                    Fila1.pop(0)
                elif 0<len(Fila2):
                    print("usuario atendido fila de apertura de cuenta "+Fila2[0]) 
                    Fila2.pop(0)
                else:
                    print("Ya no quedan clientes que atender")
                    break
            break         
    elif inst[0] == 'd' or inst[0] == 'D' :
        for k in Fila1:
            print(f'usuario {k} esta esperando en fila de depocito')
        for j in Fila2:
            print(f'usuario {j} esta esperando en fila de apertura de cuenta')

