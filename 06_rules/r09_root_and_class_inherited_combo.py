# NOTE: When custom classes are declared in the .py
# file, it must be before calling Builder.load_file().
# The RootObj is defined here as inheriting from the GridLayout and
# has an extra property added to its definition.
# See r05_root_and_class.kv for more notes.

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class MyGrid(GridLayout):
	new_property = ""

class MyLabel(Label):
	pass

kv_file = Builder.load_file("r09_root_and_class_inherited_combo.kv")


class MainApp(App):
	def build(self):
		# Either of the following will work:
		#return kv_file
		Window.add_widget(kv_file)

if __name__ == "__main__":
	MainApp().run()
