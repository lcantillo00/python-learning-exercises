import image
img=image.Image("luther.jpg")
newimg=image.EmptyImage(img.getWidth(),img.getHeight())
win = image.ImageWin()
for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        red=int(p.getRed()*0.299)
        green=int(p.getGreen()*0.587)
        blue = int(p.getBlue() * 0.114)
        lum = red + green + blue


        newpixel = image.Pixel(lum, lum, lum)
        newimg.setPixel(col,row,newpixel)

newimg.draw(win)
win.exitonclick()
