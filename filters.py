from PIL import Image



def pixel_value(k):
    if(k<0):
        return 0
    elif(k>255):
        return 255
    else:
        return k

def grayscale(im_data):
    im2=Image.new('RGB',(im_data["width"],im_data["height"])) #create a new image based on the input

    for x in range(im_data["width"]):
        for y in range(im_data["height"]):#loop on all pixels
            pix=im_data["img"].getpixel((x,y))#get RGB values of the input
            g=(pix[0]+pix[1]+pix[2])//3 #average the values
            im2.putpixel((x,y),(g,g,g))#put in on the second image

    im2.show()


def negative(im_data):
    im2=Image.new('RGB',(im_data["width"],im_data["height"]))

    for y in range(0,im_data["height"]):
            for x in range(0,im_data["width"]):
                pix1=im_data["img"].getpixel((x,y))
                r=255-pix1[0]#invert the RGB values
                v=255-pix1[1]
                b=255-pix1[2]
                im2.putpixel((x,y),(r,v,b))

    im2.show()

def rgb_mask(im_data):
    im2=Image.new('RGBA',(im_data["width"],im_data["height"]))
    r=int(input("Type the red value :"))
    v=int(input("Type the green value :"))
    b=int(input("Type the blue value :"))
    a=int(input("Type the transparency value :"))
    for y in range(0,im_data["height"]):
            for x in range(0,im_data["width"]):
                im2.putpixel((x,y),(r,v,b,a))

    im2.save("mask.png")
    layer=Image.open('mask.png')
    im_data["img"].paste(layer,(0,0),mask=layer)

    im_data["img"].show()

def sepia(im_data):

    for x in range(im_data["width"]):
        for y in range(im_data["height"]):
            pix=im_data["img"].getpixel((x,y))
            r=int(pix[0]*0.393+pix[1]*0.769+pix[2]*0.189)#change RGB values based on each one
            v=int(pix[0]*0.349+pix[1]*0.686+pix[2]*0.168)
            b=int(pix[0]*0.272+pix[1]*0.534+pix[2]*0.131)

            if r>255:#lower the value to 255 if higher
                r=255
            if v>255:
                v=255
            if b>255:
                b=255

            im_data["img"].putpixel((x,y),(r,v,b))

    im_data["img"].show()


def low_bright(im_data):

    for x in range (im_data["width"]):
        for y in range(im_data["height"]):
            pix=im_data["img"].getpixel((x,y))
            pix=list(pix)#convert the tuple into a list

            for k in range(0,3):

                if pix[k]-50>0: #lower each RGB value
                    pix[k]=pix[k]-50

                else:
                    pix[k]=0

            im_data["img"].putpixel((x,y),(pix[0],pix[1],pix[2])) #replace the values

    im_data["img"].show()

def up_bright(im_data):

    for x in range(im_data["width"]):
        for y in range(im_data["height"]):
            pix=im_data["img"].getpixel((x,y))
            pix=list(pix)

            for k in range(0,3):

                if pix[k]+50<255: #increase each RGB value
                    pix[k]=pix[k]+50

                else:
                    pix[k]=255

            im_data["img"].putpixel((x,y),(pix[0],pix[1],pix[2]))

    im_data["img"].show()

def blur(im_data):
    imflou=Image.new("RGB",(im_data["width"],im_data["height"]))
    rouge=int(0)
    vert=int(0)
    bleu=int(0)

    for x in range(0,im_data["width"]-1,1):
        for y in range(0,im_data["height"]-1,1):

            if x-2>=0 and y-2>=0 and x+2<=im_data["width"] and y+2<=im_data["height"]:

                for x2 in range(x-2,x+2): #get RGB values of the pixel + each neighbor pixel
                    for y2 in range(y-2,y+2):
                        pix=im_data["img"].getpixel((x2,y2))
                        rouge=rouge+pix[0]
                        vert=vert+pix[1]
                        bleu=bleu+pix[2]

                rouge=rouge//25 #average the values
                vert=vert//25
                bleu=bleu//25
                imflou.putpixel((x,y),(rouge,vert,bleu))
                rouge=0
                vert=0
                bleu=0

            else:
                pix=im_data["img"].getpixel((x,y))
                imflou.putpixel((x,y),(pix[0],pix[1],pix[2]))

    imflou.show()

def emboss(im_data):
    im3=Image.new("RGBA",(im_data["width"],im_data["height"]))

    for y in range(1,im_data["height"]-1):#apply a convolution matrix filter
        for x in range(1,im_data["width"]-1):
            pix0=im_data["img"].getpixel((x,y))
            pix1=im_data["img"].getpixel((x-1,y-1))
            pix2=im_data["img"].getpixel((x,y-1))
            pix3=im_data["img"].getpixel((x+1,y-1))
            pix4=im_data["img"].getpixel((x-1,y))
            pix5=im_data["img"].getpixel((x+1,y))
            pix6=im_data["img"].getpixel((x-1,y+1))
            pix7=im_data["img"].getpixel((x,y+1))
            pix8=im_data["img"].getpixel((x+1,y+1))
            r=(-2*pix1[0] - pix2[0] - pix4[0] + pix0[0] + pix6[0] + pix7[0] + 2*pix8[0])
            r=pixel_value(r)
            v=(-2*pix1[1] - pix2[1] - pix4[1] + pix0[1] + pix6[1] + pix7[1] + 2*pix8[1])
            v=pixel_value(v)
            b=(-2*pix1[2] - pix2[2] - pix4[2] + pix0[2] + pix6[2] + pix7[2] + 2*pix8[2])
            b=pixel_value(b)
            im3.putpixel((x,y),(r,v,b,pix0[3]))
            print((r,v,b,pix0[3]))


    im3.save("output.png")

#######
#1#2#3#
#4#0#5#
#6#7#8#
#######
