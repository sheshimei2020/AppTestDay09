import os

import pytest

import yaml

from Base.get_data import GetData


def read_sum_data():
    # 空列表存储数据
    sum_list = []
    # 打开文件
    # with open("./Data" + os.sep + "sum.yaml", "r") as f:
    #     #     # yaml读取文件
    #     #     data = yaml.safe_load(f)
    data = GetData.get_yaml_data("sum.yaml")
    # print("data:",data)
    # print("values:",data.values())  # 返回列表,存储所有的value
    for i in data.values():
        # print("tup:",(i.get("a"),i.get("b"),i.get("c")))
        # 添加元组数据到sum_list
        sum_list.append((i.get("a"), i.get("b"), i.get("c")))
# print("sum_list:", sum_list)
    return sum_list

class TestSum:
    # @pytest.mark.parametrize("a,b,c",[(1,2,3),(3,4,5),(4,5,9)])
    @pytest.mark.parametrize("a,b,c",read_sum_data())
    def test_sum(self,a,b,c):
        """判断两个数之和等于第三个数"""
        print("\n{}+{}={}".format(a,b,c))
        assert a + b == c