import yaml,os

class GetData:
    """读取测试数据"""
    @classmethod
    def get_yaml_data(cls,name):
        """
        :param name: 数据文件名字
        :return:
        """
        with open("./Data" + os.sep + name,"r",encoding="utf-8") as f:
            # yaml读取数据
            return yaml.safe_load(f)

    def get_csv_data(self):
        """读取csv文件数据"""
