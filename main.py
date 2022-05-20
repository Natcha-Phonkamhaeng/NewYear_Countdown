from tkinter import *
import datetime

root = Tk()
root.title('New Year Countdown')

class App:

	def __init__(self):
		self.frame = Frame(root, bg='light blue')
		self.frame.pack(fill=BOTH, expand=True)

	def draw(self):
		dt.draw()


class Dt:

	def __init__(self, frame):
		self.tday = datetime.datetime.now()
		self.new_year_day = datetime.datetime(2023, 1, 1)
		self.day_label = Label(app.frame, text='', font=my_font(18), bg='light blue', fg='blue')
		self.time_label = Label(app.frame, text='', font=my_font(15))
		self.countdown_new_year = self.new_year_day - self.tday
		self.time = 0

	def count_time(self, num=None):
		if num is not None:
			self.time = num

		if self.time <= 0:
			self.time_label['text'] = 'It is New Year!!!!'
			self.time_label.config(bg='pink', fg='blue')
		else:
			self.time_label['text'] = f'Total Second: {self.time:,}'
			self.time_label.config(bg='light blue', fg='blue')
			self.time -= 1
			root.after(1000, self.count_time)
			
	def draw(self):
		new_year = Label(app.frame, text='New Year Countdown', font=my_font(20), bg='light blue')
		new_year.pack(pady=10)

		self.day_label['text'] = f'Days: {self.countdown_new_year.days}'
		self.day_label.pack(pady=20)
		
		self.count_time(int(self.countdown_new_year.total_seconds()))
		# self.count_time(0)
		self.time_label.pack()


def my_font(num):
	font = ('Comic Sans Ms', num)
	return font

app = App()
dt = Dt(app.frame)

app.draw()

root.bind('<Escape>', lambda x:root.quit())
root.mainloop()