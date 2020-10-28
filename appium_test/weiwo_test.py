from appium import webdriver
import time

'''
# 封装翻页类
class SwipeMethod:
    def __init__(self,driver=None):
        self.pm_size=self.swipeSize()
        
    # 获取屏幕尺寸
    def swipeSize(self):
        return driver.get_window_size()
'''


# 向上滑动屏幕
def swipeUp(driver,t=500,n=1):
    l = driver.get_window_size()
    x1 = l['width']*0.5  # x坐标
    y1 = l['height'] * 0.75  # 起始y坐标
    y2 = l['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


# 向下滑动屏幕
def swipeDown(driver,t=500,n=1):
    l = driver.get_window_size()
    x1 = l['width']*0.5  # x坐标
    y1 = l['height'] * 0.25  # 起始y坐标
    y2 = l['height'] * 0.75  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


# 向左滑动屏幕
def swipeLeft(driver,t=500,n=1):
    l = driver.get_window_size()
    x1 = l['width']*0.75  # 起始x坐标
    y1 = l['height'] * 0.5  # y坐标
    x2 = l['width'] * 0.05  # 终点x坐标
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


# 向右滑动屏幕
def swipeRight(driver,t=500,n=1):
    l = driver.get_window_size()
    x1 = l['width']*0.05  # 起始x坐标
    y1 = l['height'] * 0.5  # y坐标
    x2 = l['width'] * 0.75  # 终点x坐标
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


desired_caps = {
    'platformName': 'Android',  # 设备系统
    'deviceName': 'CLB7N19220001104',  # 手机设备名称，通过adb devices查看
    'platformVersion': '10.0.0',  # 设备系统的版本号
    'appPackage': 'com.shanxitianwei.weiwopark',  # apk包名
    'appActivity': 'com.shanxitianwei.weiwopark.activity.other.SplashActivity'  # apk的launcherActivity
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# 休眠五秒等待页面加载完成
time.sleep(5)
swipeLeft(driver,n=2)  # 向右滑动两个页面

# 通过坐标定位到‘立即体验’按钮并点击
time.sleep(5)
# a1 = 540/1080
# b1 = 1553/2244
x = driver.get_window_size()['width']*0.5
y = driver.get_window_size()['height']*0.7
driver.tap([(x,y)])  #([(a1*X, b1*Y)])

# 通过坐标定位到‘立即体验’按钮并点击
time.sleep(5)
x = driver.get_window_size()['width']*0.5
y = driver.get_window_size()['height']*0.7
driver.tap([(x,y)])


# driver.find_element_by_id('com.shanxitianwei.weiwopark:id/iv_center').click()
