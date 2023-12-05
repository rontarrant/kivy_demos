# Add a Label to a window using KV

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

class MyLabel(Label):
	text = "Label 03 Example"
	color = (0.7, 0.6, 0.8, 1)

class LabelApp(App):
	def build(self):
		label = MyLabel()
		Window.add_widget(label)


if __name__ == "__main__":
	LabelApp().run()
