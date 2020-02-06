from PIL import Image
  
filename = "img.png"

img = Image.open(filename)



# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
pixels = img.load() # create the pixel map
pixelObj = {}
for i in range(img.size[0]):    # for every col:
    pixelObj[i] = {}
    for j in range(img.size[1]):    # For every row
        pixel = pixels[i,j]
        r,g,b,x = pixels[i,j]
        something = 75 
        r = r - r%something
        g = g - g%something
        b = b - b%something
        pixels[i,j] = (r,g,b)
        print pixels[i,j]
     ## find average here
for i in range(len(pixelObj.keys())):
   
    pixels[i,j]

img.show()
