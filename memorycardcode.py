from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QGroupBox,QHBoxLayout,QVBoxLayout, QButtonGroup
from random import shuffle
from random import randint



class Question():
    def __init__(self,question,ransw,wrong1,wrong2,wrong3):
        self.question = question
        self.ransw = ransw
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



question_list = []
question_list.append(Question('Какой национальности не существует?','Смурфы','Энцы','Чулымцы','Алеуты'))
question_list.append(Question('Какого города не существует?','Тарков','Сургут','Самара','Сызрань'))
question_list.append(Question('Какая страна самая населенная?','Индия','Китай','Бангладеш','Нигерия'))
question_list.append(Question('Какая страна самая большая по площади?','Россия','Китай','США','Индия'))
question_list.append(Question('Какой язык программирования наиболее мощный?','C++','Python','JavaScript','GO'))
question_list.append(Question('Как зовут автора этого теста?','Поленов Александр','Луговой Дмитрий','Епанешников Тимофей','Чеснов Елисей'))
question_list.append(Question('Какая из этих планет самая большая?', 'Юпитер','Сатурн','Земля','Нептун'))
question_list.append(Question('Какая из этих звезд самая крупная?', 'Стивенсон 2-18','Арктур','Бетельгейзе','Солнце'))
question_list.append(Question('Зачем сеньоры смешивают воду с соком и газировкой?','Чтобы пить','Неизвестно','Чтобы лучше писать код','Чтобы лучше орать на джуниоров'))
question_list.append(Question('Почему не работает гитхаб?','Из-за ркна','Из-за картошечных серверов','Из-за ненависти к Канаде','Из-за ненависти к джуниорам'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memo Card')
main_win.resize(400,300)

quest = QLabel('Какой национальности не существует?')
answ = QPushButton('Ответить')

Radiogroupbox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

Radiogroup=QButtonGroup()
Radiogroup.addButton(rbtn_1)
Radiogroup.addButton(rbtn_2)
Radiogroup.addButton(rbtn_3)
Radiogroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
Radiogroupbox.setLayout(layout_ans1)
Answgroupbox = QGroupBox('Результат теста')
text = QLabel('Правильно/Неправильно')
text2 = QLabel('Правильный ответ')

layout5 = QVBoxLayout()
layout5.addWidget(text, alignment=(Qt.AlignLeft| Qt.AlignTop))
layout5.addWidget(text2, alignment=Qt.AlignHCenter, stretch=2)
Answgroupbox.setLayout(layout5)





layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout1.addWidget(quest, alignment=(Qt.AlignHCenter| Qt.AlignVCenter))
layout2.addWidget(Radiogroupbox)
layout2.addWidget(Answgroupbox)
Answgroupbox.hide()
layout3.addStretch(1)
layout3.addWidget(answ, stretch=2)
layout3.addStretch(1)

layout4 = QVBoxLayout()
layout4.addLayout(layout1, stretch=2)
layout4.addLayout(layout2,stretch=8)
layout4.addStretch(1)
layout4.addLayout(layout3,stretch=1)
layout4.addStretch(1)
layout4.setSpacing(5)


def show_result():
    Radiogroupbox.hide()
    Answgroupbox.show()
    answ.setText('Следующий вопрос')

def show_question():
    Answgroupbox.hide()
    Radiogroupbox.show()
    answ.setText('Ответить')
    Radiogroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    Radiogroup.setExclusive(True)

spisok = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q:Question):
    shuffle(spisok)
    spisok[0].setText(q.ransw)
    spisok[1].setText(q.wrong3)
    spisok[2].setText(q.wrong2)
    spisok[3].setText(q.wrong1)
    quest.setText(q.question)
    text2.setText(q.ransw)
    show_question()
    
def show_correct(textr):
    text.setText(textr)
    show_result()

main_win.score = 0
main_win.total = 0

def check_answer():
    if spisok[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        if spisok[1].isChecked() or spisok[2].isChecked() or spisok[3].isChecked():
            show_correct('Неправильно')
    print('Статистика\n-Всего вопросов:', main_win.total)
    print('-Правильных ответов:', main_win.score)
    print('Рейтинг:', main_win.score/main_win.total*100)
        



def next_question():
    main_win.total += 1
    cur_question = randint(0,len(question_list) - 1)
    qu = question_list[cur_question]
    ask(qu)
    print('Статистика\n-Всего вопросов:', main_win.total)
    print('-Правильных ответов:', main_win.score)


def click_ok():
    if answ.text() == 'Ответить':
        check_answer()
    elif answ.text() == 'Следующий вопрос':
        next_question()




answ.clicked.connect(click_ok)
next_question()



main_win.setLayout(layout4)
main_win.show()
app.exec()
