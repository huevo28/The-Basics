#################################################################
#                                                               #
#   This script removes all metadata tags from images.          #
#                                                               #
#---------------------------------------------------------------#
#                                                               #
#               Developed by Huevo 28 May 2025                  #
#                                                               #
#############################################################################################
#                                                                                           #
#   Sources:                                                                                #
#   https://www.pythonforall.com/modules/pillow/pwmeta                                      #
#   https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Exif.get_ifd     #
#   https://exiv2.org/tags.html                                                             #
#                                                                                           #
#############################################################################################

from PIL import Image
import sys
import getpass

def main():
    print("Meta-Strip developed by Huevo")
    count = len(sys.argv)
    x = 1
    new_path = input("Where would you like to save your images?: ")
    if new_path[0] == '~':
        new_path = "/home/" + getpass.getuser() + new_path[1:]
    while x < count:
        print("-------------------------------------------------")
        print("Image path: ", sys.argv[x])
        list_tags(sys.argv[x], new_path, x)
        x = x + 1
        print("-------------------------------------------------\n")


def list_tags(img_path, new_path, count):
    img_ext = img_path[-4:]
    print(img_ext)
    img = Image.open(img_path)
    exif_data = img.getexif()
    img.save(new_path + "no-metadata-" + str(count) + img_ext)
    for k, v, in exif_data.items():
        print("Tag", k, "Value", v)

if __name__ == "__main__":
    main()