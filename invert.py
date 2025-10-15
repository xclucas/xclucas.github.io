import sys
from PIL import Image

def invert_colors(input_path, output_path):
    """
    Inverts the RGB colors of an image, leaving the alpha channel unchanged.
    """
    try:
        with Image.open(input_path) as img:
            # Ensure image has an alpha channel
            if img.mode != 'RGBA':
                img = img.convert('RGBA')

            # Split into R, G, B, A bands
            r, g, b, a = img.split()

            # Invert R, G, B bands
            r = r.point(lambda i: 255 - i)
            g = g.point(lambda i: 255 - i)
            b = b.point(lambda i: 255 - i)

            # Merge bands back
            inverted_img = Image.merge('RGBA', (r, g, b, a))

            # Save the new image
            inverted_img.save(output_path, 'PNG')
            print(f"Successfully inverted colors and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python invert.py <input.png> <output.png>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    invert_colors(input_file, output_file)
