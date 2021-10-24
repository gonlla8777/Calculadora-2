
from PyQt5.QtWidgets import QInputDialog, QMainWindow, QApplication 
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Calculadora2.ui", self) #Nombre del archivo UI para conectar
        #variables
        self.operador1 = 0
       
        

        #BOTONES PARA DISPARAR UN EVENTO O METODO

        self.boton1.clicked.connect(self.click_1)
        self.boton2.clicked.connect(self.click_2)
        self.boton3.clicked.connect(self.click_3)
        self.boton4.clicked.connect(self.click_4)
        self.boton5.clicked.connect(self.click_5)
        self.boton6.clicked.connect(self.click_6)
        self.boton7.clicked.connect(self.click_7)
        self.boton8.clicked.connect(self.click_8)
        self.boton9.clicked.connect(self.click_9)
        self.boton0.clicked.connect(self.click_0)
        self.boton_punto.clicked.connect(self.click_punto)
        


        # BOTONES PARA OPERACIONES
        self.suma.clicked.connect(self.sumar)
        self.boton_resta.clicked.connect(self.resta)
        self.potencia.clicked.connect(self.Potencia)
        self.boton_raiz.clicked.connect(self.Raiz)
        self.boton_por.clicked.connect(self.multiplica)
        self.boton_division.clicked.connect(self.divide)
        self.igual.clicked.connect(self.resultado)
        self.boton_borratodo.clicked.connect(self.borratodo)
        
     
    #OPERACIONES METODOS
       
    def sumar(self):

        #si ya tiene asignado un operador, agregamos el otro con el mismo boton
        if(self.operador1 ==0):
            self.operador1 = float(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "suma"

    def resta(self):

        #si ya tiene asignado un operador, agregamos el otro con el mismo boton
        if(self.operador1 ==0):
            self.operador1 = float(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "resta"        
        

    def multiplica(self):
         if(self.operador1 ==0):
            self.operador1 = float(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "multiplica"

    def divide(self):
         if(self.operador1 ==0):
            self.operador1 = float(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "divide" 

    def Potencia(self):

         if(self.operador1 ==0):
            self.operador1 = float(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "potencia"

    def Raiz(self):

         if(self.operador1 ==0):
            self.operador1 = float(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "raiz"                            
                


   #Al APRETAR IGUAL =
               
    def resultado(self):
        self.operador2 = float(self.Calculo.text())
        self.historial = str(self.operador1)
        self.historial2 = str(self.operador2)
        
        if(self.operacion == "suma"):
            self.opera = "+"
            self.Calculo.setText(str(self.operador1+self.operador2))
            #HISTORIAL
            self.Calculo_2.setText(self.historial + self.opera + self.historial2)

            #al apretar = seteamos los operadores a 0
            self.operador1 = 0 

        elif(self.operacion == "resta"):
            self.opera = "-"
            self.Calculo.setText(str(self.operador1 - self.operador2))
            #HISTORIAL
            self.Calculo_2.setText(self.historial + self.opera + self.historial2)

            #al apretar = seteamos los operadores a 0
            self.operador1 = 0     

        elif(self.operacion == "multiplica"):
            self.opera = "x"
            self.Calculo.setText(str(self.operador1*self.operador2))
            # HISTORIAL
            self.Calculo_2.setText(self.historial + self.opera + self.historial2)
            #al apretar = seteamos los operadores a 0
            self.operador2 = 0
            self.operador1 = 0

        elif(self.operacion == "divide"):
            self.opera = "/"
            self.Calculo.setText(str(self.operador1/self.operador2))
            # HISTORIAL
            self.Calculo_2.setText(self.historial + self.opera + self.historial2)
            #al apretar = seteamos los operadores a 0
            self.operador2 = 0
            self.operador1 = 0

        elif(self.operacion == "potencia"):
            self.opera = "^"
            self.Calculo.setText(str(self.operador1 ** self.operador2))
            # HISTORIAL
            self.Calculo_2.setText(self.historial + self.opera + self.historial2)
            #al apretar = seteamos los operadores a 0
            self.operador2 = 0
            self.operador1 = 0 

        elif(self.operacion == "raiz"):
            self.opera = "√"
            self.Calculo.setText(str(self.operador1 ** (self.operador2**(-1))))
            # HISTORIAL
            self.Calculo_2.setText(self.historial + self.opera + self.historial2)
            #al apretar = seteamos los operadores a 0
            self.operador2 = 0
            self.operador1 = 0                     

            
                

    def borratodo(self):
        self.operador1 = 0
        self.operador2 = 0



    #EVENTOS DE ASIGNACION DE VALOES AL LABEL
    def click_1(self):
        self.Calculo.setText(self.Calculo.text() + "1") 

    def click_2(self):
        self.Calculo.setText(self.Calculo.text() + "2")

    def click_3(self):
        self.Calculo.setText(self.Calculo.text() + "3")

    def click_4(self):
        self.Calculo.setText(self.Calculo.text() + "4")  

    def click_5(self):
        self.Calculo.setText(self.Calculo.text() + "5")

    def click_6(self):
        self.Calculo.setText(self.Calculo.text() + "6") 

    def click_7(self):
        self.Calculo.setText(self.Calculo.text() + "7")  

    def click_8(self):
        self.Calculo.setText(self.Calculo.text() + "8")  

    def click_9(self):
        self.Calculo.setText(self.Calculo.text() + "9")  

    def click_0(self):
        self.Calculo.setText(self.Calculo.text() + "0")  

    def click_punto(self):
        self.Calculo.setText(self.Calculo.text() + ".")                                                  


  

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()