from image import AsciiArt
from glob import glob
from os import path as os_path, system, name, get_terminal_size
from time import sleep
# return
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Load frames into memory
size = get_terminal_size()
ascii_frames = []
ascii_art = AsciiArt()
ascii_art.add_color = True
# ascii_art.use_character = '#'
image_list = glob(os_path.join('walking_duck_frames_all/', '*.jpg'))

for image_file in sorted(image_list):
    # sleep(0.1)
    # ascii_art.print_image(
    #     ascii_art.create(image_file=image_file, width=70, height=35)
    # )
    # sleep(1)
    ascii_frames.append(ascii_art.create(image_file=image_file))

# sleep(10)
while True:
    for ascii_frame in ascii_frames:
        # print(ascii_frame)
        ascii_art.print_image(ascii_frame)
        sleep(0.01)
        # clear()