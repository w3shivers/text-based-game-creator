from PIL import Image

ascii_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def main() -> None:
    image = Image.open('image.jpg')
    # image = image.resize((width, height))
    image = image.resize((50, 25))
    ascii_art = convert_to_ascii_art(image=image)
    save_as_text(ascii_art=ascii_art)

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
    return ascii_characters[index]

def save_as_text(ascii_art: list) -> None:
    with open("image.txt", "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write('\n')
        file.close()

if __name__ == '__main__':
    main()