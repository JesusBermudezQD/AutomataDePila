class Grafo:

    def __init__(self):
        self.vertices=["p","q","r"]
        self.arcos=[]
        self.pila=["#"]
        self.verticeActual="p"
        self.aceptada=False
        #self.palabraValidar=palab+"λ"
        self.palabraValidar=""
        self.caminos=[]


    
    def agregarArco(self,arco):
        self.arcos=arco
    
    def verificar(self):

        for letra in self.palabraValidar:
            arcoGuardado = None

            print('nodo: ',self.verticeActual)
            print(letra) 
            for arco in self.arcos:
                if(self.verticeActual==arco.origen and letra==arco.palabra and self.pila[-1]==arco.desapilar):
                    arcoGuardado=arco
                    break 
                
            
            if(arcoGuardado!=None):

                if(arcoGuardado.palabra=="b" and arcoGuardado.desapilar=="b" and arcoGuardado.apilar=="bb"):

                    self.pila.pop()
                    for i in arcoGuardado.apilar:
                        self.pila.append(i)
               

                    print(self.pila)
                    self.caminos.append(arco)

                    self.verticeActual=arco.destino

                elif(arcoGuardado.palabra=="a" and arcoGuardado.desapilar=="b" and arcoGuardado.apilar=="ba"):

                    self.pila.pop()
                    for i in arcoGuardado.apilar:
                        self.pila.append(i)
                    
                    print(self.pila)
                    self.caminos.append(arco)

                    self.verticeActual=arco.destino

                elif(arcoGuardado.palabra=="b" and arcoGuardado.desapilar=="a" and arcoGuardado.apilar=="ab"):

                    self.pila.pop()
                    for i in arcoGuardado.apilar:
                        self.pila.append(i)

                    print(self.pila)
                    self.caminos.append(arco)

                    self.verticeActual=arco.destino

                elif(arcoGuardado.palabra=="a" and arcoGuardado.desapilar=="a" and arcoGuardado.apilar=="aa"):

                    self.pila.pop()
                    for i in arcoGuardado.apilar:
                        self.pila.append(i)
                    
                    print(self.pila)
                    self.caminos.append(arco)

                    self.verticeActual=arco.destino


                elif(arcoGuardado.palabra=="b" and arcoGuardado.desapilar=="#" and arcoGuardado.apilar=="#b"):

                    self.pila.pop()
                    for i in arcoGuardado.apilar:
                        self.pila.append(i)

                    print(self.pila)
                    self.caminos.append(arco)

                    self.verticeActual=arco.destino


                elif(arcoGuardado.palabra=="a" and arcoGuardado.desapilar=="#" and arcoGuardado.apilar=="#a"):

                    self.pila.pop()
                    for i in arcoGuardado.apilar:
                        self.pila.append(i)

                    print(self.pila)
                    self.caminos.append(arco)

                    self.verticeActual=arco.destino


                elif(arcoGuardado.palabra=="c" and arcoGuardado.desapilar=="#" and arcoGuardado.apilar=="#"):

                    self.pila.pop()
                    for i in arcoGuardado.apilar:
                        self.pila.append(i)

                    print(self.pila)
                    self.caminos.append(arco)

                    self.verticeActual=arco.destino

                
                elif(arcoGuardado.palabra=="c" and arcoGuardado.desapilar=="b" and arcoGuardado.apilar=="b"):

                    self.pila.pop()
                    for i in arcoGuardado.apilar:
                        self.pila.append(i)

                    print(self.pila)
                    self.caminos.append(arco)

                    self.verticeActual=arco.destino


                elif(arcoGuardado.palabra=="c" and arcoGuardado.desapilar=="a" and arcoGuardado.apilar=="a"):

                    self.pila.pop()
                    for i in arcoGuardado.apilar:
                        self.pila.append(i)

                    print(self.pila)
                    self.caminos.append(arco)

                    self.verticeActual=arco.destino

                elif(arcoGuardado.palabra=="b" and arcoGuardado.desapilar=="b" and arcoGuardado.apilar=="λ"):

                    self.pila.pop()
                    print(self.pila)
                    self.caminos.append(arco)
                    self.verticeActual=arco.destino
                
                elif(arcoGuardado.palabra=="a" and arcoGuardado.desapilar=="a" and arcoGuardado.apilar=="λ"):

                    self.pila.pop()
                    print(self.pila)
                    self.caminos.append(arco)
                    self.verticeActual=arco.destino


                elif(arcoGuardado.palabra=="λ" and arcoGuardado.desapilar=="#" and arcoGuardado.apilar=="#" and self.pila[-1]=="#"):
                    
                        self.pila.pop()
                        for i in arcoGuardado.apilar:
                            self.pila.append(i)

                        print(self.pila)
                        self.caminos.append(arco)

                        self.verticeActual=arco.destino

            else:
                print("La palabra no es aceptada en el lenguaje")
                self.caminos.append(arco)
                break
                
                
        if(self.verticeActual=="r"):
            self.aceptada=True
            print(self.verticeActual)
            print("aceptada")
            for camino in self.caminos:
                print(camino.origen,camino.destino,camino.palabra,camino.desapilar,camino.apilar)

        else:
            self.aceptada=False
            for camino in self.caminos:
                print(camino.origen,camino.destino,camino.palabra,camino.desapilar,camino.apilar)


    def iniciarGrafo(self,palabra):

        listarcos=[ Arco("p","p","b","b","bb"),
                    Arco("p","p","a","b","ba"),
                    Arco("p","p","a","a","aa"),
                    Arco("p","p","b","a","ab"),
                    Arco("p","p","b","#","#b"),
                    Arco("p","p","a","#","#a"),
                    Arco("p","q","c","#","#"),
                    Arco("p","q","c","b","b"),
                    Arco("p","q","c","a","a"),
                    Arco("q","q","b","b","λ"),
                    Arco("q","q","a","a","λ"),
                    Arco("q","r","λ","#","#") ]

        self.palabraValidar = palabra+"λ"
        self.agregarArco(listarcos)



class Arco():

    def __init__(self,origen,destino,palabra,desapilar,apilar):
        
        self.destino=destino
        self.origen=origen
        self.palabra=palabra
        self.desapilar=desapilar
        self.apilar=apilar

