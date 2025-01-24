#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

#雛形特になし、自由に書いてみてください
import cv2
import numpy as np
import sys
import os



def deconvolution_simple(img_path, kernel_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    kernel = cv2.imread(kernel_path, cv2.IMREAD_GRAYSCALE)

    # 0 ~ 255に正規化
    kernel = kernel.astype(np.float32) / 255.0
    kernel = kernel / np.sum(kernel)

    # fft
    IMG = np.fft.fft2(img)
    KERNEL = np.fft.fft2(kernel)

    H = 1 / KERNEL

    # t値の調整
    H = np.where(np.abs(KERNEL) < 1e-2, 1e-2, H) #1e-2がよさげ


    F = H * IMG
    f = np.fft.ifft2(F)
    f = np.real(f)
    f = f[:img.shape[0], :img.shape[1]]

    deconvolved_img = np.fft.fftshift(f)


    return deconvolved_img

def deconvolution_wiener(img_path, kernel_path, k=1e-7):
    """
    Wienerフィルター
    """
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    kernel = cv2.imread(kernel_path, cv2.IMREAD_GRAYSCALE)


    kernel = kernel.astype(np.float32) / 255.0
    kernel = kernel / np.sum(kernel)


    # fft
    IMG = np.fft.fft2(img)
    KERNEL = np.fft.fft2(kernel)


    # Wienerフィルタ
    H = (np.conj(KERNEL)) / (np.real(KERNEL)**2 + k) #kは1e-7がよさげ

    F = H * IMG
    f = np.fft.ifft2(F)
    f = np.real(f)
    f = f[:img.shape[0], :img.shape[1]]

    deconvolved_img = np.fft.fftshift(f)


    return deconvolved_img

if __name__ == "__main__":

    img_path = sys.argv[1]
    kernel_path = sys.argv[2]

    deconvolved_img_simple = deconvolution_simple(img_path, kernel_path)
    deconvolved_img_wiener = deconvolution_wiener(img_path, kernel_path)

    basename = os.path.basename(img_path)
    filename = basename.split("_")[0]
    output_simple = os.path.join("out", filename + "_dec_simple.png")
    output_wiener = os.path.join("out", filename + "_dec_wie.png")


    cv2.imwrite(output_simple, deconvolved_img_simple)
    cv2.imwrite(output_wiener, deconvolved_img_wiener)
