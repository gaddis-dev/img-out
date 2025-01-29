from os import get_terminal_size as size
import PIL.Image
image = PIL.Image.open('image1.jpg')

#ok
input()

w, h = size()
# image = image.resize((w, h))
r, g, b = 100, 100, 100
# f'\033[48;5;{r};{g};{b}m'
for y in range(h):
    for x in range(w):
        try:
            r, g, b = image.getpixel((x, y))
        except Exception as e:
            pass
        print(f'\033[48;5;{r};{g};{b}m ', end = '')
    print('\033[0m')