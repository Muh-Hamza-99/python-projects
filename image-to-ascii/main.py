import PIL.Image

ASCII_Characters = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)

def greyify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)

def pixels_to_ASCII(image):
    pixels = image.getdata()
    characters = "".join([ASCII_Characters[pixel//25] for pixel in pixels])
    return (characters)

def main(new_width=200):
    path = input("Please enter a valid pathname to the image: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(f"{path} is not a valid pathname to an image!")
    new_image_data = pixels_to_ASCII(greyify(resize_image(image))) 
    pixel_count = len(new_image_data)
    ASCII_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    print(ASCII_image)
    with open("ASCII-Image.txt", "w") as file:
        file.write(ASCII_image)

main()