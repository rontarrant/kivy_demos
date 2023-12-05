# Add a Label to a window using KV

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_file('la10_label_bold_sans_markup.kv')

class MyLabel(Label):
	pass

class LabelApp(App):
	def build(self):
		label = MyLabel()
		Window.add_widget(label)


if __name__ == "__main__":
	LabelApp().run()
