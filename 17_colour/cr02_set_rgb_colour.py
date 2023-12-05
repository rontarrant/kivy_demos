from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class LLBoxLayout(BoxLayout):
	def release(self):
		label = self.ids.my_label
		button = self.ids.my_button
		
		if label.text == "Here's a label":
			label.text = "Another Label"
		else:
			label.text = "Here's a label"


kv = Builder.load_file("cr02_set_rgb_colour.kv")

class MyApp(App):
	def build(self):
		return LLBoxLayout()

if __name__ == "__main__":
	MyApp().run()
