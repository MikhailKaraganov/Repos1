from PyQt5 import QtWidgets
import sys

#print("Arguments", sys.argv)

def except_ok():
    except_wind.close()  

    

print(QtWidgets.QStyleFactory.keys())

app = QtWidgets.QApplication(sys.argv)
app.setStyle('windowsvista')
window = QtWidgets.QWidget()
window.setWindowTitle("Гребаный Калькулятор")
window.resize(400, 300)
operat_simbol = QtWidgets.QLabel()


#Окно обработчика исключения  
except_wind = QtWidgets.QWidget()
except_wind.setWindowTitle("ЭЭ, Йопта!")
text_of_exception = QtWidgets.QLabel('Сначала введи число!')
except_wind.resize(400, 100)
ok_butt_for_except=QtWidgets.QPushButton('&OK')
ok_butt_for_except.clicked.connect(except_ok)
except_layout = QtWidgets.QGridLayout()
except_layout.addWidget(text_of_exception)
except_layout.addWidget(ok_butt_for_except)
except_wind.setLayout(except_layout)


  

mainSpace = QtWidgets.QLabel()

collector = []

class MyButton (QtWidgets.QPushButton):
    def Ifclicked1(self):
        if (self.text()[1] == "+") & (collector != ''):
            try:
                if ((collector[-1] != "+") & (collector[-1] != "-") & (collector[-1] != "*") & (collector[-1] != "/")):
                    collector.append("+")
                    operat_simbol.setText(operat_simbol.text() + "+")
                    mainSpace.display(''.join(collector))
                    print(collector[-1])
                    print(''.join(collector))
            except:
                except_wind.show()

    def Ifclicked2(self):
        if (self.text()[1] == '-') & (collector != ''):
            try:
                if ((collector[-1] != "+") & (collector[-1] != "-") & (collector[-1] != "*") & (collector[-1] != "/")):
                    collector.append("-")
                    operat_simbol.setText(operat_simbol.text() + "-")
                    mainSpace.display(''.join(collector))
                    print(''.join(collector))
            except:
                except_wind.show()

    def Ifclicked3(self):
        if (self.text()[1] == "/") & (collector != ''):
            try:
                if ((collector[-1] != "+") & (collector[-1] != "-") & (collector[-1] != "*") & (collector[-1] != "/")):
                    collector.append("/")
                    operat_simbol.setText(operat_simbol.text() + "/")
                    mainSpace.display(''.join(collector))
                    print(''.join(collector))
            except:
                except_wind.show()

    def Ifclicked4(self):
        if (self.text()[1] == "*") & (collector != ''):
            try:
                if ((collector[-1] != "+") & (collector[-1] != "-") & (collector[-1] != "*") & (collector[-1] != "/")):
                    collector.append("*")
                    operat_simbol.setText(operat_simbol.text() + "*")
                    mainSpace.display(''.join(collector))
                    print(''.join(collector))
            except:
                except_wind.show()

    def Clear(self):
            mainSpace.display(0)
            collector.clear()
            operat_simbol.setText("")
        
    def Ifclicked(self): 
        collector.append(self.text()[1])
        mainSpace.display(''.join(collector))
    
    def Calculate(self):
        k = 0
        calc = [[]]
        for i in range(0, len(collector)):
            
            if ((collector[i] != "+") & (collector[i] != "-") & (collector[i] != "/") & (collector[i] != "*")):
               # print('Длинна выражения:', len(''.join(collector)))
               # print('Выражение:', ''.join(collector))
               # print(str(collector[i]))
                
                calc[k].append(str(collector[i])) 
            else:
                calc[k] = ''.join(calc[k])
                calc.append([])
                k+=1
        calc[k] = ''.join(calc[k])
        print(calc)
        print(''.join(calc[k]))
        k=0
        acum = float(calc[k])
        for i in range(0, len(collector)):
            if collector[i] == "+":
                acum = acum + float(calc[k+1])
                k += 1
            if collector[i] == "-":
                acum = acum - float(calc[k+1]) 
                k += 1
            if collector[i] == "*":
                acum = acum * float(calc[k+1])
                k += 1
            if collector[i] == "/":
                acum = acum / float(calc[k+1])
                k += 1
        mainSpace.display(acum)
        print('Равно:', acum)

                


btnDig_0 = MyButton('&0')
btnDig_0.clicked.connect(btnDig_0.Ifclicked)

btnDig_1 = MyButton('&1')
btnDig_1.clicked.connect(btnDig_1.Ifclicked)

btnDig_2 = MyButton('&2')
btnDig_2.clicked.connect(btnDig_2.Ifclicked)

btnDig_3 = MyButton('&3')
btnDig_3.clicked.connect(btnDig_3.Ifclicked)

btnDig_4 = MyButton('&4')
btnDig_4.clicked.connect(btnDig_4.Ifclicked)

btnDig_5 = MyButton('&5')
btnDig_5.clicked.connect(btnDig_5.Ifclicked)

btnDig_6 = MyButton('&6')
btnDig_6.clicked.connect(btnDig_6.Ifclicked)

btnDig_7 = MyButton('&7')
btnDig_7.clicked.connect(btnDig_7.Ifclicked)

btnDig_8 = MyButton('&8')
btnDig_8.clicked.connect(btnDig_8.Ifclicked)

btnDig_9 =MyButton('&9')
btnDig_9.clicked.connect(btnDig_9.Ifclicked)

btn_ADD = MyButton('&+')
btn_ADD.clicked.connect(btn_ADD.Ifclicked1)

btn_SUB = MyButton('&-')
btn_SUB.clicked.connect(btn_SUB.Ifclicked2)

btn_DIV = MyButton('&/')
btn_DIV.clicked.connect(btn_DIV.Ifclicked3)

btn_MUL = MyButton('&*')
btn_MUL.clicked.connect(btn_MUL.Ifclicked4)

btn_RES = MyButton('&C')
btn_RES.clicked.connect(btn_RES.Clear)

btn_EQU = MyButton('&=')
btn_EQU.clicked.connect(btn_EQU.Calculate)



keboard = QtWidgets.QButtonGroup()
keboard.addButton(btnDig_0)
keboard.addButton(btnDig_3)

# Добавляем кнопки в контейнер
layout = QtWidgets.QGridLayout()
layout.addWidget(btnDig_0, 3,0)
layout.addWidget(btnDig_1, 3,1)
layout.addWidget(btnDig_2, 3,2)
layout.addWidget(btnDig_3, 3,3)
layout.addWidget(btnDig_4, 2,1)
layout.addWidget(btnDig_5, 2,2)
layout.addWidget(btnDig_6, 2,3)
layout.addWidget(btnDig_7, 1,1)
layout.addWidget(btnDig_8, 1,2)
layout.addWidget(btnDig_9, 1,3)
layout.addWidget(btn_DIV, 0,0)
layout.addWidget(btn_ADD, 1,0)
layout.addWidget(btn_EQU, 0,3)
layout.addWidget(btn_RES, 0,2)
layout.addWidget(btn_MUL, 0,1)
layout.addWidget(btn_SUB, 2,0)
layout.addWidget(operat_simbol, 4, 2)
layout.addWidget(mainSpace, 5,0,4,4)

layout.setHorizontalSpacing(0)
layout.setVerticalSpacing(0)

window.setLayout(layout)

#btnQuit.clicked.connect(app.quit)
window.show()
#print(QtWidgets.qApp.arguments())

with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

sys.exit(app.exec_())
