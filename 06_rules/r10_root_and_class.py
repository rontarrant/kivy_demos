# This example shows how to import a .py script into a .kv file.
# The custom classes MyButton and RootObj are defined in r10_class_definitions.py
# and this is where their inheritance is established.
#
# NOTE: Since definition of custom classes has been moved to a separate .py file,
# we no longer need to import the Button or Widget modules here in the main .py file.

from kivy.app import App
from kivy.lang import Builder


# NOW the .kv file can be loaded.
kv_file = Builder.load_file("r10_root_and_class.kv")


class MainApp(App):
	def build(self):
		return kv_file

if __name__ == "__main__":
	MainApp().run()
