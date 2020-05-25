#importing the necessary modules:
#NumPy for array processing
#Matplotlib for visualization
#Pandas for loading the data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing .csv file to use as dataframe.
#Creating NumPy arrays for each axes
#The x-axis is the independant variable: height
#The y-axis is the dependant variable: weight
df = pd.read_csv("C:\\Users\\megal\\Documents\\weight-height.csv")
xs = np.array(list(df["Height"]))
ys = np.array(list(df["Weight"]))

#Splitting data into training and testing
#80% of data used for training
#20% of data used for testing
trainxs = xs[:int(len(xs)/1.25)]
trainys = ys[:int(len(ys)/1.25)]

testxs = xs[int(len(xs)/1.25):]
testys = ys[int(len(ys)/1.25):]

#Creating two new NumPy arrays so that calculation is made easier
#First one is simply the trainxs array with all the values squared
#Second one is an array holding the products of each pair of x and y values
xx = trainxs**2
xy = trainxs*trainys

#Mathematical formula to find best-fit gradient/slope and y-intercept
m = (len(trainxs)*sum(xy) - sum(trainxs)*sum(trainys))/(len(trainxs)*sum(xx) - sum(trainxs)**2)
b = (sum(trainys) - m*sum(trainxs))/len(trainxs)

#Constructing the line using the slope and y-intercept
line = m*xs + b

#Plotting the line and comparing it to the test data
plt.scatter(testxs, testys)
plt.plot(xs, line)
plt.show()


