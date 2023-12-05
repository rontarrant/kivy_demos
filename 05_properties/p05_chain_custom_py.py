# A Kivy custom property local to the Python script with chained callbacks.


from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import NumericProperty

Builder.load_file("p05_chain_custom_py.kv")

class MyLabel(Label):
	count = NumericProperty(0)

	def get_count(self):
		print("count is now: ", self.count)
	
	# Properties added via the kivy.properties module
	# automatically emit signals. This is how we harness them.
	def on_count(self, instance, value):
		print("on_count called...")
		self.get_count()
		
	def on_chain_count(self):
		print("on_chain_count called...")
		self.get_count()

	def on_text(self, instance, text):
		self.count += 1


class PropApp(App):
	def build(self):
		label = MyLabel()
		Window.add_widget(label)
		
		# change the label text
		label.text = "New Text"
		
		# change the label text again
		label.text = "More New Text"
		
		# and one more time
		label.text = "Hello, Kivy World, Again!"

if __name__ == "__main__":
	PropApp().run()
