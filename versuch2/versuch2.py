import cv2
import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable


GREYSCALE_PATH = "Bilder/aufnahme.png"
COLUMN_AMOUNT = 6
BORDER_TRIM = 40
IMAGE_AMOUNT = 10
DARK_PATH = "Bilder/schwarz"
WHITE_PATH = "Bilder/weiss"


def get_columns(image):
    height, width = image.shape
    column_width = width // COLUMN_AMOUNT

    columns = []

    for i in range(COLUMN_AMOUNT):
        start = i * column_width
        end = (i + 1) * column_width

        column = image[:, start:end]
        column = column[BORDER_TRIM:-BORDER_TRIM, BORDER_TRIM:-BORDER_TRIM]

        columns.append(column)

    return columns


def get_table(columns):
    table = PrettyTable(["Grauwertstufe", "Mittelwert", "Standardabweichung"])

    for i in range(len(columns)):
        column = columns[i]

        table.add_row([i + 1, column.mean(), column.std()])

    return table


def show_image(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()


greyscale_image = cv2.imread(GREYSCALE_PATH)
greyscale_image = cv2.cvtColor(greyscale_image, cv2.COLOR_BGR2GRAY)

show_image(greyscale_image)

greyscale_columns = get_columns(greyscale_image)

for greyscale_column in greyscale_columns:
    show_image(greyscale_column)

print(get_table(greyscale_columns))


def get_mean_image(path):
    images = []

    for i in range(IMAGE_AMOUNT):
        image = cv2.imread(path + f"{i + 1}.png")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = image.astype(np.float64)

        images.append(image)

    return np.mean(images, axis=0)


dark_image = get_mean_image(DARK_PATH)
contrast_dark_image = dark_image / 255

show_image(contrast_dark_image.astype(np.uint8))

white_image = get_mean_image(WHITE_PATH)
subtracted_white_image = white_image - dark_image
contrast_white_image = subtracted_white_image / 255

show_image(contrast_white_image.astype(np.uint8))

standardized_white_image = subtracted_white_image / white_image.mean()

print(standardized_white_image.mean())

corrected_greyscale_image = (greyscale_image - dark_image) / standardized_white_image

show_image(corrected_greyscale_image.astype(np.uint8))

corrected_greyscale_columns = get_columns(corrected_greyscale_image.astype(np.uint8))

print(get_table(corrected_greyscale_columns))



