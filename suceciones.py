

def mostrar(indice,ecu):
    S=lambda n: eval(ecu)
    res=0
    for x in range(1,indice):
        try:
            res=S(x)
        except:pass
        print(f'{ecu.replace("n",str(x))}={res}')
        

class Mega_sucecion:
    def main(lista):
        lista=lista
        pendientes=[]
        Sucecion=[]
        count = 1
        #SEccion para hayar multiplicadoras
        for x in range(1,len(lista)):
            Sucecion.append(Mega_sucecion.Creadora(x,pendientes,lista[x]))

        #Seccion para hallar nueva pendiente
        for x in range(1,len(lista)):
            pendientes.append(Mega_sucecion.Hallar_pendiente(Sucecion, lista, pendientes,count,x))
            count +=1
        

        #Crear sucecion
        resultado = str(lista[0])
        for x in range(len(pendientes)):
            resultado = resultado +f'+ {str(pendientes[x])}*{Sucecion[x][0]}'
        
        #regresando lambda
        return resultado
        


    def Creadora(x,pendiente,valor):
        #variables
        M=1
        m2=0
        resultado=[]
        count=1
        #Creacion de multiplicadora: ∏(x-n)
        for n in range(1,x+1):
            resultado +=[f'(n-{n})']
            
        #retorna un vector 
        return ['*'.join(resultado)]

    def Hallar_pendiente(sucecion,lista,pendiente,pnt_evaluar,pos):
        #Comprobar si es el segundo
        ecuacion = f'{lista[pos]}-{lista[0]}'
        pnt_evaluar +=1
        #preparando ecuacion
        for x  in range(0,pos-1):
            ecuacion = ecuacion +f'-{pendiente[x]}*{sucecion[x][0]}'
        ecuacion =f'({ecuacion})/({sucecion[pos-1][0]})'

        #hayando pendiente y enviarla
        f = lambda n: eval(ecuacion)
        return f(pnt_evaluar)

    def mostrar(indice,ecu):
        S=lambda n: eval(ecu)
        res=0
        for x in range(1,indice):
            try:
                res=S(x)
            except:pass
            print(f'{ecu.replace("n",str(x))}={res}\n\n')   

        

S=Mega_sucecion.main([8041981,4051982,27052014,24072002,19092016])

def Inicion(n):
    buscar_sucecion =[]
    for x in range(n):
        buscar_sucecion.append(int(input(f"escribe el  numero para {x}: ")))
    #Buscar sucecion
    ecuacion = Mega_sucecion.main(buscar_sucecion)
    #Mostrar sucesion
    Mega_sucecion.mostrar(n,ecuacion)

if __name__ =="__main__":
    longi = int(int(input("Escribe el numeor de suceciones que queires meter: ")))
    Inicion(longi)
    
