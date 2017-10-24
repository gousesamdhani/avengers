import numpy as np
import matplotlib.pyplot as plt
 
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x - n*m_y*m_x)
    SS_xx = np.sum(x*x - n*m_x*m_x)
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return(b_0, b_1)
 
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()
 
def main():
    # observations
    x = np.array([270.7, 273.3, 277.55, 277.05, 277.9, 277.2, 275.85, 276.35, 271.65, 270.2, 268.95, 270.5, 269.35, 269.65, 270.7, 272.3, 270.45, 268.25, 269.2, 271.75])
    y = np.array([4.25, 5.6, 5.4, 7.8, 6.05, 6.3, 6.45, 6.35, 4.35, 2.75, 2.45, 2.75, 2.95, 2.3, 2.15, 2.2, 5, 2.05, 1.35, 1.55])
 
    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
 
    # plotting regression line
    #plot_regression_line(x, y, b)
 
if __name__ == "__main__":
    main()


