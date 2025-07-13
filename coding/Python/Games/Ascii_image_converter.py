from PIL import Image
import math


final_image = []

ascii_chars = "@%#*+=-:. "



def asciiConvrt(image, new_width=250):
    yuanyuan = Image.open(image)
    yuanyuan = yuanyuan.convert("RGB")

    # Calculate new dimensions while maintaining aspect ratio
    aspect_ratio = yuanyuan.height / yuanyuan.width
    new_height = int(aspect_ratio * new_width * 0.45)
    yuanyuan = yuanyuan.resize((new_width, new_height), Image.ANTIALIAS)
    final_image = []

    for y in range(yuanyuan.height):
        for x in range(yuanyuan.width):
            r, g, b = yuanyuan.getpixel((x, y))
            brightness = sum([r, g, b]) / 3

            # Convert brightness to ASCII character
            if brightness > 229.5:
                final_image.append("@")
            elif brightness > 204:
                final_image.append("%")
            elif brightness > 179.5:
                final_image.append("#")
            elif brightness > 154:
                final_image.append("*")
            elif brightness > 129.5:
                final_image.append("+")
            elif brightness > 104:
                final_image.append("=")
            elif brightness > 79.5:
                final_image.append("-")
            elif brightness > 54:
                final_image.append(":")
            elif brightness > 29.5:
                final_image.append(".")
            else:
                final_image.append(" ")
        final_image.append("\n")

    return "".join(final_image)
print(asciiConvrt(r"C:\Users\hfeng\Pictures\huawei ma\IMG_20191226_084749.jpg", 250))
