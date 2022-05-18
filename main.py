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
		self.day_label = Label(app.frame, text='', font=('Comic Sans MS', 20), bg='light blue', fg='black')
		self.time_label = Label(app.frame, text='', font=('Comic Sans MS', 20), bg='light blue', fg='black')
		self.countdown_new_year = self.new_year_day - self.tday
		self.time = 0

	def count_time(self, num=None):
		if num is not None:
			self.time = num

		if self.time <= 0:
			self.time_label['text'] = 'It is New Year!!!!'
		else:
			self.time_label['text'] = self.time
			self.time -= 1
			root.after(1000, self.count_time)
			
	def draw(self):
		self.day_label['text'] = f'Days Till New Year: {self.countdown_new_year.days}'
		self.day_label.pack(pady=20)
		
		self.time_label['text'] = self.count_time(int(self.countdown_new_year.total_seconds()))
		self.time_label.pack(pady=20)

app = App()
dt = Dt(app.frame)

app.draw()

root.bind('<Escape>', lambda x:root.quit())
root.mainloop()