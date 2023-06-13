import matplotlib.pyplot as plt

class LinearRegression():
    def __init__(self):
        self.learning_rate = 0.0001
        self.actual_values_x = [5, 10, 15, 20, 30]
        self.actual_values_y = [10, 20, 30, 40, 50]
        self.list_of_predictions = [0, 5, 9, 4, 3]
        self.m = 1
        self.b = 1

    def mean_squared_error(self):
        error = 0 
        for index, value in enumerate(self.list_of_predictions):
            error += (self.actual_values_y[index] - value) ** 2
        error /= len(self.actual_values_y)
        print(f"My Mean Squared Error: {error}")
    
    def calculate_slope(self):
        new_m = 0
        for index, value in enumerate(self.actual_values_x):
            new_m += self.actual_values_x[index] * (self.actual_values_y[index] - self.m * self.actual_values_x[index] + self.b)
        new_m *= -2/len(self.actual_values_x)
        return new_m
    
    def calculate_intercept(self):
        new_b = 0 
        for index, value in enumerate(self.actual_values_x):
            new_b += self.actual_values_y[index] - (self.m * self.actual_values_x[index] + self.b)
        new_b *= -2/len(self.actual_values_x)
        return new_b

    def generate_resulting_list(self):
        y = 0
        final_predictions = []
        m, b = self.optimize_regression_line()
        print(m, b)
        for item in self.actual_values_x:
            y = m * item + b
            final_predictions.append(y)
        return final_predictions

    def optimize_regression_line(self):
        while True: 
            self.m -= self.learning_rate * self.calculate_slope()
            temp_m = self.m
            self.b -= self.learning_rate * self.calculate_intercept()
            temp_b = self.b
            # if temp_m <= self.m or temp_b <= self.b:
            #     self.m = temp_m 
            #     self.b = temp_b
            #     return self.m, self.b 
            convergence_threshold = 0.0001
            if abs(temp_m - self.m) < convergence_threshold and abs(temp_b - self.b) < convergence_threshold:
                self.m = temp_m
                self.b = temp_b
                return self.m, self.b

    def create_regression_plot(self):
        plt.scatter(self.actual_values_x, self.actual_values_y, color="red")
        pred_list = self.generate_resulting_list()
        plt.scatter(self.actual_values_x, pred_list, color="blue")
        plt.show()

linear_model = LinearRegression()
linear_model.create_regression_plot()