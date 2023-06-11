from PIL import Image
from webcolors import rgb_to_hex
from rich import print

ascii_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def main() -> None:
    image = Image.open('image.jpg')
    # image = image.resize((width, height))
    image = image.resize((70, 35))
    ascii_art = convert_to_ascii_art(image=image)
    print()
    print_lines(ascii_art=ascii_art)
    print()

def convert_to_ascii_art(image: Image) -> list:
    ascii_art = []
    (width, height) = image.size
    for y in range(0, height - 1):
        line = ''
        for x in range(0, width - 1):
            pixel = image.getpixel((x, y))
            line += convert_pixel_to_character(pixel=pixel)
        ascii_art.append(line)
    return ascii_art

def convert_pixel_to_character(pixel: tuple) -> str:
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    max_brightness = (255 * 3)
    brightness_weight = len(ascii_characters) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    hex_color = rgb_to_hex((r, g, b))
    return f'[{hex_color}]{ascii_characters[index]}[/]'
    return ascii_characters[index]

def print_lines(ascii_art: list) -> None:
        for line in ascii_art:
            print(line)

if __name__ == '__main__':
    main()