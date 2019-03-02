import tf_cnn_siamese.configurations as conf
import numpy as np


def generate_normalized_data(num_pairs):
  # pairs of tensors of images with dimention specified in conf
  x_1 = np.random.rand(num_pairs, conf.IMG_X, conf.IMG_Y).astype(conf.DTYPE)
  x_2 = np.random.rand(num_pairs, conf.IMG_X, conf.IMG_Y).astype(conf.DTYPE)
  # shfiting the range from (0, 1) to (-0.5, 0.5)
  x_1 -= 0.5
  x_2 -= 0.5
  labels = np.random.choice(a=[0, 1], size=num_pairs,
                            p=[0.48, 0.52]).astype(conf.DTYPE)
  return x_1, x_2, labels
