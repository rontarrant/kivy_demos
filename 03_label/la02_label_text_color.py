# Add a Label to a window using KV

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

class MyLabel(Label):
	pass

class LabelApp(App):
	def build(self):
		label = MyLabel()
		label.text = "Label 02 Example"
		label.color = (0.6, 0.8, 0.7, 1)
		Window.add_widget(label)


if __name__ == "__main__":
	LabelApp().run()
