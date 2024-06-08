import numpy as np

def det_inv(det):
    for i in range(1, 256):
        if (((i*det) % 256) == 1):
            return i


def key_inverse(key_matrix):
    det = (key_matrix[0, 0] * key_matrix[1, 1]) - (key_matrix[0, 1] * key_matrix[1, 0])
    det = det % 256
    x = det_inv(det)

    adj = np.array([
        [key_matrix[1, 1], -key_matrix[0, 1]],
        [-key_matrix[1, 0], key_matrix[0, 0]]
    ])
    adj = adj % 256

    inverse_key = (x * adj) % 256

    return inverse_key

