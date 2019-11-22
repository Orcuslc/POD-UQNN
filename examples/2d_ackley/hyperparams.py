"""Default hyperparameters for 2D Ackley Equation."""

import numpy as np
import tensorflow as tf


HP = {}
# Dimension of u(x, t, mu)
HP["n_v"] = 1
# Space
HP["n_x"] = 400
HP["x_min"] = -5
HP["x_max"] = +5.
HP["n_y"] = 400
HP["y_min"] = -5.
HP["y_max"] = +5.
# Time
HP["n_t"] = 0
# Snapshots count
HP["n_s"] = 1000
# POD stopping param
HP["eps"] = 1e-10
# Train/val split
HP["train_val_ratio"] = 0.5
# Deep NN hidden layers topology
HP["h_layers"] = [64, 64]
# Batch size for mini-batch training (0 means full-batch)
HP["batch_size"] = 0
# Setting up TF SGD-based optimizer
# HP["epochs"] = 100000
HP["epochs"] = 15000
HP["lr"] = 0.001
# HP["lambda"] = 1e-4
HP["lambda"] = 0.
# Frequency of the logger
HP["log_frequency"] = 1000
# Non-spatial params
HP["mu_min"] = [-1., -1., -1.]
HP["mu_max"] = [+1., +1., +1.]


np.random.seed(1111)
tf.random.set_seed(1111)
