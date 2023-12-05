from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class LLBoxLayout(BoxLayout):
	## This exists just so the call from MyButton doesn't fail.
	def set_colours(self):
		pass

kv = Builder.load_file("magic_palette averages_hex.kv")

class MyApp(App):
	def build(self):
		Window.size = (1000, 400)
		return LLBoxLayout()

if __name__ == "__main__":
	MyApp().run()
