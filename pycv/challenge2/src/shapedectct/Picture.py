import cv2
import imutils
from cv2 import imread


class Picture:  # 针对图片的操作

    def __init__(self, path_to_img) -> None:  # 初始化函数，要实例化一个新的对象需要输入文件路径
        self.modify = None
        self.img = None
        if isinstance(path_to_img, str):
            self.img = imread(path_to_img, cv2.IMREAD_COLOR)
        else:
            self.img = path_to_img

    def putText(self, string_to_write,  # 要放的字
                put_where=(100, 100),  # 坐标
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                fontScale=3,  # 大小
                color=(255, 0, 0),  # 颜色
                thickness=2,  # 粗细
                lineType=cv2.LINE_AA  # 线型
                ) -> None:  # 实现 放一个文字，至少需要输入一个string
        self.img = cv2.putText(self.img, string_to_write, put_where, fontFace, fontScale, color, thickness, lineType)

    def show(self) -> None:  # 实现 展示图片
        cv2.imshow("image", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def resize(self, width) -> None:  # 缩放，输入宽度px
        self.img = imutils.resize(self.img, width)

    def gray(self) -> None:  # 黑白
        self.modify = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def blur(self, ksize=(5, 5), sigmaX=0) -> None:  # 高斯模糊
        self.modify = cv2.GaussianBlur(self.modify, ksize, sigmaX)

    def threshold(self, thresh=60, maxval=255) -> None:  # 二值化
        self.modify = cv2.threshold(self.modify, thresh, maxval, cv2.THRESH_BINARY)[1]
