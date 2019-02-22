path = input("Image Path : ")
from PIL import Image as im
img = im.open(path)
img.show()
