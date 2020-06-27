from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver


class Base:

    def __init__(self):
        self.driver = Driver.get_app_driver()


    def search_ele(self,loc,timeout=5,poll=1):
        """定义搜索单个元素的方法"""
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(*loc))

    def search_eles(self,loc,timeout=5,poll=1):
        """定义搜索一组元素的方法"""
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self,loc,timeout=5,poll=1):
        """定义点击元素的方法"""
        self.search_ele(loc,timeout,poll).click()

    def send_text_ele(self,loc,text,timeout=5,poll=1):
        """定义输入文本的方法"""
        # 定位输入框
        input_box = self.search_ele(loc,timeout,poll)
        # 清空输入框
        input_box.clear()
        # 输入文本
        input_box.send_keys(text)
