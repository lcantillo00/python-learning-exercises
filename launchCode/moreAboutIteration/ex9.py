import image
img=image.Image("luther.jpg")
win=image.ImageWin()
newimg=image.EmptyImage(img.getWidth(),img.getHeight())
for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)
        red=int(p.getRed()* 0.393 + p.getGreen() * 0.769 + p.getBlue() * 0.189)
        green=int(p.getRed()* 0.349 + p.getGreen() *0.686 + p.getBlue() *0.168)
        blue=int(p.getRed()* 0.272 + p.getGreen() *0.534 + p.getBlue() * 0.131)
        lum = red + green + blue

        newpixel = image.Pixel(lum, lum, lum)
        newimg.setPixel(col,row,newpixel)

newimg.draw(win)
win.exitonclick()
