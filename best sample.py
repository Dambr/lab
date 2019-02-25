import numpy as np
import itertools
import random
import math
from tkinter import *
from tkinter import messagebox

class Window():

	def __init__(self):
		self.label_usl = Label(root,
			font = ('Arial', 16),
			text = 'Условия ограничения:',
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		self.label_usl.place(x = 10, y = 20)


		#widgetX = 10
		#widgetY = 10

		self.entry = [''] * 20
#		первая строка

		self.entry[1] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		self.entry[1].place(x = 10, y = 50)

		self.label_1 = Label(root,
			text = 'x +',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		self.label_1.place(x = 50, y = 45)

		self.entry[2] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		self.entry[2].place(x = 85, y = 50)

		self.label_2 = Label(root,
			text = 'y =',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_2['text'] = 'y   ='
		self.label_2.place(x = 125, y = 45)

		self.entry[3] = Entry(root,
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[3].insert(0, '3')
		#self.entry[3]['width'] = 3
		self.entry[3].place(x = 170, y = 50)

#		вторая строка

		self.entry[4] = Entry(root,
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[4].insert(0, '4')
		#self.entry[4]['width'] = 2
		self.entry[4].place(x = 10, y = 90)

		self.label_3 = Label(root,
			text = 'x +',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_3['text'] = 'x +'
		self.label_3.place(x = 50, y = 85)

		self.entry[5] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[4].insert(0, '5')
		#self.entry[5]['width'] = 2
		self.entry[5].place(x = 85, y = 90)

		self.label_4 = Label(root,
			text = 'y',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_4['text'] = 'y ='
		self.label_4.place(x = 125, y = 85)

		self.entry[13] = Entry(root,
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 2,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[13].insert(textvariable = '<=')
		#self.entry[13]['width'] = 3
		self.entry[13].place(x = 140, y = 90)

		self.entry[6] = Entry(root,
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[6].insert(0, '6')
		#self.entry[6]['width'] = 3
		self.entry[6].place(x = 170, y = 90)


#		третья строка

		self.entry[7] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[7].insert(0, '7')
		#self.entry[7]['width'] = 2
		self.entry[7].place(x = 10, y = 130)

		self.label_5 = Label(root,
			text = 'x +',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		self.label_5['text'] = 'x +'
		self.label_5.place(x = 50, y = 125)

		self.entry[8] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[8].insert(0, '8')
		#self.entry[8]['width'] = 2
		self.entry[8].place(x = 85, y = 130)

		self.label_6 = Label(root,
			text = 'y',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_6['text'] = 'y ='
		self.label_6.place(x = 125, y = 125)

		self.entry[14] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 2,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[14].insert(textvariable = '<=')
		#self.entry[14]['width'] = 3
		self.entry[14].place(x = 140, y = 130)

		self.entry[9] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[9].insert(0, '9')
		#self.entry[9]['width'] = 3
		self.entry[9].place(x = 170, y = 130)

#		четвертая строка

		self.entry[10] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[10].insert(0, '10')
		#self.entry[10]['width'] = 2
		self.entry[10].place(x = 10, y = 170)

		self.label_7 = Label(root,
			text = 'x +',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_7['text'] = 'x +'
		self.label_7.place(x = 50, y = 165)

		self.entry[11] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[11].insert(0, '11')
		#self.entry[11]['width'] = 2
		self.entry[11].place(x = 85, y = 170)

		self.label_8 = Label(root,
			text = 'y',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_8['text'] = 'y ='
		self.label_8.place(x = 125, y = 165)

		self.entry[15] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 2,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[15].insert(textvariable = '<=')
		#self.entry[15]['width'] = 3
		self.entry[15].place(x = 140, y = 170)

		self.entry[12] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[12].insert(0, '12')
		#self.entry[12]['width'] = 3
		self.entry[12].place(x = 170, y = 170)



################################################


		self.label_9 = Label(root,
			text = 'E =',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_9['text'] = 'E = '
		self.label_9.place(x = 380, y = 100)

		self.entry[16] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[16].insert(0, '14')
		#self.entry[16]['width'] = 4
		self.entry[16].place(x = 420, y = 103)

		self.label_10 = Label(root,
			text = 'H =',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_10['text'] = 'h = '
		self.label_10.place(x = 380, y = 150)

		self.entry[17] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[17].insert(0, '15')
		self.entry[17]['width'] = 4
		self.entry[17].place(x = 420, y = 153)


################################################

		self.label_11 = Label(root,
			text = 'Целевая функция',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_11['text'] = 'Целевая функция'
		self.label_11.place(x = 290, y = 10)

		self.entry[18] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 20,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[18].insert(0, '16')
		#self.entry[18]['width'] = 20
		self.entry[18].place(x = 280, y = 40)

################################################

		self.label_12 = Label(root,
			text = 'Ответ:',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_12['text'] = 'Ответ'
		self.label_12.place(x = 20, y = 200)

		self.label_13 = Label(root,
			text = 'x =',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_13['text'] = 'x = '
		self.label_13.place(x = 40, y = 230)

		self.label_14 = Label(root,
			text = 'y =',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_14['text'] = 'y = '
		self.label_14.place(x = 40, y = 260)

		self.label_15 = Label(root,
			text = 'Значение функции =',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_15['text'] = 'Значение функции = '
		self.label_15.place(x = 200, y = 230)

		self.label_16 = Label(root,
			text = 'Число пересчетов =',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_16['text'] = 'Число пересчетов = '
		self.label_16.place(x = 200, y = 260)


		self.label_17 = Label(root,
#			text = '0.162',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_17['text'] = 'x1'
		self.label_17.place(x = 100, y = 230)

		self.label_18 = Label(root,
#			text = '0.152',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_18['text'] = 'x2'
		self.label_18.place(x = 100, y = 260)

		self.label_19 = Label(root,
#			text = '0.162',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
#		self.label_19['text'] = 'w'
		self.label_19.place(x = 400, y = 230)

		self.label_20 = Label(root,
#			text = '0.152',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
#		self.label_20['text'] = 'ch'
		self.label_20.place(x = 400, y = 260)



#		21й лэйбл - число m

		self.label_21 = Label(root,
			text = 'M =',
			font = ('Arial', 14),
			bg = '#4c70d8',
			fg = '#e4cf10'
		)
		#self.label_21['text'] = 'M = '
		self.label_21.place(x = 380, y = 200)

		self.entry[19] = Entry(root, 
			textvariable = StringVar(root), 
			font = ('Arial', 12), 
			width = 4,
			justify = CENTER,
			relief = FLAT,
			bg = '#9c9b90'
		)
		#self.entry[19].insert(0, '16')
		#self.entry[19]['width'] = 3
		self.entry[19].place(x = 420, y = 203)

################################################
		self.button_add = Button(root,
			font = ('Arial', 12),
			fg = '#e4c510',
			bg = 'green'
		)
		self.button_add['text'] = 'Рассчитать'
		#self.button_add['width'] = 8
		#self.button_add['height'] = 2
		#self.button_add['font'] 
		self.button_add.bind('<ButtonRelease-1>',
			self.main
		)
		self.button_add.place(x = 250, y = 120)


	def f(self, function, x, y):
			return eval(function)

	def main(self, event):
		self.label_17['text'] = ''
		self.label_18['text'] = ''
		self.label_19['text'] = ''
		self.label_20['text'] = ''
		for i in range (1, 20):
			if self.entry[i].get() == '':
				messagebox.showinfo("Ошибка", "Не все поля заполнены")
				return

		#print(self.entry[1].get())
		signs = [self.entry[13].get(), self.entry[14].get(), self.entry[15].get(), '==']
		data = [
			[float(self.entry[4].get()), float(self.entry[5].get())],
			[float(self.entry[7].get()), float(self.entry[8].get())],
			[float(self.entry[10].get()), float(self.entry[11].get())],
			[float(self.entry[1].get()), float(self.entry[2].get())]
		]
		vals = [float(self.entry[6].get()), float(self.entry[9].get()), float(self.entry[12].get()), float(self.entry[3].get())]
		epsilonF = float(self.entry[16].get())
		h = float(self.entry[17].get())
		m = int(self.entry[19].get())
		change = 0
		arg = range(len(vals))
		x1 = []
		x2 = []
		for i in itertools.permutations(arg, 2):
			M = np.array([data[i[0]], data[i[1]]])
			V = np.array([vals[i[0]], vals[i[1]]])
			boo = True
			for j in range(len(vals)):
				if signs[j] == '>=':
					if not (data[j][0] * np.linalg.solve(M, V)[0] + data[j][1] * np.linalg.solve(M, V)[1] >= vals[j]):
						boo = False
				if signs[j] == '<=':
					if not (data[j][0] * np.linalg.solve(M, V)[0] + data[j][1] * np.linalg.solve(M, V)[1] <= vals[j]):
						boo = False
				if signs[j] == '==':
					if not (data[j][0] * np.linalg.solve(M, V)[0] + data[j][1] * np.linalg.solve(M, V)[1] == vals[j]):
						boo = False
			if boo and ((round(np.linalg.solve(M, V)[0], 2) not in x1) or (round(np.linalg.solve(M, V)[1], 2) not in x2)):
				x1.append(round(np.linalg.solve(M, V)[0], 2))
				x2.append(round(np.linalg.solve(M, V)[1], 2))
		print('x1:',[min(x1), max(x1)])
		print('x2:',[min(x2), max(x2)])
		print()
		while True:
			x = []
			w = []
			fi = [0] * m
			_x = [[0 for j in range(2)] for i in range(m)]
			r = 0
			h = 0.2
			x.append([0, 0])
			x[r][0] = round(random.uniform(min(x1), max(x1)), 2)
			x[r][1] = round(float((vals[len(vals) - 1] - data[len(data) - 1][0]*x[r][0])/data[len(data) - 1][1]), 2)
			w.append(round(self.f(self.entry[18].get(),x[r][0], x[r][1]), 2))
			while True:
				x.append([0, 0])
				sigmas = [round(random.uniform(-1, 1), 5) for s in range(m)]
				for i in range(m):
					_x[i][0] = round(x[r][0] + h * sigmas[i], 4)
					_x[i][1] = round(float((vals[len(vals) - 1] - data[len(data) - 1][0]*_x[i][0])/data[len(data) - 1][1]), 4)
					fi[i] = round(self.f(self.entry[18].get(),_x[i][0], _x[i][1]), 2) 
				w.append(max(fi))
				x[r+1][0] = _x[fi.index(max(fi))][0]
				x[r+1][1] = _x[fi.index(max(fi))][1]
				r += 1
				if (w[len(w) - 1] < w[len(w) - 2]) or ( ( (min(x1) > x[r][0]) or (max(x1) < x[r][0]) ) or ( (min(x2) > x[r][1]) or (max(x2) < x[r][1]) ) ):
					break


			for i in range(len(x)):
				if not ((min(x1) <= x[i][0] <= max(x1)) or (min(x2) <= x[i][1] <= max(x2))):
					x.remove(x[i])
					w.remove(w[i])

			if round(math.fabs(w[len(w) - 1] - w[len(w) - 2]), 3) <= epsilonF:
				break
			
			else:
				h = h * 0.5
				change += 1

		self.label_17['text'] = str(round(x[w.index(max(w))][0], 2))
		self.label_18['text'] = str(round(x[w.index(max(w))][1], 2))
		self.label_19['text'] = str(max(w))
		self.label_20['text'] = str(change)
		#print(max(w))
		#print(x[w.index(max(w))])
		#print(change)

root = Tk()
margin_x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2 - 480 / 4
margin_y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2 - 320 / 4
root.title('Метод наилучшей пробы')
root.wm_geometry("480x320+%d+%d" % (margin_x, margin_y))
root.config(bg  = '#4c70d8')
root.resizable(width=False, height=False)
obj = Window()
root.mainloop()