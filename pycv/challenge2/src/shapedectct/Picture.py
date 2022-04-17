import cv2 
from cv2 import imread

class Picture:                                                      #创建 Picture 类

    def __init__(self, path_to_img) -> None:                        #初始化函数，要实例化一个新的对象需要输入文件路径
        self.img = imread(path_to_img, cv2.IMREAD_COLOR)

    def putText(self, string_to_write):                             #实现 放一个文字，需要输入一个string
        org = (100, 100)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        lineType = cv2.LINE_AA
        self.img = cv2.putText(self.img, string_to_write, org, fontFace, fontScale, color, thickness, lineType)
        # cv2.imshow('image', img)
        # cv2.waitKey(0) 
        # cv2.destroyAllWindows() 
        
    def show(self):                                                 #实现 展示图片
        cv2.imshow("image", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


