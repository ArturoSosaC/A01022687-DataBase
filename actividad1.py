import numpy as np
from io_utilities import load_data


def main():
    data = load_data('./TextFiles/populationbycountry19802010millions.csv')
    # print (data)
    x = np.array([f[:-1] for f in data])
    y = np.array([f[-1] for f in data])
    print(y)

main()
