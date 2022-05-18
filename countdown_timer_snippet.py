from tkinter import *

root = Tk()


def countdown(num=None):
	global count_down
	if num is not None:
		count_down = num

	if count_down <= 0:
		my_label['text'] = 'Time is up!!!!'
	else:
		my_label['text'] = count_down
		count_down -= 1
		root.after(1000, countdown)

my_label = Label(root, text='', font=('Comic Sans MS', 20))
my_label.pack(pady=20)

countdown(5)

root.mainloop()