#v2
from PIL import Image

import filters
print("Welcome to PyFilters")
print("To use it, simply choose the filter you want to apply")
print("Be careful as you need to type the extension of the file as well\n")


def get_file_data(c_file):
    img = Image.open(c_file)
    width = img.size[0]
    height = img.size[1]
    return {'img' : img, 'width' : width, 'height' : height}



def main():


    print("1 = Grayscale")
    print("2 = Negative")
    print("3 = RGB Mask")
    print("4 = Sepia")
    print("5 = Lower Brightness")
    print("6 = Increase Brightness")
    print("7 = Blur")
    print("8 = Emboss\n")

    choice = int(input("Please choose a filter : "))
    c_file  = str(input("Please type the path of your file : "))

    if(choice == 1):
        filters.grayscale(get_file_data(c_file))
    elif(choice == 2):
        filters.negative(get_file_data(c_file))
    elif(choice == 3):
        filters.rgb_mask(get_file_data(c_file))
    elif(choice == 4):
        filters.sepia(get_file_data(c_file))
    elif(choice == 5):
        filters.low_bright(get_file_data(c_file))
    elif(choice == 6):
        filters.up_bright(get_file_data(c_file))
    elif(choice == 7):
        filters.blur(get_file_data(c_file))
    elif(choice == 8):
        filters.emboss(get_file_data(c_file))
    else:
        print("Please enter a correct number !")
        main()


if __name__ == '__main__':
    main()
