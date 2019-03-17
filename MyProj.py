from PIL import Image, ImageDraw
import threading
import time

image = Image.open("C:\\Users\\asus\\Desktop\\lab\\holst.jpg")
print("Начальное изображение")
print()
image.show()

def run(i):
	threading.currentThread().getName()
	for j in range(255):
		image.putpixel((j, i), (i, j, 0))
now = time.time()

for i in range(255):
	for j in range(255):
		image.putpixel((j, i), (i, j, 255))

image.show()
print("Время без потоков:", round(time.time()-now, 2), "с")


now = time.time()
for i in range(255):
	my_thread = threading.Thread(target = run, args=(i,))
	my_thread.start()
print()
print("Время c потоками:", round(time.time()-now, 2), "с")
image.show()
input()