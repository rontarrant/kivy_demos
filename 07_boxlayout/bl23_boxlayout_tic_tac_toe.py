from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
	def release(self, button):
		if button.text == " ":
			button.text = "X"
		elif button.text == "X":
			button.text = "O"
		else:
			button.text = " "


kv = Builder.load_file("bl23_boxlayout_tic_tac_toe.kv")

class MyApp(App):

	def build(self):
		return MyBoxLayout()

if __name__ == "__main__":
	MyApp().run()
