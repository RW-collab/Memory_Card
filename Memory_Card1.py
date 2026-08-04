#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, 
    QGroupBox, QRadioButton, 
    QPushButton, QLabel)

app = QApplication([])


# Create question panel
btn_OK = QPushButton('answer') #answer button
lb_Question = QLabel('In what year was New York founded?')


RadioGroupBox  =QGroupBox("answer options") # group on the screen for radio buttons with answers
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')


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


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.show()


app.exec()
