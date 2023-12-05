from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
	def release(self, button):
		print(button.text)

kv = Builder.load_file("bl25_boxlayout_caculator.kv")

class MyApp(App):

	def build(self):
		return MyBoxLayout()

if __name__ == "__main__":
	MyApp().run()
