import numpy as np


def step_function(x: np.ndarray) -> np.ndarray:
    y = x > 0
    return y.astype(np.int)
