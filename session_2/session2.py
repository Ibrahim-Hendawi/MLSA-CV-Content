import cv2
import numpy as np
# import matplotlib.pyplot as plt
img = cv2.imread("1.png")
print(img.shape)

# plt.imshow(img)
cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()