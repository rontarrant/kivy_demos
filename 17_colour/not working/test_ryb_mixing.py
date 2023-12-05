## NOTE: DOESN'T WORK
## RYB Colour Mixing in an RGB World
from rgb_to_ryb import RgbToRyb
from ryb_to_rgb import RybToRgb
from ryb_colour_mixing import SubtractiveColourMix

## tests
## combine yellow and blue
rgb1 = (1.0, 1.0, 0.0)
rgb2 = (0.0, 0.0, 1.0)
ryb1 = RgbToRyb(rgb1)
print("ryb1: ", ryb1)
ryb2 = RgbToRyb(rgb2)
print("ryb2: ", ryb2)
ryb_result = SubtractiveColourMix(ryb1, ryb2)
rgb_result = RybToRgb(ryb_result)
print("result: ", rgb_result)