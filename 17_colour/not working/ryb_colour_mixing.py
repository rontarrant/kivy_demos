## NOTE: DOESN'T WORK
def SubtractiveColourMix(ryb1, ryb2):
    """
    Simulates RYB subtractive color mixing.
    
    :param ryb1: Tuple representing the RYB values of the first color (Red, Yellow, Blue)
    :param ryb2: Tuple representing the RYB values of the second color (Red, Yellow, Blue)
    :return: Tuple representing the resulting color after mixing (Red, Yellow, Blue)
    """
    red1, yellow1, blue1 = ryb1
    red2, yellow2, blue2 = ryb2

    # Subtractive color mixing formula
    mixed_red = red1 + red2
    mixed_yellow = yellow1 + yellow2
    mixed_blue = blue1 + blue2

    # Ensure values are clamped to the range [0, 1]
    mixed_red = min(1.0, mixed_red)
    mixed_yellow = min(1.0, mixed_yellow)
    mixed_blue = min(1.0, mixed_blue)

    return mixed_red, mixed_yellow, mixed_blue

# Example usage:
if __name__ == "__main__":
	color1 = (1.0, 0.0, 0.0)  # Pure Red (RYB values)
	color2 = (0.0, 1.0, 0.0)  # Pure Yellow (RYB values)

	result_color = SubtractiveColourMix(color1, color2)
	print("Resulting color (RYB):", result_color)
