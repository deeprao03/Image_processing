import numpy as np

def global_hist_eq(img):

    M, N = img.shape
    hist = np.zeros(256, dtype=int)

    for i in range(M):
        for j in range(N):
            hist[img[i, j]] += 1

    pdf = hist / (M * N)

    cdf = np.zeros(256)
    cdf[0] = pdf[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + pdf[i]

    out = np.zeros_like(img)

    for i in range(M):
        for j in range(N):
            out[i, j] = round(255 * cdf[img[i, j]])

    return out.astype(np.uint8)


def local_hist_eq(img):

    M, N = img.shape
    out = np.zeros_like(img)

    padded = np.pad(img, 1, mode='edge')

    for i in range(M):
        for j in range(N):

            window = padded[i:i+3, j:j+3]

            hist = np.zeros(256, dtype=int)
            for x in range(3):
                for y in range(3):
                    hist[window[x, y]] += 1

            pdf = hist / 9.0

            cdf = np.zeros(256)
            cdf[0] = pdf[0]
            for k in range(1, 256):
                cdf[k] = cdf[k - 1] + pdf[k]

            out[i, j] = round(255 * cdf[img[i, j]])

    return out.astype(np.uint8)
