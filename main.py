import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# load the dataset from the root directory
csv_file_path = 'honeyproduction.csv'
df = pd.read_csv(csv_file_path)

def main():
    # display the first few rows of the dataset
    print("first few rows of the dataset:")
    print(df.head())

    # group by year and calculate mean total production
    prod_per_year = df.groupby('year').totalprod.mean().reset_index()
    print("\ntotal production per year (grouped by year):")
    print(prod_per_year)

    # create and reshape the X variable for years
    X = prod_per_year['year'].values.reshape(-1, 1)
    print("\nreshaped years (X):")
    print(X)

    # create the y variable for total production
    y = prod_per_year['totalprod']
    print("\ntotal production (y):")
    print(y)

    # scatter plot of y (total production) vs X (year)
    plt.scatter(X, y)
    plt.xlabel('year')
    plt.ylabel('total production')
    plt.title('honey production per year')
    plt.show()

    # create the linear regression model
    regr = LinearRegression()

    # fit the model to the data
    regr.fit(X, y)

    # print the slope and intercept
    print("\nlinear regression model:")
    print(f"slope: {regr.coef_}")
    print(f"intercept: {regr.intercept_}")

    # create predictions for the X data
    y_predict = regr.predict(X)
    print("\npredicted total production (y_predict):")
    print(y_predict)

    # plot the predictions on top of the scatterplot
    plt.scatter(X, y)
    plt.plot(X, y_predict, color='red')
    plt.xlabel('year')
    plt.ylabel('total production')
    plt.title('honey production with linear regression line')
    plt.show()

    # create the future years (2013 to 2050)
    X_future = np.array(range(2013, 2051)).reshape(-1, 1)
    print("\nfuture years (X_future):")
    print(X_future)

    # predict future honey production using the regression model
    future_predict = regr.predict(X_future)
    print("\npredicted future honey production (future_predict):")
    print(future_predict)

    # plot future predictions vs X_future
    plt.plot(X_future, future_predict, color='green')
    plt.xlabel('year')
    plt.ylabel('predicted total production')
    plt.title('predicted honey production (2013 - 2050)')
    plt.show()

if __name__ == '__main__':
    main()
