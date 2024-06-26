import cv2 as cv
from cv2.typing import MatLike

ASCII = "`^,+_-?1tfjrxnczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def to_ascii(image: MatLike, /):
    new_image = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
    for x in range(len(image)):
        for y in range(len(image[x])):
            pixel = image[x][y]
            pixel = ASCII[pixel % len(ASCII)]
            new_image[x][y] = pixel
    return new_image

def to_file(ascii_image, file_name = "result", /):
    with open(f"result/{file_name}_to_ascii.txt", "w") as f:
        for row in ascii_image:
            f.write('  '.join(row) + '\n')

def main():
    image_name = "venti.jpg"
    image: MatLike = cv.imread("img/venti.jpg")
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image = cv.resize(image, (300, 300))

    ascii_image = to_ascii(image)
    to_file(ascii_image, image_name)

    # cv.imshow('item', image)
    # cv.waitKey(0)

if __name__ == "__main__":
    main()