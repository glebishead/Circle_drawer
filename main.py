import sys
from random import randrange
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor


class CircleDrawer(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.pushButton.clicked.connect(self.draw_circle)
		
		self.flag = False
	
	def draw(self):
		self.qp.setPen(QColor(*[randrange(255) for _ in range(3)]))
		n = randrange(10, 100)
		self.qp.drawEllipse(randrange(10, 550), randrange(10, 550), 2 * n, 2 * n)
	
	def draw_circle(self):
		self.flag = True
		self.update()
	
	def paintEvent(self, event):
		if self.flag:
			self.qp = QPainter()
			self.qp.begin(self)
			self.draw()
			self.qp.end()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = CircleDrawer()
	ex.show()
	sys.exit(app.exec_())
