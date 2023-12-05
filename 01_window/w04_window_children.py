# A window's children
# Show that the window has no children,
# then add a Label to the window and show that
# it now has children.
# Then access the text property of the label via
# the Window's list of children and change the text.
# Also note that we've set up a reference to child zero
# so we don't have to access it by array element number.

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

class MyLabel(Label):
	pass

class WindowApp(App):
	def build(self):
		children = Window.children # get state
		print("children before: ", children)
		
		label = MyLabel(text = "Hello, Kivy World!")
		Window.add_widget(label)
		
		print("children after: ", children)
		
		print("Now, change the label...")
		myLabel = Window.children[0]
		myLabel.text = "So long."
		#Window.children[0].text = "Goodbye!"
		
		return

if __name__ == "__main__":
	WindowApp().run()
