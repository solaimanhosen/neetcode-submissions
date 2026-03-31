class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        if iterations == 0:
            return init

        x = float(init)
        for _ in range(iterations):
            x = x - learning_rate * (2 * x)

        return round(x, 5)
