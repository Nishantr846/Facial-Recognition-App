import re
import numpy as np
import cv2
import json
import os

# Ask user for the subfolder name inside 'original'
subfolder = input("Enter the person's folder name inside 'original': ")
input_dir = os.path.join("original", subfolder)
if not os.path.isdir(input_dir):
    print(f"Folder '{input_dir}' does not exist.")
    exit(1)

# Create output subfolder for the person
output_dir = os.path.join("cropped", subfolder)
os.makedirs(output_dir, exist_ok=True)
files = os.listdir(input_dir)
print(f"Found {len(files)} files in {input_dir}")
count = 1

# Use OpenCV's built-in haarcascade path
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

for fname in files:
    img_path = os.path.join(input_dir, fname)
    img = cv2.imread(img_path)
    if img is None:
        print(f"Could not read image: {img_path}")
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        roi_color = img[y:y + h, x:x + w]
        out_path = os.path.join(output_dir, f"{count:03d}.jpg")
        cv2.imwrite(out_path, roi_color)
        count += 1