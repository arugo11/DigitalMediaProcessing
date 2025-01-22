#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

#雛形特になし、自由に書いてみてください
import cv2
import numpy as np
import sys
import os



def quarter_swap(image):
    """
    四分割スワップ
    """
    h, w = image.shape

    h_top = h // 2
    h_bottom = h - h_top
    w_left = w // 2
    w_right = w - w_left

    # 結果用
    result = np.zeros_like(image)

    top_left = image[:h_top, :w_left]
    top_right = image[:h_top, w_left:]
    bottom_left = image[h_top:, :w_left]
    bottom_right = image[h_top:, w_left:]


    result[:h_bottom, :w_right] = bottom_right    # 右下 → 左上
    result[:h_bottom, w_right:] = bottom_left     # 左下 → 右上

    result[h_bottom:, :w_right] = top_right      # 右上 → 左下
    result[h_bottom:, w_right:] = top_left       # 左上 → 右下

    return result

def deconvolution_simple(img_path, kernel_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    kernel = cv2.imread(kernel_path, cv2.IMREAD_GRAYSCALE)

    # 0 ~ 255に正規化
    kernel = kernel.astype(np.float32) / 255.0
    kernel = kernel / np.sum(kernel)

    # カーネルをfftのためにイメージと同じサイズに調整
    #note 周波数領域だから位置は特に考えなくてよいので今回は左上に配置
    kernel_padded = np.zeros(img.shape, dtype=np.float32)
    kernel_h, kernel_w = kernel.shape
    kernel_padded[:kernel_h, :kernel_w] = kernel

    # fft
    IMG = np.fft.fft2(img)
    KERNEL = np.fft.fft2(kernel_padded)


    H = 1 / KERNEL

    # t値の調整
    H = np.where(np.abs(KERNEL) < 1e-2, 1e-2, H) #1e-2がよさげ


    F = H * IMG
    f = np.fft.ifft2(F)
    f = np.abs(f)
    f = f[:img.shape[0], :img.shape[1]]

    deconvolved_img = quarter_swap(f)


    return deconvolved_img

def deconvolution_wiener(img_path, kernel_path, K=1e-7):
    """
    Wienerフィルター
    """
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    kernel = cv2.imread(kernel_path, cv2.IMREAD_GRAYSCALE)


    kernel = kernel.astype(np.float32) / 255.0
    kernel = kernel / np.sum(kernel)

    # カーネルをfftのためにイメージと同じサイズに調整
    kernel_padded = np.zeros(img.shape, dtype=np.float32)
    kernel_h, kernel_w = kernel.shape
    kernel_padded[:kernel_h, :kernel_w] = kernel

    # fft
    IMG = np.fft.fft2(img)
    KERNEL = np.fft.fft2(kernel_padded)


    # Wienerフィルタ
    H = (np.conj(KERNEL)) / (np.abs(KERNEL)**2 + K) #Kは1e-7がよさげ

    F = H * IMG
    f = np.fft.ifft2(F)
    f = np.abs(f)
    f = f[:img.shape[0], :img.shape[1]]

    deconvolved_img = quarter_swap(f)


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
