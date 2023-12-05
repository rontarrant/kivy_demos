## ti04_textinput_alignment.py
## The alignment set is for the widget's text and
## doesn't affect the widget's alignment within its parent.

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_file('ti04_textinput_alignment.kv')

class TestApp(App):
	def build(self):
		return TextInput()

if __name__ == "__main__":
	TestApp().run()
