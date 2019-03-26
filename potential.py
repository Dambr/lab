# Задача транспортной логистики
# Метод потенциалов
# Метод Фогеля (аппроксимация Фогеля)

from tkinter import *
from tkinter import messagebox

class Window():
	def __init__(self):
		self.labels = ['X'] * (26)
		self.enters = [''] * (23)
		for i in range( len( self.labels ) ):
			self.labels[ i ] = Label( root,
				font = ( 'Comic Sans MS', 16 ),
				bg = '#DDAC46',
				fg = '#9B23A9',
				width = 2
			)
		for i in range( len( self.enters ) ):
			self.enters[ i ] = Entry( root, 
				font = ('Comic Sans MS', 16 ), 
				width = 2,
				justify = CENTER,
				bg = '#9c9b90',
				borderwidth = '2',
				relief = 'solid'
			)
		for i in range(11, 26):
			self.labels[ i ][ 'borderwidth' ] = 2
			self.labels[ i ][ 'relief' ] = 'solid',

		#	Первый столбец
		
		self.labels[ 1 ][ 'text' ] = 'A1'
		self.labels[ 1 ].place( x = 40, y = 60 )

		self.labels[ 2 ][ 'text' ] = 'A2'
		self.labels[ 2 ].place( x = 40, y = 110 )

		self.labels[ 3 ][ 'text' ] = 'A3'
		self.labels[ 3 ].place( x = 40, y = 160 )

		self.labels[ 4 ][ 'text' ] = 'Потреб.'
		self.labels[ 4 ][ 'width' ] = 6
		self.labels[ 4 ].place( x = 10, y = 210 )

		#	Первая строка

		self.labels[ 5 ][ 'text' ] = 'B1'
		self.labels[ 5 ].place( x = 130, y = 10 )

		self.labels[ 6 ][ 'text' ] = 'B2'
		self.labels[ 6 ].place( x = 200, y = 10 )

		self.labels[ 7 ][ 'text' ] = 'B3'
		self.labels[ 7 ].place( x = 270, y = 10 )

		self.labels[ 8 ][ 'text' ] = 'B4'
		self.labels[ 8 ].place( x = 340, y = 10 )

		self.labels[ 9 ][ 'text' ] = 'B5'
		self.labels[ 9 ].place( x = 410, y = 10 )

		self.labels[ 10 ][ 'text' ] = 'Запасы'
		self.labels[ 10 ][ 'width' ] = 6
		self.labels[ 10 ].place( x = 460, y = 10 )

		#	Последний столбец

		self.enters[ 0 ][ 'width' ] = 3
		self.enters[ 0 ].place( x = 480, y = 60 )

		self.enters[ 1 ][ 'width' ] = 3
		self.enters[ 1 ].place( x = 480, y = 110 )

		self.enters[ 2 ][ 'width' ] = 3
		self.enters[ 2 ].place( x = 480, y = 160 )

		#	Последняя строка

		self.enters[ 3 ][ 'width' ] = 3
		self.enters[ 3 ].place( x = 125, y = 210 )

		self.enters[ 4 ][ 'width' ] = 3
		self.enters[ 4 ].place( x = 195, y = 210 )

		self.enters[ 5 ][ 'width' ] = 3
		self.enters[ 5 ].place( x = 265, y = 210 )

		self.enters[ 6 ][ 'width' ] = 3
		self.enters[ 6 ].place( x = 335, y = 210 )

		self.enters[ 7 ][ 'width' ] = 3
		self.enters[ 7 ].place( x = 405, y = 210 )

		#	Enters  в матрице
			# Первая строка
		self.enters[ 8 ].place( x = 110, y = 60 )
		self.enters[ 9 ].place( x = 180, y = 60 )
		self.enters[ 10 ].place( x = 250, y = 60 )
		self.enters[ 11 ].place( x = 320, y = 60 )
		self.enters[ 12 ].place( x = 390, y = 60 )
			# Вторая строка
		self.enters[ 13 ].place( x = 110, y = 110 )
		self.enters[ 14 ].place( x = 180, y = 110 )
		self.enters[ 15 ].place( x = 250, y = 110 )
		self.enters[ 16 ].place( x = 320, y = 110 )
		self.enters[ 17 ].place( x = 390, y = 110 )
			# Третья строка
		self.enters[ 18 ].place( x = 110, y = 160 )
		self.enters[ 19 ].place( x = 180, y = 160 )
		self.enters[ 20 ].place( x = 250, y = 160 )
		self.enters[ 21 ].place( x = 320, y = 160 )
		self.enters[ 22 ].place( x = 390, y = 160 )

		#	Labels в матрице
			# Первая строка
		self.labels[ 11 ]. place( x = 140, y = 60 )
		self.labels[ 12 ]. place( x = 210, y = 60 )
		self.labels[ 13 ]. place( x = 280, y = 60 )
		self.labels[ 14 ]. place( x = 350, y = 60 )
		self.labels[ 15 ]. place( x = 420, y = 60 )
			# Вторая строка
		self.labels[ 16 ]. place( x = 140, y = 110 )
		self.labels[ 17 ]. place( x = 210, y = 110 )
		self.labels[ 18 ]. place( x = 280, y = 110 )
		self.labels[ 19 ]. place( x = 350, y = 110 )
		self.labels[ 20 ]. place( x = 420, y = 110 )
			# Третья строка
		self.labels[ 21 ]. place( x = 140, y = 160 )
		self.labels[ 22 ]. place( x = 210, y = 160 )
		self.labels[ 23 ]. place( x = 280, y = 160 )
		self.labels[ 24 ]. place( x = 350, y = 160 )
		self.labels[ 25 ]. place( x = 420, y = 160 )

		self.button = Button(root,
			font = ('Comic Sans MS', 12),
			fg = '#e4c510',
			bg = '#2723A9',
			text = 'Рассчет'
		)
		self.button.bind('<ButtonRelease-1>', self.main)
		self.button.place(x = 467, y = 207)

		


	def vertical( self, arg ):
		'''
		Функция принимает на вход координату точки.
		Возвращает следующую точку цикла по вертикали.
		'''
		dots = []
		for i in range( len( self.A ) ):
			if self.PLAN[ i ][ arg[ 1 ] ] is not '-' and self.PLAN[ i ][ arg[ 1 ] ] is not '+' and [ i, arg[ 1 ] ] not in self.cickle:
				dots.append( [ i, arg[ 1 ] ] )
		for i in range( len( dots ) ):
			for j in range( len( self.B ) ):
				if j != dots[ i ][ 1 ] and self.PLAN[ dots[ i ][ 0 ] ][ j ] != '-':
					answer = dots[ i ]
		return answer

	def horizontal( self, arg ):
		'''
		Функция принимает на вход координату точки.
		Возвращает следующую точку цикла по горизонтали.
		'''
		dots = []
		for i in range( len( self.B ) ):
			if self.PLAN[ arg[ 0 ] ][ i ] is  not '-' and [ arg[ 0 ], i ] not in self.cickle:
				dots.append( [ arg[ 0 ], i ] )
		for i in range( len( dots ) ):
			for j in range( len( self.A ) ):
				if j != dots[ i ][ 0 ] and self.PLAN[ j ][ dots[ i ][ 1 ] ] != '-':
					answer = dots[ i ]
		return answer

	def delta( self, arr ):
		'''
		Функция принимает на вход вектор.
		Возвращает модуль разницы между двумя минимальными элементами вектора.
		Если в вектора два минимальных элемента, то вернет 0.
		'''
		a = min( arr )
		arr[ arr.index( a ) ] = max( arr )
		b = min( arr )
		return a - b if a > b else b - a

		#		Шаг 1. Дано

	def main( self, event ):
		try:
			self.A = [ int( self.enters[0].get() ), int( self.enters[1].get() ), int( self.enters[2].get() ) ]
			self.B = [ int( self.enters[3].get() ), int( self.enters[4].get() ), int( self.enters[5].get() ), int( self.enters[6].get() ), int( self.enters[7].get() ) ]
			self.C = [
				[ int( self.enters[8].get() ), int( self.enters[9].get() ), int( self.enters[10].get() ), int( self.enters[11].get() ), int( self.enters[12].get() ) ],
				[ int( self.enters[13].get() ), int( self.enters[14].get() ), int( self.enters[15].get() ), int( self.enters[16].get() ), int( self.enters[17].get() ) ],
				[ int( self.enters[18].get() ), int( self.enters[19].get() ), int( self.enters[20].get() ), int( self.enters[21].get() ), int( self.enters[22].get() ) ]
			]
		except:
			messagebox.showinfo('Ошибка', 'Внесены данные, которые не удается обработать.')
			return
		'''
			# Задаем вектов А
		self.A = [ 10, 15, 25 ]

			# Задачем вектор В
		self.B = [ 10, 4, 14, 6, 16 ]

			# Матрица С
		self.C = [
			[ 15, 8, 9, 11, 12 ],
			[ 4, 10, 7, 5, 8 ],
			[ 6, 3, 4, 15, 20 ]
		]
		'''
			# Дельты C
		self.deltaC = []

			# Первоначальный план пуст
		self.PLAN = [ [ '-' for i in range( len( self.B ) ) ] for j in range( len( self.A ) ) ]

			#		Шаг 2. Проверка задачи на закрытость

		if sum( self.A ) != sum( self.B ):
			#print( 'Задача является открытой' )
			messagebox.showerror('Ошибка!', 'Задача является открытой')
			return

			#		Шаг 3. Составление опорного плана
			#		Используется метод Фогеля (аппроксимация Фогеля)

		while sum( self.A ) != 0 and sum( self.B ) != 0:
				# Массив дельт по столбцу
			dI = [ 0 ] * len( self.A )

				# Массив дельт по строке
			dJ = [ 0 ] * len( self.B )

				# Заполняем массив dI
			for i in range( len( self.A ) ):
				arg = []
				for j in range( len( self.B ) ):
					if self.PLAN[i][j] is '-':
						arg.append( self.C[ i ][ j ] )
				if len( arg ) != 0:
					dI[ i ] = self.delta( arg )
				else:
					dI[i] = -1

				# Заполняем массив dJ
			for i in range( len( self.B ) ):
				arg = []
				
				for j in range( len( self.A ) ):
					if self.PLAN[ j ][ i ] is '-':
						arg.append( self.C[ j ][ i ] )
				if len( arg ) != 0:
					dJ[ i ] = self.delta( arg )
				else:
					dJ[ i ] = -1

				# Ищем позицию плана, которая соответствует пересечению максимальной дельты
				# и минимального тарифного плана

			if max( dJ ) > max( dI ):
				Stb = []
				for i in range( len( self.A ) ):
					if self.PLAN[ i ][ dJ.index(  max( dJ ) ) ] is '-':
						Stb.append( [ self.C[ i ][ dJ.index(  max( dJ ) ) ], [ i, dJ.index(  max( dJ ) ) ] ] )
				if  self.A[ min( Stb )[ 1 ][ 0 ] ] > self.B[ min( Stb )[ 1 ][ 1 ] ]:
					self.PLAN[ min( Stb )[ 1 ][ 0 ] ][ min( Stb )[ 1 ][ 1 ] ] = self.B[ min( Stb )[ 1 ][ 1 ] ]
					self.A[ min( Stb )[ 1 ][ 0 ] ] -= self.B[ min( Stb )[ 1 ][ 1 ] ]
					self.B[ min( Stb )[ 1 ][ 1 ] ] = 0
					for i in range( len( self.A ) ):
						if self.PLAN[ i ][ min( Stb )[ 1 ][ 1 ] ] is '-':
							self.PLAN[ i ][ min( Stb )[ 1 ][ 1 ] ] = '+'
				else:
					self.PLAN[ min( Stb )[ 1 ][ 0 ] ][ min( Stb )[ 1 ][ 1 ] ] = self.A[ min( Stb )[ 1 ][ 0 ] ]
					self.B[ min( Stb )[ 1 ][ 1 ] ] -= self.A[ min( Stb )[ 1 ][ 0 ] ]
					self.A[ min( Stb )[ 1 ][ 0 ] ] = 0
					for i in range( len ( self.B ) ):
						if self.PLAN[ min( Stb )[ 1 ][ 0 ] ][ i ] is '-':
							self.PLAN[ min( Stb )[ 1 ][ 0 ] ][ i ] = '+'
			else:
				Str = []
				for i in range( len( self.B ) ):
					if self.PLAN[ dI.index(  max( dI ) ) ][ i ] is '-':
						Str.append( [ self.C[ dI.index(  max( dI ) ) ][ i ], [ i ,  dI.index(  max( dI ) ), i ] ] )
				if self.A[ min( Str )[ 1 ][ 1 ] ] > self.B[ min( Str )[ 1 ][ 0 ] ]:
					self.PLAN[ min( Str )[ 1 ][ 1 ] ][ min( Str )[ 1 ][ 0 ] ] = self.B[ min( Str )[ 1 ][ 0 ] ]
					self.A[ min( Str )[ 1 ][ 1 ] ] -= self.B[ min( Str )[ 1 ][ 0 ] ]
					self.B[ min( Str )[ 1 ][ 0 ] ] = 0
					for i in range( len( self.A ) ):
						if self.PLAN[ i ][ min( Str )[ 1 ][ 0 ] ] is '-':
							self.PLAN[ i ][ min( Str )[ 1 ][ 0 ] ] = '+'
				else:
					self.PLAN[ min( Str )[ 1 ][ 1 ] ][ min( Str )[ 1 ][ 0 ] ] = self.A[ min( Str )[ 1 ][ 1 ] ]
					self.B[ min( Str )[ 1 ][ 0 ] ] -= self.A[ min( Str )[ 1 ][ 1 ] ]
					self.A[ min( Str )[ 1 ][ 1 ] ] = 0
					for i in range( len( self.B ) ):
						if self.PLAN[ min( Str )[ 1 ][ 1 ] ][ i ] is '-':
							self.PLAN[ min( Str )[ 1 ][ 1 ] ][ i ] = '+'
			
			#	Шаг 4. Проверка опорного плана на вырожденность

		count = 0
		for i in range( len( self.PLAN ) ):
			for j in range( len( self.PLAN[ i ] ) ):
				if self.PLAN[ i ][ j ] is '+':
					self.PLAN[ i ][ j ] = '-'
				else:
					count += 1

		if count < len( self.A ) + len( self.B ) - 1:
			#messagebox.showerror('Ошибка', 'План вырожденный')
			return
			for i in range ( len( self.PLAN ) ):
				for j in range ( len( self.PLAN[ i ] ) ):
					self.cickle = []
					self.cickle.append( self.vertical( [i, j] ) )
					while True:
						if self.cickle[ len( self.cickle ) - 1 ][ 0 ] is  i and self.cickle[ len( self.cickle ) - 1 ][ 1 ] is j:
							break
						self.cickle.append( self.horizontal( self.cickle[ len( self.cickle ) - 1 ] ) )
						if self.cickle[ len( self.cickle ) - 1 ][ 0 ] is  i and self.cickle[ len( self.cickle ) - 1 ][ 1 ] is j:
							break
						self.cickle.append( self.vertical( self.cickle[ len( self.cickle ) - 1 ] ) )

		while True:
			# Задаем базисные точки
			basis = []
			for i in range( len( self.PLAN ) ):
				for j in range( len( self.PLAN[ i ] ) ):
					if self.PLAN[ i ][ j ] != '-':
						basis.append( [ i, j ] )

				#	Шаг 5. Вычисление потенциалов для плана перевозки
				# Задание первоначальных неопределенных потенциалов

			U = [ None ] * len( self.A )
			V = [ None ] * len( self.B )
				# Принимаем первый потенциал U за 0
			U[ basis[ 0 ][ 0 ] ] = 0
				# Вычисление остальных потенциалов
			for k in range( len( basis ) ):
				for i in range( len( basis ) ):
					if U[ basis[ i ][ 0 ] ] is None and V[ basis[ i ][ 1 ] ] is not None:
						U[ basis[ i ][ 0 ] ] = self.C[ basis[ i ][ 0 ] ][ basis[ i ][ 1 ] ] - V[ basis[ i ][ 1 ] ]
					if V[ basis[ i ][ 1 ] ] is None and U[ basis[ i ][ 0 ] ] is not None:
						V[ basis[ i ][ 1 ] ] = self.C[ basis[ i ][ 0 ] ][ basis[ i ][ 1 ] ] - U[ basis[ i ][ 0 ] ]
			
				#	Шаг 6. Проверка плана на оптимальность

			self.deltaC = []
			for i in range( len( self.C ) ):
				for j in range( len( self.C[i] ) ):
					self.deltaC.append( [ self.C[ i ][ j ] - U[ i ] - V[ j ], [ i, j ] ] )

				# Проверка плана маршрута на оптимальность
			if min( self.deltaC )[ 0 ] >= 0:
				break

			self.PLAN[ min( self.deltaC )[ 1 ][ 0 ] ][ min( self.deltaC )[ 1 ][ 1 ] ] = '+'

				#	Шаг 7. Перераспределение поставок
			self.cickle = []
			self.cickle.append( self.vertical( [ min( self.deltaC )[ 1 ][ 0 ], min( self.deltaC )[ 1 ][ 1 ] ] ) )
			while True:
				if self.cickle[ len( self.cickle ) - 1 ][ 0 ] is  min( self.deltaC )[ 1 ][ 0 ] and self.cickle[ len( self.cickle ) - 1 ][ 1 ] is min( self.deltaC )[ 1 ][ 1 ]:
					break
				self.cickle.append( self.horizontal( self.cickle[ len( self.cickle ) - 1 ] ) )
				if self.cickle[ len( self.cickle ) - 1 ][ 0 ] is  min( self.deltaC )[ 1 ][ 0 ] and self.cickle[ len( self.cickle ) - 1 ][ 1 ] is min( self.deltaC )[ 1 ][ 1 ]:
					break
				self.cickle.append( self.vertical( self.cickle[ len( self.cickle ) - 1 ] ) )

			self.PLAN[ self.cickle[ len( self.cickle ) - 1 ][ 0 ] ][ self.cickle[ len( self.cickle ) - 1 ][ 1 ] ] = 0
			
				# Обозначим массив со знаком минус и заполним его
			minus = []
			for i in range( 0, len( self.cickle ), 2 ):
				minus.append( self.cickle[ i ] )
			
				# Обозначим массив со знаком плюс и заполним его
			plus = []
			for i in range( 1, len( self.cickle ), 2 ):
				plus.append( self.cickle[ i ] )
			
				# Сопоставим значения плана его отрицательным пунктам маршрута
			pminus = minus.copy()
			for i in range( len( minus ) ):
				pminus[ i ] = self.PLAN[ minus[ i ][ 0 ] ][ minus[ i ][ 1 ] ]

				# Находим минимальный минимальный элемент из массива pminus.
				# Вычитаем его значение из всех отрицательных элементов плана.
				# Прибавляем его значение ко всем положительным элементам плана
			for i in range( len( minus ) ):
				self.PLAN[ minus[ i ][ 0 ] ][ minus[ i ][ 1 ] ] -= min( pminus )
				if self.PLAN[ minus[ i ][ 0 ] ][ minus[ i ][ 1 ] ] is 0:
					self.PLAN[ minus[ i ][ 0 ] ][ minus[ i ][ 1 ] ] = '-'
			for i in range( len( plus ) ):
				self.PLAN[ plus[ i ][ 0 ] ][ plus[ i ][ 1 ] ] += min( pminus )
			#	Шаг 8. Переходим к пункту 5

			#	Шаг 9. Вычисляем общие затраты на перевозку

		Z = 0
		for i in range( len( self.PLAN ) ):
			for j in range( len( self.PLAN[ i ] ) ):
				if self.PLAN[i][j] is not '-':
					Z += self.PLAN[i][j] * self.C[i][j]

		for i in range( len( self.PLAN ) ):
			for j in range( len( self.PLAN[ i ] ) ):
				self.labels[ 11 + ( j + i * 5 ) ][ 'text' ] = self.PLAN[ i ][ j ]


		child = Tk()
		child.title('Граф перевозок')
		child.iconbitmap('2.ico')
		child.wm_geometry('680x320')
		child.config(bg  = '#06D076')
		child.resizable(width=False, height=False)
		c = Canvas(child, width=680, height=320, bg='#06D076')
		c.pack()
		c.create_text(285, 20, anchor=W, font=('Comic Sans MS', 14), text='Стоимость: ' + str(Z), fill='#7E62BC')
		for i in range( len( self.B ) ):
			c.create_oval(25 + i * 125, 50, 75 + i * 125, 100, width=2, outline='#EB7400')
			c.create_text(40 + i * 125, 75, anchor=W, font=('Comic Sans MS', 14), text='B' + str( i + 1 ), fill='#EB7400')
		for i in range( len( self.A ) ):
			c.create_oval(155 + i * 125, 250, 205 + i * 125, 300, width=2, outline='#DAD2D2')
			c.create_text(170 + i * 125,  275, anchor=W, font=('Comic Sans MS', 14), text='A' + str( i + 1 ), fill='#DAD2D2')
		for i in range( len( self.PLAN ) ):
			for j in range( len( self.PLAN[ i ] ) ):
				if self.PLAN[i][j] != '-' and self.PLAN[i][j] != 0:
					xtop = 50 + j * 125
					ytop = 100
					xbot = 180 + i * 125
					ybot = 250
					c.create_line(xbot, ybot, xtop, ytop, fill='#212BCA', arrow=LAST, arrowshape='5 12 5', width = 2)
					c.create_text(xtop+30, ytop + ( i - ( len( self.B ) - len( self.A ) ) )*20, anchor=W, font=('Comic Sans MS', 14), text=str(self.PLAN[i][j]), fill='#2C726C')
			c.create_text(620, 60 + i * 20, anchor=W, font=('Comic Sans MS', 14), text='от A' + str( i + 1 ), fill='#726565')


root = Tk()
margin_x = (root.winfo_screenwidth() - root.winfo_reqwidth())
margin_y = (root.winfo_screenheight() - root.winfo_reqheight())
root.title('Задача транспортной логистики. Метод потенциалов')
root.wm_geometry('560x270+%d+%d' % (margin_x/3, margin_y/3))
root.config(bg  = '#DDAC46')
root.iconbitmap('1.ico')
root.resizable(width=False, height=False)
obj = Window()
root.mainloop()