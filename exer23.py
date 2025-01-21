#dm2024 1bc36c9b73b21cad239bf4d37aa34f3ad5d42093064e17d1f87d7bb079e60ffe#
#dm template
# これより上は編集しないこと

#雛形特になし、自由に書いてみてください
import cv2
import numpy as np
import sys
import os

def normalize(image, out_min=0, out_max=255):
    # float32型に変換
    img = image.astype(np.float32)
    
    # 最小値と最大値を取得
    in_min = np.min(img)
    in_max = np.max(img)
    
    # 最小-最大正規化の実行
    normalized = (img - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    # 8ビット整数型に変換
    result = np.clip(normalized, 0, 255).astype(np.uint8)
    
    return result

def quarter_swap(image):
    """
    奇数サイズの画像にも対応した四分割スワップの実装
    """
    h, w = image.shape
    
    # 上下、左右の分割位置を計算（切り上げと切り捨てを考慮）
    h_top = h // 2
    h_bottom = h - h_top
    w_left = w // 2
    w_right = w - w_left
    
    # 結果用の配列を作成
    result = np.zeros_like(image)
    
    # 元の画像の4つの部分を取得
    top_left = image[:h_top, :w_left]
    top_right = image[:h_top, w_left:]
    bottom_left = image[h_top:, :w_left]
    bottom_right = image[h_top:, w_left:]
    
    # 新しい位置に配置（サイズを明示的に指定）
    # 下半分
    result[:h_bottom, :w_right] = bottom_right    # B2 → 左上
    result[:h_bottom, w_right:] = bottom_left     # B1 → 右上
    # 上半分
    result[h_bottom:, :w_right] = top_right      # A2 → 左下
    result[h_bottom:, w_right:] = top_left       # A1 → 右下
    
    return result

def deconvolution_simple(img_path, kernel_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    kernel = cv2.imread(kernel_path, cv2.IMREAD_GRAYSCALE)


    kernel = kernel.astype(np.float32) / 255.0
    kernel = kernel / np.sum(kernel)

    # カーネルをイメージ画像と同じサイズに調整
    kernel_padded = np.zeros(img.shape, dtype=np.float32)
    kernel_h, kernel_w = kernel.shape
    kernel_padded[:kernel_h, :kernel_w] = kernel

    # フーリエ変換
    IMG = np.fft.fft2(img)
    KERNEL = np.fft.fft2(kernel_padded)


    H = 1 / KERNEL

    # t値の調整
    H = np.where(np.abs(KERNEL) < 1e-2, 1e-2, H) #0に近い値は1e-2にする


    F = H * IMG
    f = np.fft.ifft2(F)
    f = np.abs(f)
    f = f[:img.shape[0], :img.shape[1]] #トリミング

    deconvolved_img = quarter_swap(normalize(f))


    return deconvolved_img

def deconvolution_wiener(img_path, kernel_path, K=1e-7):  # Kを追加
    """
    Wienerフィルターを用いてデコンボリューションを行う。
    """
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    kernel = cv2.imread(kernel_path, cv2.IMREAD_GRAYSCALE)


    kernel = kernel.astype(np.float32) / 255.0
    kernel = kernel / np.sum(kernel)

    # 画像サイズに合わせる
    kernel_padded = np.zeros(img.shape, dtype=np.float32)
    kernel_h, kernel_w = kernel.shape
    kernel_padded[:kernel_h, :kernel_w] = kernel

    # フーリエ変換
    IMG = np.fft.fft2(img)
    KERNEL = np.fft.fft2(kernel_padded)


    # Wienerフィルタの適用 (Kは調整が必要)
    H = (np.conj(KERNEL) * np.abs(KERNEL)**2) / (np.abs(KERNEL)**4 + K) #Kはハイパーパラメータ

    F = H * IMG
    f = np.fft.ifft2(F)
    f = np.abs(f)
    f = f[:img.shape[0], :img.shape[1]]

    deconvolved_img = quarter_swap(normalize(f))


    return deconvolved_img

if __name__ == "__main__":

    img_path = sys.argv[1]
    kernel_path = sys.argv[2]

    # 逆畳み込みの実行
    deconvolved_img_simple = deconvolution_simple(img_path, kernel_path)
    deconvolved_img_wiener = deconvolution_wiener(img_path, kernel_path)

    # 出力ファイル名の決定
    basename = os.path.basename(img_path)
    filename = basename.split("_")[0]
    output_simple = os.path.join("out", filename + "_dec_simple.png")
    output_wiener = os.path.join("out", filename + "_dec_wie.png")

    # 画像の保存
    if deconvolved_img_simple is not None:
        cv2.imwrite(output_simple, deconvolved_img_simple)
        print(f"Deconvolved image (simple) saved to: {output_simple}")

    if deconvolved_img_wiener is not None:
        cv2.imwrite(output_wiener, deconvolved_img_wiener)
        print(f"Deconvolved image (Wiener) saved to: {output_wiener}")