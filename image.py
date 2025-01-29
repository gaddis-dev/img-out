from os import get_terminal_size as size
import PIL.Image
image = PIL.Image.open(input('image: ') + '.jpg')
input()
image = image.resize(size()[::-1])
print(list(image.getdata()), image, '\033[48;5;{r};{g};{}m h')