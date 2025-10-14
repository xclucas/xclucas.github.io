from PIL import Image
import sys

def process_image(input_path, output_path):
    """
    Takes a black and white PNG image and makes the transparency
    proportional to the whiteness of the pixels.
    White pixels become fully transparent, black pixels remain opaque.

    Args:
        input_path (str): The path to the input PNG image.
        output_path (str): The path to save the output PNG image.
    """
    try:
        # Open the input image
        with Image.open(input_path) as img:
            # Ensure the image has an alpha channel for transparency
            img = img.convert("RGBA")

            # Get the pixel data
            data = img.getdata()

            new_data = []
            for item in data:
                # item is a tuple (R, G, B, A)
                # For a black and white image, R, G, and B are the same.
                # We use the red channel value as a measure of whiteness (0=black, 255=white).
                whiteness = item[0]

                # The new alpha is inversely proportional to whiteness.
                # 255 (white) -> 0 (transparent)
                # 0 (black) -> 255 (opaque)
                new_alpha = 255 - whiteness

                # We keep the original color but apply the new alpha.
                # For a pure black and white output on a transparent background,
                # you could use (0, 0, 0, new_alpha).
                new_data.append((0, 0, 0, new_alpha))

            # Update image data
            img.putdata(new_data)

            # Save the new image
            img.save(output_path, "PNG")
            print(f"Successfully processed image and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_image.py <input_file.png> <output_file.png>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_image(input_file, output_file)