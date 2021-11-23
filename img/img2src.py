from PIL import Image
import sys

colors = ((134, 192, 108), (7, 24, 33), (224, 248, 207), (48, 104, 80))

for filename in sys.argv[1:]:
    image = Image.open(filename)
    blit_bytes = []

    for y in range(image.height):
        for x in range(0, image.width, 4):
            indices = [colors.index(image.getpixel((x + xo, y))) for xo in range(4)]
            out_byte = indices[0] << 6 | indices[1] << 4 | indices[2] << 2 | indices[3]
            blit_bytes.append(f'0x{out_byte:02X}')

    print(f"[{','.join(blit_bytes)}]")
    # print(len(blit_bytes))
