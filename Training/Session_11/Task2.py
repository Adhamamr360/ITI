import cv2
import numpy as np

image_path = 'Session_11\\Insects.jpg'
image = cv2.imread(image_path)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_bound = (0, 0, 0)  
upper_bound = (180, 255, 200)  

mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours by area if needed
min_contour_area = 50  
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

# Draw contours on the original image
cv2.drawContours(image, filtered_contours, -1, (0, 255, 0), 2)

# Count the number of insects detected
number_of_insects = len(filtered_contours)
print(f"Number of insects detected: {number_of_insects}")

# Optionally show the image and the mask for visualization
cv2.imshow('Detected Insects', image)
cv2.imshow('Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
