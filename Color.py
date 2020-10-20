
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import numpy as np
from datetime import date



path = "/path/Sample.jpeg"
outputfile = path.split('.')[0] + "Palette.png"
img = Image.open(path)
width,height = img.size
steps = 500
step = int(width*height//steps)

totalclusters = 5
day = date.today().weekday()


pixels = np.array(img.getdata())
x = []
for pixel in pixels[::step]:
    x.append(pixel)


kmean = KMeans(n_clusters=totalclusters)
kmean.fit(x)
centers = kmean.cluster_centers_
labels = kmean.labels_


freq = {}
for i in range(len(labels)):
	freq.setdefault(labels[i],0)
	freq[labels[i]] += 1/len(labels)


palette = []
for i in range(totalclusters):
    for j in range(int(freq[i]*height)):
        for k in range(width):
            r,g,b = map(int,centers[i % totalclusters])
            palette.append((r,g,b))



img2 = Image.new('RGB', img.size)
img2.putdata(palette)

img2.save(outputfile,'PNG')
