from PIL import Image
from webcolors import rgb_to_hex
from rich import print as print_ascii

class AsciiArt():
    ascii_characters: str = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    add_color: bool = True
    width: int = 0
    height: int = 0

    def create(self, image_file: str) -> str:
        image = Image.open(image_file)
        image = image.resize((self.width, self.height))
        ascii_lines = self.convert_to_ascii_art(image=image)
        return '\n'.join(ascii_lines)

    def convert_to_ascii_art(self, image: Image) -> list:
        previous_color = ''
        ascii_art = []
        (width, height) = image.size
        for y in range(0, height - 1):
            line = ''
            for x in range(0, width - 1):
                pixel = image.getpixel((x, y))
                # If user doesn't want color. Then we continue after adding char to line
                if not self.add_color:
                     line += self.convert_pixel_to_character(pixel=pixel)
                     continue
                # If user wants color, then...
                character = self.convert_pixel_to_character(pixel=pixel)
                if character == '\\':
                    character = '\\\\' # Have to double escape the backslash to ensure it doesn't escape any color tags.
                hex_color = rgb_to_hex(pixel)
                if not line:
                    line += f'[{hex_color}]{character}'
                elif previous_color != hex_color:
                    line += f'[/][{hex_color}]{character}'
                else:
                    line += character
                previous_color = hex_color
            if not self.add_color:
                ascii_art.append(line)
                continue
            ascii_art.append(line + '[/]')
        return ascii_art

    def convert_pixel_to_character(self, pixel: tuple) -> str:
        (r, g, b) = pixel
        pixel_brightness = r + g + b
        max_brightness = (255 * 3)
        brightness_weight = len(self.ascii_characters) / max_brightness
        index = int(pixel_brightness * brightness_weight) - 1
        return self.ascii_characters[index]
        return '$'

    def print_image(self, ascii_art: str) -> None:
        # If not color use normal print
        if not self.add_color:
            print(ascii_art)
        else:
            print_ascii(ascii_art)

# if __name__ == '__main__':
#     ascii = AsciiArt(add_color=False)
#     ascii.print_image(
#         ascii.create(image_file='walking_duck_frames/23.jpg', width=70, height=35)
#     )
#     ascii.print_image(
#         ascii.create(image_file='walking_duck_frames/25.jpg', width=70, height=35)
#     )