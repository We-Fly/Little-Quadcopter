import cv2
from src.shapedectct import Picture

# # 实例化一个新的对象 需要输入文件路径
# test = Picture("test.jpg")
# # 放一个文字，需要输入一个string
# test.putText("wwwwwwww")
#
# test.resize(500)
# # 展示图片
# test.show()

# 初始化摄像头，你们的应该是0或者1，我这边有两个所以是2
webcam = cv2.VideoCapture(2)

while 1:
    # 获取一帧图像
    (flag, stream) = webcam.read()
    # 转换成我们写的Picture类
    frame = Picture(stream)

    # Do something

    # 显示视频，按q退出
    cv2.imshow("capture", frame.img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
