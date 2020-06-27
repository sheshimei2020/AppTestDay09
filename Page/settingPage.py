from Base.base import Base
from Page.pageElement import PageElement


class SettingPage(Base):
    def __init__(self):
        super().__init__()


    def click_search_btn(self):
        # 点击搜索按钮
        self.click_ele(PageElement.search_btn)
