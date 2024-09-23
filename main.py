import cv2
import numpy as np

# Load the images
img1 = cv2.imread('doraemon.png')
img2 = cv2.imread('nobita.png')
img3 = cv2.imread('shizuka.png')
img4 = cv2.imread('sunio.png')

# Resize the images to the same size
height, width, _ = img1.shape
img2 = cv2.resize(img2, (width, height))
img3 = cv2.resize(img3, (width, height))
img4 = cv2.resize(img4, (width, height))

# Create a collage by concatenating the images horizontally
collage = np.concatenate((img1, img2, img3, img4), axis=1)

# Create a video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 1  # frames per second
video = cv2.VideoWriter('collage_video.avi', fourcc, fps, (collage.shape[1], collage.shape[0]))

# Write the collage to the video
for _ in range(100):  # write the collage 100 times to create a 100-frame video
    video.write(collage)

# Release the video writer
video.release()