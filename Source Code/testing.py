import numpy as np
import os
import pandas as pd

temperature = np.linspace(0.3,3,109)
temperature = np.delete(temperature,[25,26,27,53,54,55,81,82,83])
print(temperature)
