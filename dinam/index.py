from tkinter import *
import numpy as np
import random
import json
import math
class Window():
	def __init__(self):
		self.labels = ['X'] * 26
		for i in range( len( self.labels ) ):
			self.labels[i] = Label( root,
				font = ( 'Comic Sans MS', 16 ),
				bg = '#DDAC46',
				fg = '#9B23A9',
				# width = 2
			)
		self.labels[0]['text'] = 'Метод Монте-Карло:'
		self.labels[0].place(x = 10, y = 40)

		self.labels[1]['text'] = 'Муравьиный алгоритм:'
		self.labels[1].place(x = 10, y = 120)

		self.labels[2].place(x = 10, y = 80)
		self.labels[3].place(x = 10, y = 160)

		self.labels[4]['text'] = 'Результат:'
		self.labels[4].place(x = 400, y = 40)

		self.labels[5].place(x = 400, y = 80)
		self.labels[6].place(x = 400, y = 160)

		self.button = Button(root,
			font = ('Comic Sans MS', 12),
			fg = '#e4c510',
			bg = '#2723A9',
			text = 'Рассчет'
		)
		self.button.bind('<ButtonRelease-1>', self.main)
		self.button.place(x = 10, y = 200)

	def main(self, event):
		self.labels[2]['text'] = self.m()[1]
		self.labels[3]['text'] = self.m()[1]
		self.labels[5]['text'] = self.m()[0]
		self.labels[6]['text'] = self.m()[0]
	
	def a(self):
		with open('config.json') as f:
			config = json.load(f)
		M = np.array(config['cities'])
		M1 = M + M.T
		a = 1
		b = 2
		Q = 1
		Tau = M1.copy()
		for i in range(len(Tau)):
			for j in range(len(Tau[i])):
				if i != j:
					Tau[i][j] = 1

		P = M1.copy()
		# sum
		for t in range(1, 2000):
			s = 0
			for i in range(len(P)):
				for j in range(len(P[i])):
					if i != j:
						s += (math.pow(1/M1[i][j], b) * math.pow(Tau[i][j], a))
			for i in range(len(P)):
				for j in range(len(P[i])):
					if i != j:
						P[i][j] = 100 * (math.pow(1/M1[i][j], b) * math.pow(Tau[i][j], a)) / s
			for i in range(len(Tau)):
				for j in range(len(Tau[i])):
					if i != j:
						Tau[i][j] += Q / s
		return [M1, P]
	
	def m(self):
		origin = 0
		with open('config.json') as f:
			config = json.load(f)
		M = np.array(config['cities'])

		M1 = M + M.T

		M1 = M1

		Ngor = len(M1)
		Nbros = 1000

		def spisok(q):
			x_i = []
			for i in range(Ngor):
				x_i.append(i)
			for i in range(1, Ngor):
				a = random.randint(0, Ngor - 1)
				if a != i:
					q = x_i[a]
					x_i[a] = x_i[i]
					x_i[i] = q
			return x_i
		sum = []
		# Sum
		n = 1
		Smin = 999999
		put = 0
		while n <= Nbros:
			S = 0
			sp = spisok(1)
			for i in range(Ngor - 1):
				S = S + M1[sp[i+1]][sp[i]]
			S = S + M1[sp[1]][sp[Ngor-1]]
			if Smin > S:
				Smin = S
				put = sp
			n = n + 1
		return [Smin, put]

root = Tk()
margin_x = (root.winfo_screenwidth() - root.winfo_reqwidth())
margin_y = (root.winfo_screenheight() - root.winfo_reqheight())
root.title('Задача транспортной логистики. Метод потенциалов')
root.wm_geometry('560x270+%d+%d' % (margin_x/3, margin_y/3))
root.config(bg  = '#DDAC46')
root.resizable(width=False, height=False)
obj = Window()
root.mainloop()