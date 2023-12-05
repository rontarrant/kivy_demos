## ly13_align_textinputs.py
## The alignment set is for the widget's text and
## doesn't affect the widget's alignment within its parent.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
	def release(self, button):
		print(button.text)

Builder.load_file('bl18_align_with_middle_space.kv')

class MyApp(App):

	def build(self):
		Window.size = (600, 1024)
		return MyBoxLayout()

if __name__ == "__main__":
	MyApp().run()
