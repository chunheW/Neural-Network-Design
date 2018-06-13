"""
Consider a Hopfield network, with the follwing weight and bias.

W = [[1, -1], [-1, 1]]  b = [0, 0].T

i.   The following input (initial condition) is applied to the network.  Find the network response (show the network output at each iteration until the network converges).
        p = [0.9, 1].T
ii.  Draw a sketch indicating what region of the input space will converge to the same final output that you found in part i. (In other words, for what other p vectors will
     the network converge to the same final output?) Explain how you obtained your answer.
iii. What other prototypes will this network converge to, and what regions of the input space corresponds to each prototype (sket the regions).  Explain how you obtained your answer.
"""

import numpy as np
import matplotlib.pyplot as plt

from HopfieldNetwork import HopfieldNetwork

if __name__ == "__main__":
    print("Consider a Hopfield network, with the follwing weight and bias.", "\n\tW = [[1, -1], [-1, 1]]  b = [0, 0].T")

    weights = np.array([[1, -1], [-1, 1]])
    bias = np.array([0, 0]).reshape((2, 1))

    test_input = np.array([0.9, 1]).reshape((2, 1))

    e3_3Network = HopfieldNetwork(weights= weights, bias = bias)
    e3_3Network.classify(a0 = test_input)

    print("\ni.   The following input (initial condition) is applied to the network.  Find the network response (show the network output at each iteration until the network converges).", "\n\tp = [0.9, 1].T")
    print("Listing activations")
    for index, activation in enumerate(e3_3Network.activations):
        print("\n", index, activation)


    print("\nii.  Draw a sketch indicating what region of the input space will converge to the same final output that you found in part i. (In other words, for what other p vectors will the network converge to the same final output?) Explain how you obtained your answer.")
    x = np.linspace(-50,50)
    y = x
    y_edge = np.linspace(50,50)
    plt.plot(x,y)
    plt.fill_between(x, y, y_edge, where = y_edge > y)
    plt.grid(True)
    plt.show()

    print("\niii. What other prototypes will this network converge to, and what regions of the input space corresponds to each prototype (sket the regions).  Explain how you obtained your answer.")
    print("All prototypes above the line x=y because this is the decision matrix that would be generated by a weight = [[1, -1], [-1, 1]] and bias = [0, 0]")