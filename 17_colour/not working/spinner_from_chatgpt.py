## THIS DOESN'T WORK.

from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.utils import get_color_from_hex

class ColourSpinner(Spinner):
    values = ["Red", "Green", "Blue"]  # Replace with your color values

    def __init__(self, **kwargs):
        super(ColourSpinner, self).__init__(**kwargs)
        self.bind(on_text=self.spinner_clicked)

    def spinner_clicked(self, instance, text):
        print("Colour selected:", text)

class MySpinnerApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MySpinnerApp, self).__init__(**kwargs)

        # Create a ColourSpinner widget
        my_spinner = ColourSpinner()

        # Add the spinner to the layout
        self.add_widget(my_spinner)

if __name__ == '__main__':
    runTouchApp(MySpinnerApp())