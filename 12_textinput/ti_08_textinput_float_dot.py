## Allow only floating point numbers (including a single dot)
## to be entered into a Kivy TextInput.
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

import re ## Any library has to be imported into any module that uses it.

class FloatInput(TextInput):
	pat = re.compile('[^0-9]')
	
	def insert_text(self, substring, from_undo = False):
		pat = self.pat
		
		if '.' in self.text:
			s = re.sub(pat, '', substring)
		else:
			s = '.'.join(re.sub(pat, '', s)
			for s in substring.split('.', 1))
				
		return super().insert_text(s, from_undo = from_undo)

class TestApp(App):
	def build(self):
		float_input = FloatInput()
		Window.add_widget(float_input)

if __name__ == "__main__":
	TestApp().run()
