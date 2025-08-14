#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup, QTextEdit, QListWidget, QLineEdit, QInputDialog
import json


def show_note():
    name = spisok_zametok.selectedItems()[0].text()
    vvod_zametki.setText(notes[name]['текст'])
    spisok_tegov.clear()
    spisok_tegov.addItems(notes[name]['теги'])

def add_note():
    imya_zametki, ok = QInputDialog.getText(mw, 'Добавить заметку', 'Название заметки')
    if ok and imya_zametki != '':
        notes[imya_zametki] = {'текст': '', 'теги': []}
        spisok_zametok.addItem(imya_zametki)
    elif ok and imya_zametki == '':
        win = QMessageBox()
        win.setText('ОШИБКА!\n назовите заметку')
        win.exec_() 
    else:
        pass                


def del_note():
    if spisok_zametok.selectedItems():
        name = spisok_zametok.selectedItems()[0].text()
        del notes[name]
        spisok_zametok.clear()
        spisok_zametok.addItems(notes)
        spisok_tegov.clear()
    else:
        win = QMessageBox()
        win.setText('ОШИБКА!\n выберите заметку')
        win.exec_()                 


def save_note():
    if spisok_zametok.selectedItems():
        name = spisok_zametok.selectedItems()[0].text()
        text = vvod_zametki.toPlainText()
        notes[name]['текст'] = text
    else:
        win = QMessageBox()
        win.setText('ОШИБКА!\n выберите заметку')
        win.exec_()                 

        

def add_tag():
    if spisok_zametok.selectedItems():
        name = spisok_zametok.selectedItems()[0].text()
        taxt = vvod_tega.text()
        if not taxt in notes[name]['теги'] and taxt != '':
            notes[name]['теги'].append(taxt)
            vvod_tega.clear()
            spisok_tegov.clear()
            spisok_tegov.addItems(notes[name]['теги'])
        elif taxt in notes[name]['теги']:
            win = QMessageBox()
            win.setText('ОШИБКА!\n тег уже есть')
            win.exec_()
        else:
            win = QMessageBox()
            win.setText('ОШИБКА!\n введите тег')
            win.exec_()  
    else:
        win = QMessageBox()
        win.setText('ОШИБКА!\n выберите заметку')
        win.exec_()                 

def del_tag():
    if spisok_tegov.selectedItems():
        name = spisok_zametok.selectedItems()[0].text()
        nam = spisok_tegov.selectedItems()[0].text()
        notes[name]['теги'].remove(nam)
        spisok_tegov.clear()
        spisok_tegov.addItems(notes[name]['теги'])
    elif not spisok_zametok.selectedItems():
        win = QMessageBox()
        win.setText('ОШИБКА!\n выберите заметку')
        win.exec_()       
    else:
        win = QMessageBox()
        win.setText('ОШИБКА!\n выберите тег')
        win.exec_() 

def search_tag():
    tag = vvod_tega.text()
    spisok_poiska = {}
    if knopka_iskat.text() == 'Искать заметки по тегу' and tag != '':
        for note in notes:
            if tag in notes[note]['теги']:
                spisok_poiska[note] = notes[note]
        spisok_zametok.clear()
        vvod_tega.clear()
        spisok_tegov.clear()
        spisok_zametok.addItems(spisok_poiska)
        knopka_iskat.setText('Сбросить поиск')
    elif knopka_iskat.text() == 'Сбросить поиск':
        spisok_tegov.clear()
        spisok_zametok.clear()
        vvod_tega.clear()
        spisok_zametok.addItems(notes)
        knopka_iskat.setText('Искать заметки по тегу')
    else:
        win = QMessageBox()
        win.setText('ОШИБКА!\n введите тег')
        win.exec_()

with open('notes.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)


app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Умные заметки')
mw.resize(900, 600)

knopka_sozdat = QPushButton('Создать заметку')
knopka_udal = QPushButton('Удалить заметку')
knopka_dobav = QPushButton('Добавить к заметке')
knopka_otkrep = QPushButton('Открепить от заметки')
knopka_sohran = QPushButton('Сохранить заметку')
knopka_iskat = QPushButton('Искать заметки по тегу')
nadpis_zametki = QLabel('Список заметок')
nadpis_tegi = QLabel('Список тегов')
vvod_zametki = QTextEdit()


vvod_tega = QLineEdit()
spisok_zametok = QListWidget()
spisok_tegov = QListWidget()
vvod_tega.setPlaceholderText('Введите тег...')

vertikal_lm = QHBoxLayout()
vertikal_lm.addWidget(knopka_sozdat)
vertikal_lm.addWidget(knopka_udal)
vertikal_pm = QHBoxLayout()
vertikal_pm.addWidget(knopka_dobav)
vertikal_pm.addWidget(knopka_otkrep)
vertikal_gl = QVBoxLayout()
vertikal_gl.addWidget(nadpis_zametki)
vertikal_gl.addWidget(spisok_zametok)
vertikal_gl.addLayout(vertikal_lm)
vertikal_gl.addWidget(knopka_sohran)
vertikal_gl.addWidget(nadpis_tegi)
vertikal_gl.addWidget(spisok_tegov)
vertikal_gl.addWidget(vvod_tega)
vertikal_gl.addLayout(vertikal_pm)
vertikal_gl.addWidget(knopka_iskat)
gorizontal_gl = QHBoxLayout()
gorizontal_gl.addWidget(vvod_zametki, 59)
gorizontal_gl.addLayout(vertikal_gl, 41)
mw.setLayout(gorizontal_gl)

spisok_zametok.addItems(notes)
spisok_zametok.itemClicked.connect(show_note)
knopka_sozdat.clicked.connect(add_note)
knopka_udal.clicked.connect(del_note)
knopka_sohran.clicked.connect(save_note)
knopka_dobav.clicked.connect(add_tag)
knopka_otkrep.clicked.connect(del_tag)
knopka_iskat.clicked.connect(search_tag)

mw.show()
app.exec_()
with open('notes.json', 'w', encoding='utf-8') as file:
    json.dump(notes, file)