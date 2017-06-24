import image

def convertBlackWhite(input_image):
    grayscale_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())

    for col in range(input_image.getWidth()):
        for row in range(input_image.getHeight()):
            p = input_image.getPixel(col, row)

            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()

            avg = (red + green + blue) / 3.0

            newpixel = image.Pixel(avg, avg, avg)
            grayscale_image.setPixel(col, row, newpixel)

    blackwhite_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())
    for col in range(input_image.getWidth()):
        for row in range(input_image.getHeight()):
            p = grayscale_image.getPixel(col, row)
            red = p.getRed()
            if red > 140:
                val = 255
            else:
                val = 0

            newpixel = image.Pixel(val, val, val)
            blackwhite_image.setPixel(col, row, newpixel)
    return blackwhite_image


win = image.ImageWin()
img = image.Image("luther.jpg")

bw_img = convertBlackWhite(img)
bw_img.draw(win)

win.exitonclick()
