#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, 
    QGroupBox, QRadioButton, 
    QPushButton, QLabel, QButtonGroup)
from random import shuffle

app = QApplication([])


# Create question panel
btn_OK = QPushButton('answer') #answer button
lb_Question = QLabel('In what year was New York founded?')


RadioGroupBox = QGroupBox("answer options") # group on the screen for radio buttons with answers
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() # the vertical ones will be inside the horizontal ones
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # two answers in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answets in the second column
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) #columns are in the same line


RadioGroupBox.setLayout(layout_ans1) # "panel" with answer options are ready


# Create a results panel
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('Are you correct or not?') # "Correct" or "Incorrect" test will be here
lb_Correct = QLabel('the answer will be here!') # correct answer text will be written here


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# Place all the widgets in the window
layout_line1 = QHBoxLayout() #question
layout_line2 = QHBoxLayout() # answer options or test results
layout_line3 = QHBoxLayout() # "answer" button


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))


# Put both panels in the same line; one of them will be hidden and the other will be shown
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide() # We've already seen this panel' let's hide it and see hwo the answer panel turned out


# Now let's put the lines we've created one under one another:


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # the button shuld be large
layout_line3.addStretch(1)
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between content


def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('next question')


def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(question, right_answer, wrong1, wrong2, wrong3):
    ''' the function writes the value of the question and asnwers into the corresponding widgets while distributing the answer options randomly'''
    shuffle(answers)
    answers[0].setText(right_answer) 
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(question)
    lb_Correct.setText(right_answer)
    show_question()


def show_correct(res):
    ''' show result - put the written text into "result" and show the corresponding panel '''
    lb_Result.setText(res)
    show_result()


def check_answer():
    ''' if an answer option was selected, check and show answer panel '''
    if answers[0].isChecked():
        show_correct('Correct!')
    else:
        if answers[1].isChecked or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')

    
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
ask('The national language of Brazil', 'Brazillian', 'Portuguese', 'Spanish', 'Italian')
btn_OK.clicked.connect(check_answer)


window.resize(400, 300)
window.show()
app.exec()
