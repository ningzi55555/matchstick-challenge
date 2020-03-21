'''
界面
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QLineEdit, QPushButton,QComboBox,QTextBrowser
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPainter, QFont,QPen,QPixmap
from PyQt5.QtCore import Qt
import search,search2


#开始界面（选择移动一根或两根火柴）
class IntroWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MATCHSTICK CHALLENGE')
        Title_label=QLabel(self)
        Title_label.setText("火柴棍挑战")
        Title_label.setFont(QFont("微软雅黑", 20))
        Title_label.adjustSize()
        Title_label.move(400,100)

        self.OneMatchBtn=QPushButton('移动一根火柴',self)
        self.OneMatchBtn.resize(200,100)
        self.OneMatchBtn.move(400,200)
        self.OneMatchBtn.setFont(QFont("微软雅黑", 10))

        self.TwoMatchBtn=QPushButton('移动两根火柴',self)
        self.TwoMatchBtn.resize(200, 100)
        self.TwoMatchBtn.move(400, 350)
        self.TwoMatchBtn.setFont(QFont("微软雅黑", 10))


        self.OneMatchBtn.clicked.connect(self.on_OneMatch_clicked)
        self.TwoMatchBtn.clicked.connect(self.on_TwoMatch_clicked)
        self.setGeometry(300, 300, 1000, 600)

    windowList = []

    def on_OneMatch_clicked(self):
        John = mainWindow()
        John.flag=0
        John.setWindowTitle('Move one match')
        self.windowList.append(John)
        self.close()
        John.show()

    def on_TwoMatch_clicked(self):
        Paul = mainWindow()
        Paul.level.addItem('等式题库')
        Paul.flag=1
        Paul.setWindowTitle('Move two matches')
        self.windowList.append(Paul)
        self.close()
        Paul.show()

############################################################
#正式界面
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.flag=0
        #自己输入式子按下“确定”按钮会将题目用火柴棍显示，并显示答案
        confrim_btn = QPushButton('确定', self)
        confrim_btn.move(285, 355)
        confrim_btn.resize(135,35)

        #自己输入式子按下“出题”按钮会将题目用火柴棍显示，但不会显示答案
        question_btn=QPushButton('出题',self)
        question_btn.move(50,355)
        question_btn.resize(135,35)

        #输入式子的第一个数字
        self.num_a = QLineEdit(self)
        self.num_a.resize(70,50)
        self.num_a.setFont(QFont( "微软雅黑" , 20 ))
        self.num_a.move(50,290)

        #输入式子的运算符
        self.operator = QComboBox(self)
        self.operator.resize(70,50)
        self.operator.setFont(QFont("微软雅黑", 15))
        self.operator.move(138,292)
        self.operator.addItems(['+', '-', '*'])
        self.operator.adjustSize()

        #输入式子的第二个数字
        self.num_b = QLineEdit(self)
        self.num_b.resize(70, 50)
        self.num_b.setFont(QFont("微软雅黑", 20))
        self.num_b.move(210,290)

        label_equal = QLabel(self)
        label_equal.setText("=")
        label_equal.move(280,270)
        label_equal.setFont(QFont("微软雅黑",30))
        label_equal.adjustSize()

        #输入式子的结果
        self.num_c = QLineEdit(self)
        self.num_c.resize(90, 50)
        self.num_c.setFont(QFont("微软雅黑", 20))
        self.num_c.move(330,290)

        #显示答案
        self.text_result=QTextBrowser(self)
        self.text_result.move(470,300)
        self.text_result.resize(480,250)
        self.text_result.setFont(QFont("微软雅黑", 20))

        label_equal = QLabel(self)
        label_equal.setText("解答")
        label_equal.move(680, 245)
        label_equal.setFont(QFont("微软雅黑", 13))
        label_equal.adjustSize()

        label_make_question = QLabel(self)
        label_make_question.setText("自己出题")
        label_make_question.move(180, 235)
        label_make_question.setFont(QFont("微软雅黑", 13))
        label_make_question.adjustSize()

        label_choose_question = QLabel(self)
        label_choose_question.setText("从题库选题")
        label_choose_question.move(165, 415)
        label_choose_question.setFont(QFont("微软雅黑", 13))
        label_choose_question.adjustSize()

        level_label=QLabel(self)
        level_label.setFont(QFont("微软雅黑", 10))
        level_label.move(50, 465)
        level_label.setText('等级：')
        level_label.adjustSize()

        #选择等级
        self.level=QComboBox(self)
        self.level.addItems(['1','2','3'])
        self.level.setFont(QFont("微软雅黑", 10))
        self.level.move(100,465)
        self.level.currentIndexChanged.connect(self.levelChanged)
        self.level.resize(135, 35)

        #从题库中选择一题，显示该题答案
        answer_btn = QPushButton('显示答案', self)
        answer_btn.move(100, 510)
        answer_btn.resize(135, 35)

        #显示题库上一题
        former_btn = QPushButton('上一题', self)
        former_btn.move(285, 465)
        former_btn.resize(135, 35)

        #显示题库下一题
        latter_btn = QPushButton('下一题', self)
        latter_btn.move(285, 510)
        latter_btn.resize(135, 35)

        confrim_btn.clicked.connect(self.confirm_btn_clicked)
        question_btn.clicked.connect(self.question_btn_clicked)
        answer_btn.clicked.connect(self.answer)
        former_btn.clicked.connect(self.former_btn_clicked)
        latter_btn.clicked.connect(self.latter_btn_clicked)

        self.numbers=[QPixmap('new_0.png'),QPixmap('new_1.png'),QPixmap('new_2.png'),QPixmap('new_3.png'),
                      QPixmap('new_4.png'),QPixmap('new_5'),QPixmap('new_6.png'),QPixmap('new_7.png'),
                      QPixmap('new_8.png'),QPixmap('new_9.png'),QPixmap('new_add.png'),QPixmap('new_minus.png'),
                      QPixmap('new_mul.png'),QPixmap('new_equal.png')]

        #以下为题库，每一等级有10道题，Order表示目前显示的是第几题
        self.Order=0
        OneMatchProblem1 = [['5', '2', '8', '+'], ['1', '5', '4', '+'],['7','8','7','-'],['8','2','-4','+'],['0','3','2','+'],['5','1','8','-'],
                            ['3','7','4','-'],['6','9','5','+'],['4','5','7','+'],['5','5','8','+']]
        OneMatchProblem2 = [['21', '52', '83', '+'], ['22','45','97','+'],['12','35','45','+'],['15','23','62','-'],['41','72','35','-'],
                            ['68','12','12','+'],['-31','10','-87','+'],['77','51','34','-'],['77','51','34','+'],['85', '98', '181', '-']]
        OneMatchProblem3 = [['8', '4', '35', '*'], ['31', '90', '4550', '*'],['16','86','1230','*'],['98','32','1056','*'],['68','2','204','*'],
                            ['55','90','5398','*'],['85','5','255','*'],['52','11','3892','*'],['8','22','190','*'],['8','80','784','*']]

        TwoMatchProblem1 = [['4', '3', '2', '+'], ['8', '2', '-8', '-'],['-4','2','-8','+'],['0','4','7','+'],['0','1','-7','-'],['5','1','-7','-'],
                            ['5','1','-4','+'],['2','1','7','+'],['2','4','0','+'],['5','4','0','-']]
        TwoMatchProblem2 = [['52', '44', '53', '-'], ['65', '34', '42', '+'],['-57','11','-80','+'],['-27','31','60','-'],['32','36','-41','-'],
                            ['-60','59','21','-'],['81','53','121','+'],['90','53','121','-'],['90','31','30','+'],['34','31','30','+']]
        TwoMatchProblem3 = [['-99', '99', '6881', '*'], ['94', '69', '4704', '*'],['-56','96','4376','*'],['15','27','7515','*'],['15','27','7515','*'],
                            ['62','69','3276','*'],['71','6','439','*'],['23','12','276','+'],['8','33','-104','*'],['-84','50','-4072','*']]
        #等式题库
        AccurateProblem = [['6', '0', '6', '+'], ['9', '0', '9', '+'], ['2', '3', '5', '+'],
                            ['9', '8', '17', '+'], ['1', '8', '9', '+'],
                            ['1', '3', '4', '+'], ['1', '3', '3', '*'], ['2', '3', '6', '*'],
                            ['5', '3', '2', '-'], ['5', '1', '4', '-']]

        self.Problems=[[OneMatchProblem1,OneMatchProblem2,OneMatchProblem3],[TwoMatchProblem1,TwoMatchProblem2,TwoMatchProblem3,AccurateProblem]]
        self.levels=0

        #var0,var1...var11为火柴棍图片显示的Label
        for i in range(12):
            exec('self.var{}=QLabel(self)'.format(i))

        if(self.flag==0):
            self.equation = OneMatchProblem1[0]
        else:
            self.equation=TwoMatchProblem1[0]

        self.setNum()
        self.setGeometry(300, 300, 1000, 600)

    #分割线
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(50, 220, 950, 220)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(50, 405, 420, 405)

    windowList=[]
    def closeEvent(self,event):
        George=IntroWindow()
        self.windowList.append(George)
        George.show()
        event.accept()

    def levelChanged(self):
        if(self.level.currentText()!='等式题库'):
            self.levels=int(self.level.currentText())-1
        else:
            self.levels=3
        self.Order=0
        self.equation=self.Problems[self.flag][self.levels][0]
        self.setNum()

    #判断输入的式子是否符合要求
    def getNum(self):
        self.equation[0] = self.num_a.text()
        self.equation[1] = self.num_b.text()
        self.equation[2] = self.num_c.text()
        self.equation[3] = self.operator.currentText()
        a=self.equation
        len1 = len(self.equation[0])
        len2 = len(self.equation[1])
        len3 = len(self.equation[2])
        if (len1 == 0 or (a[0][0]=='-' and (len1>3 or a[0][1:].isdigit()==False)) or (a[0][0]!='-' and (len1 > 2 or a[0].isdigit()==False)) ):
            return False
        elif(len2 == 0 or len2 > 2 or a[1].isdigit()==False ):
            return False
        elif(int(a[1])<0):
            return False
        elif(len3 == 0 or (a[2][0]=='-' and (len3>5 or a[2][1:].isdigit()==False)) or (a[2][0]!='-' and (len3 > 4 or a[2].isdigit()==False))):
            return False
        else:
            return True

    def confirm_btn_clicked(self):
        if (self.getNum() == False):
            QMessageBox.warning(self, "警告", "式子不符合规范，请重新输入式子", QMessageBox.Yes | QMessageBox.No)
        else:
            self.setNum()
            self.answer()

    def former_btn_clicked(self):
        if(self.Order==0):
            QMessageBox.warning(self, "警告", "已翻到第一题", QMessageBox.Yes | QMessageBox.No)
        else:
            self.Order-=1
            self.equation=self.Problems[self.flag][self.levels][self.Order]
        self.setNum()

    def latter_btn_clicked(self):
        if(self.Order==9):
            QMessageBox.warning(self, "警告", "已翻到最后一题", QMessageBox.Yes | QMessageBox.No)
        else:
            self.Order+=1
            self.equation=self.Problems[self.flag][self.levels][self.Order]
        self.setNum()

    #调用search函数得到答案
    def answer(self):
        ans = ''
        #若移动两根火柴
        if (self.flag == 1):
            self.result = search2.make_equation2(self.equation)
            n = int(len(self.result) / 12)
            if(n!=0):
                ans = ans + '移动2根火柴：\n'
            for i in range(n):
                ans=ans+str(self.result[i * 12 + 10])
                for j in range(2):
                    ans = ans + str(self.result[i * 12 + j])
                ans = ans + str(self.result[i * 12 + 8])
                for j in range(2, 4):
                    ans = ans + str(self.result[i * 12 + j])
                ans = ans + str(self.result[i * 12 + 9])
                ans = ans + str(self.result[i * 12 + 11])
                for j in range(4, 8):
                    ans = ans + str(self.result[i * 12 + j])
                ans = ans + '\n'
        #若移动一根火柴
        self.result = search.make_equation(self.equation)
        if (self.flag == 1 and self.result != []):
            ans = ans + '移动1根或0根火柴：\n'
        n = int(len(self.result) / 11)
        for i in range(n):
            for j in range(3):
                ans = ans + str(self.result[i * 11 + j])
            ans = ans + str(self.result[i * 11 + 10])
            for j in range(3, 5):
                ans = ans + str(self.result[i * 11 + j])
            if (self.result[i * 11 + 10] == '='):
                ans = ans + '-'
            else:
                ans = ans + '='
            for j in range(5, 10):
                ans = ans + str(self.result[i * 11 + j])
            ans = ans + '\n'

        if (ans == ''):
            self.text_result.setText('该式子无解')
        else:
            self.text_result.setText(ans)

    def question_btn_clicked(self):
        if (self.getNum() == False):
            QMessageBox.warning(self, "警告", "式子不符合规范，请重新输入式子", QMessageBox.Yes | QMessageBox.No)
        else:
            self.setNum()

    #将式子用火柴棍显示出来
    def setNum(self):
        equa=''
        equa+=self.equation[0]
        equa+=self.equation[3]
        equa+=self.equation[1]
        equa+='='
        equa+=self.equation[2]
        for i in range(12):
            exec('self.var{}.clear()'.format(i))
        for i in range(len(equa)):
            if (equa[i] == '+'):
                exec('self.var{}.setPixmap(self.numbers[10])'.format(i))
                exec('self.var{}.resize(60,60)'.format(i))
                exec('self.var{}.move(75*i+50,75)'.format(i))
            elif(equa[i]=='-'):
                exec('self.var{}.setPixmap(self.numbers[11])'.format(i))
                exec('self.var{}.resize(60,60)'.format(i))
                exec('self.var{}.move(75*i+50,75)'.format(i))
            elif (equa[i] == '*'):
                exec('self.var{}.setPixmap(self.numbers[12])'.format(i))
                exec('self.var{}.resize(60,60)'.format(i))
                exec('self.var{}.move(75*i+50,75)'.format(i))
            elif (equa[i] == '='):
                exec('self.var{}.setPixmap(self.numbers[13])'.format(i))
                exec('self.var{}.resize(60,60)'.format(i))
                exec('self.var{}.move(75*i+50,75)'.format(i))
            else:
                exec('self.var{}.setPixmap(self.numbers[int(equa[i])])'.format(i))
                exec('self.var{}.resize(75,120)'.format(i))
                exec('self.var{}.move(75*i+50,50)'.format(i))

            exec('self.var{}.setScaledContents(True)'.format(i))

if __name__ == '__main__':
    app = QApplication([])
    Ringo = IntroWindow()
    Ringo.show()
    sys.exit(app.exec_())
