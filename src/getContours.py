import os, cv2, numpy as np
from matplotlib import pyplot as plt

def createContours():
    for file in os.listdir("data/horse/"):
        if file.endswith(".jpg"):
            createContour(file)

def createContour(file):
    os.makedirs("data/horsecontour", exist_ok=True)
    img = cv2.imread("data/horse/"+file,0)
    edges = cv2.Canny(img,100,200)
    cv2.imwrite("data/horsecontour/"+file, edges)

    #plt.subplot(121),plt.imshow(img,cmap = 'gray')
    #plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    #plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    #plt.show()

def main():
    createContours()

if __name__ == '__main__':
    main()
