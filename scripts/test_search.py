import pytest

from Base.driver import Driver
from Base.page import Page


class TestSearch:

    def teardown_class(self):
        Driver.quit_app_driver()

    @pytest.fixture(scope='class',autouse=True)
    def click_search_btn(self):
        """点击搜索按钮"""
        Page.get_setting_page().click_search_btn()

    @pytest.mark.parametrize("search_text,expect_result",[("1","休眠"),("i","IP地址"),("m","MAC地址")])
    def test_search(self,search_text,expect_result):
        # 输入搜索内容
        Page.get_search_page().input_search_text(search_text)
        # 获取结果并断言
        assert expect_result in Page.get_search_page().get_search_result()
