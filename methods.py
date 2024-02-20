import numpy as np




# Методы решают уравнение вида y' = f(x,y) на отрезке [0, 1] с начальным условием y(0) = y_0

class Method():
    def __init__(self, f, num_points, y0):
        self.f = f
        self.num_points = num_points
        self.stepsize = 1 / (num_points - 1)
        self.X = np.zeros(num_points)
        self.Y = np.zeros(num_points)
        self.yi = y0
        self.xi = 0
        self.Y[0] = self.yi
        self.X[0] = self.xi

        

class EulerMethod(Method):
    def __init__(self, f, num_points, y0):
        Method.__init__(self, f, num_points, y0)
    def calculate(self):
        for i in range(1, self.num_points):
            self.yi += self.stepsize * self.f(self.xi, self.yi)
            self.xi += self.stepsize
            self.Y[i] = self.yi
            self.X[i] = self.xi
        return self.X, self.Y
        


class CauchyMethod(Method):
    def __init__(self, f, num_points, y0):
        Method.__init__(self, f, num_points, y0)
    def calculate(self):
        for i in range(1, self.num_points):
            self.yi += self.stepsize * \
                       self.f(
                           self.xi + self.stepsize / 2, 
                           self.yi + self.stepsize / 2 * self.f(self.xi, self.yi)
                           )
            self.xi += self.stepsize
            self.Y[i] = self.yi
            self.X[i] = self.xi
        return self.X, self.Y


class TaylorMethod(Method):
    def __init__(self, f, d1f, d2f, d3f, num_points, y0):
        Method.__init__(self, f, num_points, y0)
        self.d1f = d1f
        self.d2f = d2f
        self.d3f = d3f 
        self.h1 = (self.stepsize ** 2) / 2
        self.h2 = (self.stepsize ** 3) / 6
        self.h3 = (self.stepsize ** 4) / 24
    def calculate(self):
        for i in range(1, self.num_points):
            self.yi += self.stepsize * self.f(self.xi, self.yi) + \
                       self.h1 * self.d1f(self.xi, self.yi) + \
                       self.h2 * self.d2f(self.xi, self.yi) + \
                       self.h3 * self.d3f(self.xi, self.yi)
            self.xi += self.stepsize
            self.Y[i] = self.yi
            self.X[i] = self.xi
        return self.X, self.Y
    


    