import numpy as np
import os
import sys

sys.path.append("utils")


def create_linear_mesh(x_min, x_max, n_x,
                       y_min=None, y_max=None, n_y=None,
                       z_min=None, z_max=None, n_z=None):
    dim = 1
    n_nodes = n_x

    x = np.linspace(x_min, x_max, n_x).reshape((n_x, 1))

    if y_min is not None and y_max is not None and \
       n_y is not None:
        dim += 1
        n_nodes *= n_y
        y = np.linspace(y_min, y_max, n_y).reshape((n_y, 1))

        if z_min is not None and z_max is not None and \
           n_z is not None:
            dim += 1
            n_nodes *= n_z
            z = np.linspace(z_min, z_max, n_z).reshape((n_z, 1))

            X, Y, Z = np.meshgrid(x, y, z)
            Xflat = X.reshape((n_nodes, 1))
            Yflat = Y.reshape((n_nodes, 1))
            Zflat = Z.reshape((n_nodes, 1))
            idx = np.array(range(1, n_nodes + 1)).reshape((n_nodes, 1))
            return np.hstack((idx, Xflat, Yflat, Zflat))

        X, Y = np.meshgrid(x, y)
        Xflat, Yflat = X.reshape((n_nodes, 1)), Y.reshape((n_nodes, 1))
        idx = np.array(range(1, n_nodes + 1)).reshape((n_nodes, 1))
        return np.hstack((idx, Xflat, Yflat))

    idx = np.array(range(1, n_nodes + 1)).reshape((n_nodes, 1))
    return np.hstack((idx, x))

if __name__ == "__main__":
    print(create_linear_mesh(0, 1, 10))
    print(create_linear_mesh(0, 1, 10, 1, 2, 5))
    print(create_linear_mesh(0, 1, 2, 1, 2, 5, 2, 3, 3))
