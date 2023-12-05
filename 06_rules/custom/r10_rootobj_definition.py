# This script is imported into this demo's .kv file. Doing things this way
# allows us to keep all import statements at the tops of their respective files.
# In other words, in the main .py file, we don't have to define our custom
# classes before importing the .kv file.
from kivy.uix.widget import Widget

# Class definitions must come first...
class RootObj(Widget):
	pass
