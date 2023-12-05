## ti05_textinput_read_only.py
## The cursor can be placed within the TextInput widget and
## moved around. Also, the text can be selected, but
## no typing is allowed.

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_file('ti05_textinput_read_only.kv')

class TestApp(App):
	def build(self):
		return TextInput()

if __name__ == "__main__":
	TestApp().run()
