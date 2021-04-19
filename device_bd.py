from PyQt5 import QtWidgets, QtGui, QtCore, QtSql
import PyQt5
import os
import sys
import sqlite3
##from PIL import Image

path = ''
for i in os.path.dirname(__file__):
    if i == "\\":
        path += '/'
    elif i == ' ': 
        continue
    else:
        path+=i


###########################################################
########    Создание\подключение базы данных   ############
###########################################################
commDB = sqlite3.connect("CommDB.db")
cursor = commDB.cursor()
try:
    cursor.execute("""CREATE TABLE devices
                  (Brand text, Model text, SerN int, Location text, 
                  ContrN int, ContactOrganization text, 
                  Client text, Contagent text, 
                  ContactName text, ContactPhone int, ServComment text)
                    """)
except:
    print('DB already exist')

#############################################################
########       Обработчики событий      #####################
#############################################################

###Окно ввода данных о новом приборе
def input_cliced ():
    input_window.show()


###Окно вывода данных о новом приборе
def output_cliced ():

    output_window.show()
    #cursor.execute("SELECT * FROM devices WHERE Model = (?)", [srch_model.text()])
    #cursor.execute("DELETE FROM devices WHERE Model = (?)", [srch_model.text()])
    cursor.execute("SELECT * FROM devices")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
  

####Внесение в базу
def db_commit():
    data_to_commit = [(input_place_devprod.text()), (input_place_devmode.text()), (input_place_devSN.text()),
                      (input_place_location.text()), (input_place_contractNB.text()), (input_place_org.text()),
                       (input_client.text()), (input_contragent.text()), (input_place_contactName.text()), (input_place_contactPHNB.text())]
    print(data_to_commit)
    cursor.execute("INSERT INTO devices VALUES (?,?,?,?,?,?,?,?,?,?)", data_to_commit)

    commDB.commit()

    input_place_devprod.clear()
    input_place_devmode.clear()
    input_place_devSN.clear()
    input_place_location.clear()
    input_place_contractNB.clear()
    input_place_org.clear()
    input_client.clear()
    input_contragent.clear()
    input_place_contactName.clear()
    input_place_contactPHNB.clear()

def file_commit():
    file_commit_window.show()
    if dialog.fileSelected():
        print(dialog.getOpenFileUrl)
    #im = Image.open(dialog.get)



####Вывод таблицы (пока всей)
def output() :
   print("""PRAGMA table_info(devices)""")
    # print(cursor.execute("SELECT rowid, * FROM devices ORDER BY SerN"))

def seacrh():
   print(cursor.execute("""PRAGMA table_info(devices)"""))
   #("SELECT ServComment FROM devices WHERE SerN LIKE "%search_sn_place.text()%" OR WHERE Client LIKE "%search_client_place.text()%" ")



app = QtWidgets.QApplication(sys.argv)

###########################################################
########            Стартовое окно             ############
###########################################################
start_window = QtWidgets.QWidget()
start_window.setWindowTitle('База приборов')
start_window.setWindowIcon(QtGui.QIcon(path + "/Icon.png"))
button_input = QtWidgets.QPushButton('Внести новый прибор')
button_input.clicked.connect(input_cliced)
button_output = QtWidgets.QPushButton('Получить/редактировать данные о приборе')
button_output.clicked.connect(output_cliced)
service_btn = QtWidgets.QPushButton('Сервисная база')




# print('Вот:', os.path.dirname(__file__), '\nИ вот:', path)
start_layout = QtWidgets.QGridLayout()

###########################################################
######## Окно ввода информации о новом приборе ############
###########################################################
input_window = QtWidgets.QWidget()
input_window.setWindowTitle('Ввод нового прибора')
input_window.resize(QtCore.QSize(1000,300))
input_window.setWindowIcon(QtGui.QIcon(path + "/upload.png"))
###Поля ввода информации в окне ввода
input_layout = QtWidgets.QGridLayout()
lable_devprod = QtWidgets.QLabel('Введите данные прибора:')
input_place_devprod = QtWidgets.QLineEdit()
input_place_devprod.setPlaceholderText('Производитель прибора (Sysmex, Alifax, Roshe..)')
input_place_devmode = QtWidgets.QLineEdit()
input_place_devmode.setPlaceholderText('Введите модель прибора:')
input_place_devSN = QtWidgets.QLineEdit()
input_place_devSN.setPlaceholderText('Введите серийный номер прибора:')
input_place_org = QtWidgets.QLineEdit()
input_place_org.setPlaceholderText('Введите контактную организацию:')
input_place_location = QtWidgets.QLineEdit()
input_place_location.setPlaceholderText('Введите место нахождения прибора:')
input_client = QtWidgets.QLineEdit()
input_client.setPlaceholderText('Конечный клиент:')
input_contragent = QtWidgets.QLineEdit()
input_contragent.setPlaceholderText('Введите контрагента:')
input_place_contactName = QtWidgets.QLineEdit()
input_place_contactName.setPlaceholderText('Введите ФИО контакта:')
input_place_contactPHNB = QtWidgets.QLineEdit()
input_place_contactPHNB.setPlaceholderText('Введите номер телефона контактного лица:')
input_place_contractNB = QtWidgets.QLineEdit()
input_place_contractNB.setPlaceholderText('Введите номер договора:')

input_submit_btn = QtWidgets.QPushButton('Ввести данные')
#Назначение обработчика кнопки коммита
input_submit_btn.clicked.connect(db_commit)

add_file_btn = QtWidgets.QPushButton('Прикрепить файлы')
add_file_btn.clicked.connect(file_commit)

###Добавление полей ввода в слой окна ввода данных
input_layout.addWidget(lable_devprod)
input_layout.addWidget(input_place_devprod)
input_layout.addWidget(input_place_devmode)
input_layout.addWidget(input_place_devSN)
input_layout.addWidget(input_place_location)
input_layout.addWidget(input_place_contractNB)
input_layout.addWidget(input_place_org)
input_layout.addWidget(input_client)
input_layout.addWidget(input_contragent)
input_layout.addWidget(input_place_contactName)
input_layout.addWidget(input_place_contactPHNB)
input_layout.addWidget(input_submit_btn)
input_layout.addWidget(add_file_btn)
###Передача слоя в окно ввода данных
input_window.setLayout(input_layout)




###############################################################################
###  Окно для получения/дополнении информации о раннее внесенном приборе ######
###############################################################################


output_window = QtWidgets.QWidget()
output_window.setWindowIcon(QtGui.QIcon(path + "/download.png"))
srch_model = QtWidgets.QLineEdit()
srch_model.setPlaceholderText('Модель прибора')
srch_SN = QtWidgets.QLineEdit()
srch_SN.setPlaceholderText('Серийный номер')
srch_location = QtWidgets.QLineEdit()
srch_location.setPlaceholderText('Локация')
srch_client = QtWidgets.QLineEdit()
srch_client.setPlaceholderText('Клиент')

output_btn = QtWidgets.QPushButton('Вывести')
output_btn.clicked.connect(output_cliced)



###############################################################################
######################### Объявление слоев ####################################
###############################################################################


output_layout = QtWidgets.QGridLayout()
output_layout.addWidget(output_btn)
output_layout.addWidget(srch_model)
output_layout.addWidget(srch_SN)
output_layout.addWidget(srch_location)
output_layout.addWidget(srch_client)


file_commit_window = QtWidgets.QWidget()
file_commit_layout = QtWidgets.QGridLayout()
dialog = QtWidgets.QFileDialog()
file_commit_layout.addWidget(dialog)
file_commit_window.setLayout(file_commit_layout)


output_window.setLayout(output_layout)

start_layout.addWidget(button_input)
start_layout.addWidget(button_output)
start_layout.addWidget(service_btn)

start_window.setLayout(start_layout)


start_window.show()

sys.exit(app.exec_())
