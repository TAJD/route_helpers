"""
Performance

Functions assisting with the generation of synthetic performance values.

Thomas Dickson
12/03/2019
thomas.dickson@soton.ac.uk
"""
import numpy as np, os
from scipy.interpolate import Rbf


def generate_performance_and_save(lower_twa, x_tws, ratio, path=None):
    """Generate and save synthetic sailing craft performance varying windward capability and wind power conversion efficiency."""
    x_tws, xi, performance = generate_performance(lower_twa, x_tws, ratio)
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)
    if path == None:
        path = os.getcwd()
    name = path+"/performance_"+str(lower_twa)+"_"+str(ratio)+".txt"
    print(str(name))
    with open(name, 'w') as f:
        f.write(np.array2string(x_tws, separator=', '))
        f.write("\n")
        f.write(np.array2string(xi, separator=', '))
        f.write("\n")
        f.write(np.array2string(performance, separator=', '))


def generate_performance(lower_twa, x_tws, ratio):
    """Generate and save synthetic sailing craft performance varying windward capability and wind power conversion efficiency."""
    x_twa = np.array([lower_twa, lower_twa+(180.0-lower_twa)/2, 180.0])
    y_bsp = np.zeros(shape=(x_twa.shape[0], x_tws.shape[0]))
    for i in range(x_tws.shape[0]-2):
        y_bsp[1:, i+1] = x_tws[i+1]*ratio
    xi = np.linspace(np.min(x_twa), np.max(x_twa), 21)
    performance = np.empty(shape=[len(xi), len(x_tws)])
    for i in range(len(x_tws)):
        rbf = Rbf(x_twa, y_bsp[:, i])
        performance[:, i] = rbf(xi)
    return x_tws, xi, performance


def generate_circular_performance(lower_twa, x_tws, ratio, path=None):
    x_twa = np.linspace(lower_twa, 180.0)
    y_bsp = np.zeros(shape=(x_twa.shape[0], x_tws.shape[0]))
    for i in range(x_tws.shape[0]-2):
        y_bsp[1:, i+1] = x_tws[i+1]*ratio
    performance = np.empty(shape=(x_twa.shape[0], x_tws.shape[0]))
    plt.figure(figsize=(6,6))
    ax = plt.subplot(111, projection='polar')
    ax.set_theta_zero_location("N")
    for i in range(len(x_tws)):
        performance[:, i] = y_bsp[:, i]
    return x_tws, x_twa, performance
