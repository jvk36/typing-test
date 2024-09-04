from PIL import Image

infile = "images/background.png"
im = Image.open(infile)

# print(im.format, im.size, im.mode)
print(f"Image Format: {im.format}, Size: {im.size}, Mode: {im.mode}")

# saves it as a temporary PNG file and launches an app to display
# it, if such app is available. The photos app is launched on windows
# im.show()

# convert from jpg to webp
outfile = "images/background.webp"
if infile != outfile:
    try:
        with Image.open(infile) as im:
            im.save(outfile)
            im2 = Image.open(outfile)
            print(im2.format)
            # im2.show()
    except OSError:
        print("cannot convert", infile)

# convert from jpg to thumbnail
im3 = Image.open("images/background.jpg")
# im3.show()
size = (128, 128)
im3.thumbnail(size)
outfile = "images/thumbnail.jpg"
im3.save(outfile, "JPEG")
im3.show()

