# Demo of a root rule containing a widget tree.

# NOTE: Custom classes must be declared in the .py
# file before calling Builder.load_file().

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class RootObj(GridLayout):
	pass

class MyButton(Button):
	pass

class MyLabel(Label):
	pass

kv_file = Builder.load_file("r05_root_rule_tree.kv")


class MainApp(App):
	def build(self):
		# Either of the following will work:
		return kv_file
		#Window.add_widget(kv_file)

if __name__ == "__main__":
	MainApp().run()
