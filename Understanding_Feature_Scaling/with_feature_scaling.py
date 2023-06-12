from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# creating custom data
age = [45, 44, 40, 36, 39, 55]
height = [5.5, 4.9, 5.3, 6.0, 4.5, 5.9]
salary = [70000, 60000, 52000, 46000, 100000, 5000000]

# converting to DataFrames
df_x = pd.DataFrame({"Age":age, "Height": height})
df_y = pd.DataFrame(salary)

# converting age & salary columns to 2D numpy arrays
# np_x = df_x.values.reshape(-1, 1)
np_y = df_y.values.reshape(-1, 1)

# feature scaling data - using normalization
normalizer = MinMaxScaler()
normalized_x = normalizer.fit_transform(df_x)
normalized_y = normalizer.fit_transform(np_y)

# creating a LinearRegression model
linear_model = LinearRegression()

# splitting the data between train & test
X_train, X_test, y_train, y_test = train_test_split(normalized_x, normalized_y, random_state=42)

# training the model
linear_model.fit(X_train, y_train)

# testing the model
prediction = linear_model.predict(X_train)

# comparing predicted test data with original test data
print(prediction)
print(y_train)

#converting the numpy array back to Dataframe
X_train = pd.DataFrame(X_train, columns=df_x.columns)
#plotting to see the results
plt.scatter(X_train["Height"], prediction, color="blue", alpha=0.4)
plt.scatter(X_train["Height"], y_train, color="red", alpha=0.4)
plt.title("WITH FEATURE SCALING")
plt.show()