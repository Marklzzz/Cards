from PIL import Image


def greening(img):
    im = Image.open(img)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            if pixels[i, j] != (255, 255, 255) and pixels[i, j] != (255, 255, 255, 0):
                pixels[i, j] = (0, pixels[i, j][1], 0)
            else:
                pixels[i, j] = (0, 0, 0)
    im.save('current_img.jpg')


if __name__ == '__main__':
    img_to_convert = 'crab.jpg'
    greening(img_to_convert)
