from selenium.webdriver.common.by import By


class PageElement:
    """管理页面所有元素"""
    """搜索页面元素"""
    search_btn = (By.ID, "com.android.settings:id/search")

    """搜索框输入页面元素"""
    search_input_box = (By.ID, "android:id/search_src_text")
    # 获取搜索结果信息
    search_input_result = (By.ID, "com.android.settings:id/title")

