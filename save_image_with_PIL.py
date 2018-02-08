from PIL import Image
import numpy

from PIL import Image

for i in range(1,4):
    print i
    img = Image.open('./data/%d.jpg' %i)
    img.save('./data1/new_%d.png' %i)
    img_gray = img.convert('L')
    img_gray.save('./data1/gray_%d.png' %i)
