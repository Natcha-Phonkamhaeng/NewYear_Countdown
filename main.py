from tkinter import *
import datetime
import time

WIDTH = 400
HEIGHT = 400

root = Tk()
root.title('New Year Countdown')
s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
# root.geometry(f'{WIDTH}x{HEIGHT}+{s_width//2-WIDTH//2}+{s_height//2-HEIGHT//2}')
root.geometry('400x400+2000+200')


class App:

	def __init__(self):
		self.frame = Frame(root, bg='light blue')
		self.frame.pack(fill=BOTH, expand=True)

	def draw(self):
		dt.draw()


class Dt:
	# Date
	def __init__(self, frame):
		self.tday = datetime.datetime.now()
		self.new_year_day = datetime.datetime(2023, 1, 1)
		self.day_label = Label(app.frame, text='', font=('Comic Sans MS', 20), bg='black', fg='white')
		
	def count_date(self):
		self.countdown_new_year = self.new_year_day - self.tday
		return f'Days Till New Year: {self.countdown_new_year.days}'

	def draw(self):
		self.day_label['text'] = self.count_date()
		self.day_label.pack(pady=20)


class Tm:
	#Time
	def __init__(self,frame):
		pass


app = App()
dt = Dt(app.frame)
tm = Tm(app.frame)

app.draw()

root.bind('<Escape>', lambda x:root.quit())
root.mainloop()