import PIL.Image

#ascii characters to build image
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
new_w = 100

#resize image
def resize_image(image):
    w, h = image.size
    ratio = h / w
    new_h = int(new_w * ratio)
    resized_image = image.resize((new_w, new_h)) #resize needs a tuple so thats why there are two sets of parenthesis
    return resized_image

#convert each pixel to grayscale
def grayscale(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels]) #// means that it divides and rounds down
    return characters

def main():
    #attempt to open image from user input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image.")

    #convert
    new_image_data = pixels_to_ascii(grayscale(resize_image(image)))

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_w)] for i in range(0, pixel_count, new_w)) 

    #save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f: 
        f.write(ascii_image)
        print("Image has been converted")
main()