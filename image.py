from PIL import Image
from webcolors import rgb_to_hex
from rich import print

class AsciiArt():
    ascii_characters: str = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    def create(self) -> None:
        image = Image.open('cat.jpg')
        # image = image.resize((width, height))
        image = image.resize((90, 35))
        ascii_art = self.convert_to_ascii_art(image=image)
        self.print_lines(ascii_art=ascii_art)

    def convert_to_ascii_art(self, image: Image) -> list:
        previous_color = ''
        ascii_art = []
        (width, height) = image.size
        for y in range(0, height - 1):
            line = ''
            for x in range(0, width - 1):
                pixel = image.getpixel((x, y))
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
                # line += character
                previous_color = hex_color
            ascii_art.append(line + '[/]')
            # ascii_art.append(line)
        return ascii_art

    def convert_pixel_to_character(self, pixel: tuple) -> str:
        (r, g, b) = pixel
        pixel_brightness = r + g + b
        max_brightness = (255 * 3)
        brightness_weight = len(self.ascii_characters) / max_brightness
        index = int(pixel_brightness * brightness_weight) - 1
        return self.ascii_characters[index]
        return '$'

    def print_lines(self, ascii_art: list) -> None:
            for line in ascii_art:
                print(line)

if __name__ == '__main__':
    AsciiArt().create()