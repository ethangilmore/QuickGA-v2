# Quick GA

## Example Usage

```python
from quickga import Organism
from quickga.traits import FloatTrait

class LinearRegression(Organism):

    def __init__(self, points):
        # pass all init arguments to the base class
        super().__init__(points)
        self.points = points

        # define the traits of our organism - these are what will be optimized
        self.slope = FloatTrait(min_value=-10, max_value=10)
        self.y_intercept = FloatTrait(min_value=-10, max_value=10)

    def fitness_function(self):
        # define the linear function using slope and y-intercept
        f = lambda x: self.slope * x + self.y_intercept
        # calculate the mean squared error for our function on the points
        mse = sum([(f(x) - y)**2 for x, y in self.points])
        # a higher fitness is better, so we return the inverse of the mse
        return 1/mse

points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
lr = LinearRegression(points)
lr.evolve(population_size=100, num_generations=500)
print(lr.slope, lr.y_intercept)
```