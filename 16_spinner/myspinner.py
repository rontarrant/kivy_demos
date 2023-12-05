from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner

class MySpinner(Spinner):
	def callback_function(self):
		# This is your callback function
		print("Spinner Text:", self.text)

class MyGridLayout(GridLayout):
	pass

class MySpinnerApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	MySpinnerApp().run()