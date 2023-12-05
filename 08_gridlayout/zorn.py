## Zorn Colour Palette Mixer
## GridLayout 4x5
## Step 1: get RGB values of a subset of web-safe colours
## Step 2: Build a dictionary with these RGB values
## Step 3: Build a UI with:
##	- a drop-down list of the colours,
## - a 4x5 grid for mixing colours
## - an extra column to the left of the mixing grid with 
##   drop-down lists of colours in the first and last rows,
## - an extra row above the mixing grid with colour drop-downs in the
##   2nd and 4th columns
## - an extra cell above the extra column and to the left of the extra
##   row containing:
##		- a button for saving the palette (or an image of the mixing grid
##      with RGB values for all colours)
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown

class ZornGridLayout(GridLayout):
	def spinner_clicked(self, value):
		print("Colour selected: ", value)


class ZornApp(App):
	def build(self):
		Window.size = 500, 600
		return ZornGridLayout()

if __name__ == "__main__":
	ZornApp().run()
