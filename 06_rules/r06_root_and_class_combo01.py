# Set up both Root and Class rules in the .kv file.

# Also, add the widget tree to the App class by returning an assumed instance of RootObj.
#
# NOTE: When custom classes are defined in the .py file,
# such statements must appear before the .kv file is loaded.

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label


# Class definitions must come first...
class RootObj(GridLayout):
	pass

class MyButton(Button):
	pass

class MyLabel(Label):
	pass

# NOW the .kv file can be loaded.
kv_file = Builder.load_file("r06_root_and_class_combo01.kv")


class MainApp(App):
	def build(self):
		return RootObj()

if __name__ == "__main__":
	MainApp().run()
