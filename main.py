from asyncio.windows_events import NULL
from sklearn import linear_model
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
import readFile 
import matplotlib.pyplot as plt
import numpy as np

readFile.readFile()
X = readFile.Timestamp
Y = readFile.Open
degree = 2
Y_predict = NULL



def pricePredictor():
    global Y_predict 
    reg = make_pipeline(PolynomialFeatures(degree),linear_model.LinearRegression())
    reg.fit(X,Y)
    Y_predict = reg.predict(X)

def drawGraph():
    plt.scatter(X, Y)
    plt.plot(X,Y_predict,color='red')
    plt.title("Polynomial regression with degree " + str(degree))
    plt.show()

    coefs = np.polyfit(X.flatten(), Y.flatten(), degree)
    plt.figure()
    plt.plot(X, np.polyval(coefs, X), color="black")
    plt.title("Polyfit degree "+str(degree))
    plt.scatter(X,Y)
    plt.show()

    return 1

def main():
    pricePredictor()
    print(Y_predict)
    drawGraph()

if __name__ == "__main__":
    main()
