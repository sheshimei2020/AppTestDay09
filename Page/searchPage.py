from Base.base import Base
from Page.pageElement import PageElement


class SearchPage(Base):

    def __init__(self):
        super().__init__()

    def input_search_text(self,text):
        # 输入搜索内容
        self.send_text_ele(PageElement.search_input_box, text)

    def get_search_result(self):
        # 获取所有搜索结果
        results = self.search_eles(PageElement.search_input_result)
        return [i.text for i in results]
