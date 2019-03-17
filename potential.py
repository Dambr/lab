#Метод потенциалов
#Метод минимального элемента.


from tkinter import *
from tkinter import messagebox

class Window():
	def __init__(self):
		self.labels = [''] * 28
		for i in range (len(self.labels)):
			self.labels[i] = Label(root,
				font = ('Comic Sans MS', 16),
				bg = '#DDAC46',
				fg = '#9B23A9'
			)
		self.labels[27]['text'] = 'Цена перевозки:'
		self.labels[27].place(x = 150, y = 1)
		self.enters = [''] * 15
		for i in range (len(self.enters)):
			self.enters[i] = Entry(root, 
				font = ('Comic Sans MS', 16), 
				width = 2,
				justify = CENTER,
				relief = FLAT,
				bg = '#9c9b90'
			)

		self.labels[0]['text'] = 'A1 ='
		self.labels[0].place(x = 10, y = 30)
		self.labels[1]['text'] = 'A2 ='
		self.labels[1].place(x = 10, y = 90)
		self.labels[2]['text'] = 'A3 ='
		self.labels[2].place(x = 10, y = 160)
		self.labels[3]['text'] = 'B1 ='
		self.labels[3].place(x = 75, y = 220)
		self.labels[4]['text'] = 'B2 ='
		self.labels[4].place(x = 160, y = 220)
		self.labels[5]['text'] = 'B3 ='
		self.labels[5].place(x = 245, y = 220)
		self.labels[6]['text'] = 'U1 ='
		self.labels[6].place(x = 380, y = 30)
		self.labels[7]['text'] = 'U2 ='
		self.labels[7].place(x = 380, y = 90)
		self.labels[8]['text'] = 'U3 ='
		self.labels[8].place(x = 380, y = 160)
		self.labels[9]['text'] = 'V1 ='
		self.labels[9].place(x = 90, y = 270)
		self.labels[10]['text'] = 'V2 ='
		self.labels[10].place(x = 190, y = 270)
		self.labels[11]['text'] = 'V3 ='
		self.labels[11].place(x = 290, y = 270)
		self.enters[0].place(x = 60, y = 33)
		self.enters[1].place(x = 60, y = 93)
		self.enters[2].place(x = 60, y = 163)
		self.enters[3].place(x = 130, y = 223)
		self.enters[4].place(x = 215, y = 223)
		self.enters[5].place(x = 300, y = 223)
		self.enters[6].place(x = 130, y = 33)
		self.labels[12].place(x = 160, y = 30)
		self.enters[7].place(x = 130, y = 93)
		self.labels[13].place(x = 160, y = 90)
		self.enters[8].place(x = 130, y = 163)
		self.labels[14].place(x = 160, y = 160)
		self.enters[9].place(x = 215, y = 33)
		self.labels[15].place(x = 245, y = 30)
		self.enters[10].place(x = 215, y = 93)
		self.labels[16].place(x = 245, y = 90)
		self.enters[11].place(x = 215, y = 163)
		self.labels[17].place(x = 245, y = 160)
		self.enters[12].place(x = 300, y = 33)
		self.labels[18].place(x = 330, y = 30)
		self.enters[13].place(x = 300, y = 93)
		self.labels[19].place(x = 330, y = 90)
		self.enters[14].place(x = 300, y = 163)
		self.labels[20].place(x = 330, y = 160)
		self.labels[21].place(x = 430, y = 30)
		self.labels[22].place(x = 430, y = 90)
		self.labels[23].place(x = 430, y = 160)
		self.labels[24].place(x = 140, y = 270)
		self.labels[25].place(x = 240, y = 270)
		self.labels[26].place(x = 340, y = 270)

		self.button = Button(root,
			font = ('Comic Sans MS', 12),
			fg = '#e4c510',
			bg = '#2723A9',
			text = 'Рассчет'
		)
		self.button.bind('<ButtonRelease-1>', self.main)
		self.button.place(x = 390, y = 240)

	def Circle(self, y, x):
		hor = []
		ver = []
		def getHorizontal():
			for i in range (len(self.B)):
				if i != x and self.PLAN[y][i] != '-':
					hor.append(i)
		def getVertical():
			for i in range (len(self.A)):
				if i != y and self.PLAN[i][x] != '-':
					ver.append(i)
		getHorizontal()
		getVertical()
		for i in ver:
			for j in hor:
				if self.PLAN[i][j] != '-':
					return [ [y, x], [y, j], [i, x], [i, j] ]   

	def checkOptimum(self):
		for i in range(len(self.deltaC)):
			for j in range(len(self.deltaC[i])):
				if self.deltaC[i][j] < 0:
					return False
		return True

	def main(self, event):
		
		for i in range(len(self.enters)):
			if self.enters[i].get() == '':
				messagebox.showerror("Ошибка внесенных данных", "Уточните входные параметры")
				return

		# ШАГ 1
		try:
			self.C = [[int(self.enters[6].get()), int(self.enters[9].get()), int(self.enters[12].get())],
					  [int(self.enters[7].get()), int(self.enters[10].get()), int(self.enters[13].get())],
					  [int(self.enters[8].get()), int(self.enters[11].get()), int(self.enters[14].get())]]
			self.A = [int(self.enters[0].get()), int(self.enters[1].get()), int(self.enters[2].get())]
			self.B = [int(self.enters[3].get()), int(self.enters[4].get()), int(self.enters[5].get())]
		except:
			messagebox.showerror("Ошибка", "Внесены данные, которые не удается обработать\nОбратите внимание, что вносимые данные должны быть целыми числами")
			return

		for i in range(len(self.enters)):
			if int(self.enters[i].get()) < 1:
				messagebox.showerror("Ошибка внесенных данных", "Уточните входные параметры")
				return
		'''
		self.C = [
				[5, 10, 7],
				[10, 0, 0],
				[3, 12, 8]
		]
		self.A = [10, 20, 30]
		self.B = [15, 20, 25]
		'''
		self.deltaC = []
		self._deltaC = []
		self.PLAN = [['-' for i in range(len(self.A))] for j in range(len(self.B))]
		self._A = self.A.copy()
		self._B = self.B.copy()

		# ШАГ 2
		if not (sum(self.A) == sum(self.B)):
			messagebox.showerror("Ошибка", "Сумма элементов вектора A должна быть равна сумме элементов вектора B")
			return


		# ШАГ 3
		arr = [0] * len(self.C) * len(self.C[0])
		index = 0
		for i in range(len(self.C)):
			for j in range(len(self.C[i])):
				arr[index] = [self.C[i][j], [i, j]]
				index += 1

		for i in range(len(arr) - 1):
			for j in range(len(arr) - i - 1):
				if arr[j][0] > arr[j+1][0]:
					arr[j], arr[j+1] = arr[j+1], arr[j]

		boo = False
		for i in range(len(arr)):
			if (sum(self._A) == 0 and sum(self._B) == 0) or (boo):
				break
			top = arr[i][1][0]
			gor = arr[i][1][1]

			if (self._A[top] < self._B[gor]) and (self._A[top] != 0):
				self.PLAN[top][gor] = self._A[top]
				self._B[gor] -= self._A[top]
				self._A[top] = 0
			if (self._A[top] >= self._B[gor]) and (self._B[gor] != 0):
				self.PLAN[top][gor] = self._B[gor]
				self._A[top] -= self._B[gor]
				self._B[gor] = 0

		# ШАГ 4
		basis = []
		index = 0
		for i in range(len(self.PLAN)):
			for j in range(len(self.PLAN[i])):
				if self.PLAN[i][j] is not '-':
					index += 1
					basis.append([i, j])
		
		while index < len(self.A) + len(self.B) - 1:
			boo = True
			for i in range(len(self.A)):
				if boo:
					for j in range(len(self.B)):
						if self.Circle(i, j) == None and self.PLAN[i][j] == '-':
							self.PLAN[i][j] = 0
							boo = False
							break
			basis = []
			index = 0
			for i in range(len(self.PLAN)):
				for j in range(len(self.PLAN[i])):
					if self.PLAN[i][j] is not '-':
						index += 1
						basis.append([i, j])
		
		while True:
			# ШАГ 5
			U = [None] * len(self.A)
			V = [None] * len(self.B)
			U[basis[0][0]] = 0
			for k in range(len(basis)):
				for i in range(len(basis)):
					if U[basis[i][0]] == None and V[basis[i][1]] is not None:
						U[basis[i][0]] = self.C[basis[i][0]][basis[i][1]] - V[basis[i][1]]
					if V[basis[i][1]] == None and U[basis[i][0]] is not None:
						V[basis[i][1]] = self.C[basis[i][0]][basis[i][1]] - U[basis[i][0]]
			
			# ШАГ 6
			self.deltaC = []
			for i in range(len(self.C)):
				self.deltaC.append(self.C[i].copy())

			for i in range(len(self.A)):
				for j in range(len(self.B)):
					self.deltaC[i][j] = self.C[i][j] - (U[i] + V[j])
			
			# ШАГ 7
			if not self.checkOptimum():
				self._deltaC = []
				for i in range(len(self.deltaC)):
					for j in range(len(self.deltaC[i])):
						self._deltaC.append([self.deltaC[i][j], [i, j]])

			else:
				break
			min_deltaC = self._deltaC[0][0]
			koord_min_deltaC = self._deltaC[0][1]
			
			for i in range(len(self._deltaC)):
				if self._deltaC[i][0] <= min_deltaC:
					min_deltaC = self._deltaC[i][0]
					koord_min_deltaC = self._deltaC[i][1]

			args = self.Circle(koord_min_deltaC[0], koord_min_deltaC[1])
			try:
				par = min ( self.PLAN[ args[1][0] ][ args[1][1] ], self.PLAN[ args[2][0] ][ args[2][1] ] ) 
			except:
				messagebox.showerror("Неизвестная ошибка", "Невозможно обработать внесенные данные")
				return
			self.PLAN[ args[0][0] ][ args[0][1] ] = par
			self.PLAN[ args[1][0] ][ args[1][1] ] -= par
			self.PLAN[ args[2][0] ][ args[2][1] ] -= par
			self.PLAN[ args[3][0] ][ args[3][1] ] += par

			for i in range(len(self.PLAN)):
				for j in range(len(self.PLAN[i])):
					if self.PLAN[i][j] == 0:
						self.PLAN[i][j] = '-'

			# ШАГ 8
			if not self.checkOptimum():
				break

		# ШАГ 9
		Z = 0
		for i in range(len(self.PLAN)):
			for j in range(len(self.PLAN[i])):
				if self.PLAN[i][j] != '-':
					Z += self.PLAN[i][j] * self.C[i][j]

		self.labels[12]['text'] = self.PLAN[0][0]
		self.labels[13]['text'] = self.PLAN[1][0]
		self.labels[14]['text'] = self.PLAN[2][0]
		self.labels[15]['text'] = self.PLAN[0][1]
		self.labels[16]['text'] = self.PLAN[1][1]
		self.labels[17]['text'] = self.PLAN[2][1]
		self.labels[18]['text'] = self.PLAN[0][2]
		self.labels[19]['text'] = self.PLAN[1][2]
		self.labels[20]['text'] = self.PLAN[2][2]
		
		self.labels[21]['text'] = U[0]
		self.labels[22]['text'] = U[1]
		self.labels[23]['text'] = U[2]

		self.labels[24]['text'] = V[0]
		self.labels[25]['text'] = V[1]
		self.labels[26]['text'] = V[2]

		child = Tk()
		margin_x = (child.winfo_screenwidth() - child.winfo_reqwidth()) / 2 - 480 / 4
		margin_y = (child.winfo_screenheight() - child.winfo_reqheight()) / 2 - 320 / 4
		child.title('Граф перевозок')
		child.iconbitmap("C:\\Users\\asus\\Desktop\\7\\2.ico")
		child.wm_geometry("480x320")
		child.config(bg  = '#06D076')
		child.resizable(width=False, height=False)
		c = Canvas(child, width=480, height=320, bg='#06D076')
		c.pack()
		c.create_text(165, 20, anchor=W, font=("Comic Sans MS", 14), text="Стоимость: " + str(Z), fill="#7E62BC")

		c.create_oval(50, 50, 100, 100, width=2, outline="#EB7400")
		c.create_text(65, 75, anchor=W, font=("Comic Sans MS", 14), text="A1", fill="#EB7400")
		c.create_oval(200, 50, 250, 100, width=2, outline="#EB7400")
		c.create_text(215, 75, anchor=W, font=("Comic Sans MS", 14), text="A2", fill="#EB7400")
		c.create_oval(350, 50, 400, 100, width=2, outline="#EB7400")
		c.create_text(365, 75, anchor=W, font=("Comic Sans MS", 14), text="A3", fill="#EB7400")

		c.create_oval(50, 250, 100, 300, width=2, outline="#DAD2D2")
		c.create_text(65, 275, anchor=W, font=("Comic Sans MS", 14), text="B1", fill="#DAD2D2")
		c.create_oval(200, 250, 250, 300, width=2, outline="#DAD2D2")
		c.create_text(215, 275, anchor=W, font=("Comic Sans MS", 14), text="B2", fill="#DAD2D2")
		c.create_oval(350, 250, 400, 300, width=2, outline="#DAD2D2")
		c.create_text(365, 275, anchor=W, font=("Comic Sans MS", 14), text="B3", fill="#DAD2D2")

		for i in range(len(self.PLAN)):
			for j in range(len(self.PLAN[i])):
				if self.PLAN[i][j] != '-' and self.PLAN[i][j] != 0:
					if i == 0:
						xtop = 75
					if i == 1:
						xtop = 225
					if i == 2:
						xtop = 375
					ytop = 100
					ybot = 250
					if j == 0:
						xbot = 75
					if j == 1:
						xbot = 225
					if j == 2:
						xbot = 375
					c.create_line(xtop, ytop, xbot, ybot, fill='#212BCA', arrow=LAST, arrowshape="5 12 5", width = 2)
					c.create_text(xtop+30, ytop+ j*20 - 40, anchor=W, font=("Comic Sans MS", 14), text=str(self.PLAN[i][j]), fill="#2C726C")
		c.create_text(440, 60, anchor=W, font=("Comic Sans MS", 14), text="к B1", fill="#726565")
		c.create_text(440, 80, anchor=W, font=("Comic Sans MS", 14), text="к B2", fill="#726565")
		c.create_text(440, 100, anchor=W, font=("Comic Sans MS", 14), text="к B3", fill="#726565")
		child.mainloop()

root = Tk()
margin_x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 480 / 4
margin_y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 320 / 4
root.title('Задача транспортной логистики. Метод потенциалов')
root.wm_geometry("480x320+%d+%d" % (margin_x, margin_y))
root.config(bg  = '#DDAC46')
root.iconbitmap("C:\\Users\\asus\\Desktop\\7\\1.ico")
root.resizable(width=False, height=False)
obj = Window()
root.mainloop()