from Page.searchPage import SearchPage
from Page.settingPage import SettingPage


class Page:

    """返回所有页面类的实例化对象"""
    @classmethod
    def get_setting_page(cls):
        return SettingPage()

    @classmethod
    def get_search_page(cls):
        return SearchPage()