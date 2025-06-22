import numpy as np
from PIL import Image
import cv2

def pca(matrix, k):
    # Langkah 1: Mengurangi rata-rata dari setiap kolom (mean centering)
    mean = np.mean(matrix, axis=0)
    centered = matrix - mean

    # Langkah 2: Menghitung matriks kovarian
    covariance = np.cov(centered, rowvar=False)

    # Langkah 3: Eigen decomposition
    eigVal, eigVec = np.linalg.eigh(covariance)

    # Langkah 4: Mengurutkan eigenvalue dan eigenvector dari yang terbesar
    idx = eigVal.argsort()[::-1]
    eigVal = eigVal[idx]
    eigVec = eigVec[:, idx]

    # Langkah 5: Memilih k komponen utama (principal components) teratas
    eigVec = eigVec[:, :k]

    # Langkah 6: Memproyeksikan data ke ruang dimensi baru (kompresi)
    compressed = np.dot(centered, eigVec)

    # Langkah 7: Merekonstruksi data dari hasil kompresi
    reconstructed = np.dot(compressed, eigVec.T) + mean

    return reconstructed

def compress(img, percentage):
    # kompresi PCA
    img = img.astype(np.float32)
    m, n = img.shape[0], img.shape[1]
    percent = percentage / 100
    k = round((m * n) * percent / (m + n + 1))

    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    try: a = img[:, :, 3]
    except: a = None

    b_comp = pca(b, k)
    g_comp = pca(g, k)
    r_comp = pca(r, k)

    if a is not None:
        a_comp = pca(a, k)

    redImg = Image.fromarray(np.clip(r_comp, 0, 255)).convert("L")
    greenImg = Image.fromarray(np.clip(g_comp, 0, 255)).convert("L")
    blueImg = Image.fromarray(np.clip(b_comp, 0, 255)).convert("L")

    if a is not None:
        alphaImg = Image.fromarray(np.clip(a_comp, 0, 255)).convert("L")
        imgScaled = Image.merge("RGBA", (redImg, greenImg, blueImg, alphaImg))
        opencvimg = cv2.cvtColor(np.array(imgScaled), cv2.COLOR_RGBA2BGRA)
    else:
        imgScaled = Image.merge("RGB", (redImg, greenImg, blueImg))
        opencvimg = cv2.cvtColor(np.array(imgScaled), cv2.COLOR_RGB2BGR)

    return opencvimg