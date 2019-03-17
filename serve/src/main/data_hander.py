#encoding=utf-8
import os
import numpy as np
from .. import util

year_range = range(1960, 2016 + 1)


def calc_data_by_year():
    # 获取基础目录内的文件列表
    file_list = os.listdir(util.path.origin_data)

    # 过滤掉不需要的文件
    file_list = list(filter(lambda s:s.find('zh') == -1 and s.find('Indicator') == -1, file_list))

    # 按文件名称进行排序
    file_list.sort()

    # 需要输出的文件
    data_by_year = {}

    # 属性列表, 最后会加入输出文件
    indicator_codes = []

    # 初始化
    for year in year_range:
        data_by_year[str(year)] = []
    
    # 遍历每个国家
    for file_name in file_list:
        # 读取国家数据
        csv_data = util.open_csv(util.path.origin_data + file_name)

        # 该国家的数据
        country_data = {}

        # 初始化
        for year in year_range:
            country_data[str(year)] = []

        # 遍历每一年
        row_range = range(4, 60 + 1)
        for row_index in row_range:
            now_year = str(csv_data[0][row_index])
            for line in csv_data:
                # 过滤掉第一行
                if line[0] == 'CountryName':
                    continue

                # 添加indicator数组
                if line[3] not in indicator_codes:
                    indicator_codes.append(line[3])
                country_data[now_year].append(float(line[row_index]) if len(line[row_index])>0 else 0)


        for now_year in year_range:
            now_year = str(now_year)
            data_by_year[now_year].append(country_data[now_year])

    # 遍历每一年的统计数据 ，删去空属性，并按年保存数据
    for now_year in year_range:
        now_year = str(now_year)

        # 对每一列进行求和
        col_sum = np.sum(data_by_year[now_year],axis=0)
        
        # 筛选出求和结果为0的属性
        empty_rows = []
        for col in range(0, len(col_sum)):
            if col_sum[col] == 0:
                empty_rows.append(col)

        # 在第一行插入indicator_code
        data_by_year[now_year].insert(0,indicator_codes)

        # 删除求和结果为0的列
        data_by_year[now_year] = np.delete(data_by_year[now_year], empty_rows, axis=1)

        # 保存数据
        util.save_csv(data_by_year[now_year],util.path.data_by_year + now_year)




calc_data_by_year()