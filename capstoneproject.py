import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:\\Users\\megal\\Documents\\weight-height.csv")
xs = np.array(list(df["Height"]))
ys = np.array(list(df["Weight"]))

trainxs = xs
trainys = ys

xx = trainxs**2
yy = trainys**2
xy = trainxs*trainys

m = (len(trainxs)*sum(xy) - sum(trainxs)*sum(trainys))/(len(trainxs)*sum(xx) - sum(trainxs)**2)
b = (sum(trainys) - m*sum(trainxs))/len(trainxs)
y = m*xs + b

plt.scatter(trainxs, trainys)
plt.plot(xs, y)
plt.show()


