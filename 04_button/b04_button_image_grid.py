## Reproduction of partial NumPad without a .kv file.

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class OneButton(Button):
	background_normal = './images/Button1normal.png'
	background_down = './images/Button1pressed.png'
	#size_hint = (.33, .1)

	def on_release(self):
		print("1 Button pressed")


class TwoButton(Button):
	background_normal = './images/Button2normal.png'
	background_down = './images/Button2pressed.png'
	#size_hint = (.33, .1)

	def on_release(self):
		print("2 Button pressed")


class ThreeButton(Button):
	background_normal = './images/Button3normal.png'
	background_down = './images/Button3pressed.png'
	#size_hint = (.33, .1)

	def on_release(self):
		print("3 Button pressed")


class FourButton(Button):
	background_normal = './images/Button4normal.png'
	background_down = './images/Button4pressed.png'
	#size_hint = (.33, .1)

	def on_release(self):
		print("4 Button pressed")


class FiveButton(Button):
	background_normal = './images/Button5normal.png'
	background_down = './images/Button5pressed.png'
	#size_hint = (.33, .1)

	def on_release(self):
		print("5 Button pressed")


class SixButton(Button):
	background_normal = './images/Button6normal.png'
	background_down = './images/Button6pressed.png'
	#size_hint = (.33, .1)

	def on_release(self):
		print("6 Button pressed")


class SevenButton(Button):
	background_normal = './images/Button7normal.png'
	background_down = './images/Button7pressed.png'
	#size_hint = (.33, .1)

	def on_release(self):
		print("7 Button pressed")


class EightButton(Button):
	background_normal = './images/Button8normal.png'
	background_down = './images/Button8pressed.png'
	#size_hint = (.33, .1)

	def on_release(self):
		print("8 Button pressed")


class NineButton(Button):
	background_normal = './images/Button9normal.png'
	background_down = './images/Button9pressed.png'
	#size_hint = (.33, .1)

	def on_release(self):
		print("9 Button pressed")


class MyLayout(GridLayout):
	# These two lines centre the grid within the window.
	size_hint = .93, .5
	# x = centre, y = 10% from bottom
	pos_hint = {'center_x': .5, 'center_y': .1}
	# set the number of columns
	cols = 3
	# force the rows and columns to the size of the button images.
	row_force_default = True
	row_default_height = 104
	col_force_default = True
	col_default_width = 186
	

class MyApp(App):
	def build(self):
		Window.size = (600, 1024)
		layout = MyLayout()
		
		Window.add_widget(layout)
		
		one_button = OneButton()
		two_button = TwoButton()
		three_button = ThreeButton()
		layout.add_widget(one_button)
		layout.add_widget(two_button)
		layout.add_widget(three_button)
		
		four_button = FourButton()
		five_button = FiveButton()
		six_button = SixButton()
		layout.add_widget(four_button)
		layout.add_widget(five_button)
		layout.add_widget(six_button)

		seven_button = SevenButton()
		eight_button = EightButton()
		nine_button = NineButton()
		layout.add_widget(seven_button)
		layout.add_widget(eight_button)
		layout.add_widget(nine_button)
		

if __name__ == "__main__":
	MyApp().run()
