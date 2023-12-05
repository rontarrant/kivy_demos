from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button

## local
from test_magic_palette_rgb import Palette

class MyButton(Button):
	def mix_colours(self):
		colour1 = Palette["Ivory Black"]
		colour2 = Palette["Titanium White"]
		##colour2 = (1.0, 1.0, .9412, 1) ## Ivory Black
		red1, green1, blue1, alpha1 = colour1
		red2, green2, blue2, alpha2 = colour2
		new_red = (red1 + red2) / 2
		new_green = (green1 + green2) / 2
		new_blue = (blue1 + blue2) / 2
		self.background_color = (new_red, new_green, new_blue, 1)
		
		new_red_int =   int(new_red * 255)
		new_green_int = int(new_green * 255)
		new_blue_int =  int(new_blue * 255)
		print("new colour: ", f'{new_red_int:X}' + f'{new_green_int:X}' + f'{new_blue_int:X}')

Builder.load_file("test_magic_palette.kv")

class MagicPaletteTestApp(App):
	def build(self):
		Window.size = 150, 150
		return MyButton()

if __name__ == "__main__":
	MagicPaletteTestApp().run()
