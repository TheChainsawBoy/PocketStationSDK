"""
image_converter.py - Convert PNG images to PixelSprite data
Converts images to black and white and generates code
"""
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import sys

class ImageConverter:
    @staticmethod
    def open_file_dialog():
        #Open file dialog and return selected PNG path
        root = tk.Tk()
        root.withdraw()  #Hide the main window

        file_path = filedialog.askopenfilename(
            title="Select PNG Image (max 32x32)",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )

        root.destroy()
        return file_path

    @staticmethod
    def resize_if_needed(img, max_size=32):
        #Resize image if larger than max_size while maintaining aspect ratio
        if img.width > max_size or img.height > max_size:
            # Calculate scaling factor
            scale = min(max_size / img.width, max_size / img.height)
            new_width = int(img.width * scale)
            new_height = int(img.height * scale)
            img = img.resize((new_width, new_height), Image.Resampling.NEAREST)

        return img

    @staticmethod
    def image_to_pixel_data(img, threshold=128):
        #Convert PIL Image to 2D list of 1s and 0s
        #1 = black pixel (visible), 0 = white pixel (transparent/background)
        #Convert to grayscale
        img = img.convert('L')

        width, height = img.size
        pixel_data = []

        for y in range(height):
            row = []
            for x in range(width):
                pixel = img.getpixel((x, y))
                #If pixel is darker than threshold, it's black (1)
                row.append(1 if pixel < threshold else 0)
            pixel_data.append(row)

        return pixel_data

    @staticmethod
    def pixel_data_to_code(pixel_data, var_name="sprite_data"):
        #Convert pixel data to Python code string
        code = f"{var_name} = [\n"
        for row in pixel_data:
            code += "    " + str(row) + ",\n"
        code += "]\n"
        return code

    @staticmethod
    def print_preview(pixel_data):
        #Print ASCII preview of the sprite
        print("\nPreview:")
        print("-" * (len(pixel_data[0]) + 2))
        for row in pixel_data:
            line = "|"
            for pixel in row:
                line += "█" if pixel else " "
            line += "|"
            print(line)
        print("-" * (len(pixel_data[0]) + 2))

    @staticmethod
    def convert_image_full_pipeline(image_path=None, threshold=128):
        """
        Full conversion pipeline:
        1. Load image (or open dialog if no path given)
        2. Resize if needed
        3. Convert to black/white
        4. Generate code
        """
        #Open file dialog if no path provided
        if not image_path:
            image_path = ImageConverter.open_file_dialog()
            if not image_path:
                print("No file selected!")
                return None

        print(f"Processing: {image_path}")

        try:
            #Load image
            img = Image.open(image_path)
            print(f"Original size: {img.size[0]}x{img.size[1]}")

            #Resize if needed
            img = ImageConverter.resize_if_needed(img, max_size=32)
            print(f"Final size: {img.size[0]}x{img.size[1]}")

            #Convert to pixel data
            pixel_data = ImageConverter.image_to_pixel_data(img, threshold)

            #Generate code
            code = ImageConverter.pixel_data_to_code(pixel_data)

            #Print preview and code
            ImageConverter.print_preview(pixel_data)
            print("\nGenerated code:")
            print("=" * 50)
            print(code)
            print("=" * 50)
            print("\nUsage:")
            print("from objects import PixelSprite")
            print("sprite = PixelSprite(x, y, sprite_data)")

            return pixel_data

        except Exception as e:
            print(f"Error converting image: {e}")
            return None

def main():
    print("=== PocketStation Image to PixelSprite Converter ===")
    print("Select a PNG image (max 32x32 recommended)")
    print("1 = BLACK pixel, 0 = WHITE/transparent")
    print()

    #Check for command line argument
    image_path = None
    if len(sys.argv) > 1:
        image_path = sys.argv[1]

    #Run conversion
    pixel_data = ImageConverter.convert_image_full_pipeline(
        image_path=image_path,
        threshold=128  #Adjust this if needed (0-255)
    )

    if pixel_data:
        print("\n✓ Conversion successful!")

        #Option to save to file
        save = input("\nSave to file? (y/n): ").lower()
        if save == 'y':
            filename = input("Enter filename (e.g. my_sprite.txt): ")
            try:
                with open(filename, 'w') as f:
                    code = ImageConverter.pixel_data_to_code(pixel_data)
                    f.write(code)
                print(f"✓ Saved to {filename}")
            except Exception as e:
                print(f"Error saving: {e}")
    else:
        print("\n✗ Conversion failed!")

if __name__ == "__main__":
    main()