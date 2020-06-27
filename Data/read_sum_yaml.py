import yaml

def read_sum_data():
    # 空列表存储数据
    sum_list = []
    # 打开文件
    with open("./sum.yaml","r") as f:
        # yaml读取文件
        data = yaml.safe_load(f)
        # print("data:",data)
        # print("values:",data.values())  # 返回列表,存储所有的value
        for i in data.values():
            # print("tup:",(i.get("a"),i.get("b"),i.get("c")))
            # 添加元组数据到sum_list
            sum_list.append((i.get("a"),i.get("b"),i.get("c")))

    print("sum_list:",sum_list)
    return sum_list