import numpy as np
import pandas as pd

df = pd.read_csv("C:\\Users\\megal\\Documents\\weight-height.csv")
xs = np.array(list(df["Height"]))
ys = np.array(list(df["Weight"]))

xx = x*x
xy = x*y
yy = y*y

def getLine(xs, ys):
  m = (len(xs)*sum(xy) - sum(xs)*sum(ys))/(len(xs)*sum(xx) - sum(xs)**2)
  b = (sum(ys) - m*sum(xs))/len(xs)
  return m, b
  
def getAccuracy(xvals, yvals):
  n = len(xs)
  numerator = n*sum(xy) - sum(xs)*sum(ys)
  denominator = ( (n*sum(xx) - sum(xs)**2) * (n*sum(yy) - sum(ys)**2) )
  return (numerator/denominator)**0.5

