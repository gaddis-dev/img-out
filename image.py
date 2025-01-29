from os import get_terminal_size as size
import PIL.Image
image = PIL.Image.open(input('image: ') + '.jpg')
input()
image = image.resize(size()[::-1])
r, g, b = 100, 100, 100
print(list(image.getdata()), image, f'\033[48;5;{r};{g};{b}m h')