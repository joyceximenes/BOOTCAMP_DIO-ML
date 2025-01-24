import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_image(image_path, threshold=127):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    return gray_image, binary_image

def show_images(original, gray, binary):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.subplot(1, 3, 2)
    plt.title("Grayscale Image")
    plt.imshow(gray, cmap='gray')
    plt.axis('off')
    plt.subplot(1, 3, 3)
    plt.title("Binary Image")
    plt.imshow(binary, cmap='gray')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

image_path = "sua_imagem.jpg"

try:
    gray_img, binary_img = process_image(image_path)
    original_img = cv2.imread(image_path)
    show_images(original_img, gray_img, binary_img)
except FileNotFoundError as e:
    print(e)
