# Dahlquist 测试方程

from AISimulation.iteration import Iterator
from AISimulation.result_plot import basic_2d_plot

import numpy as np


def dahlquist(data):
    """
    Dahlquist 测试函数，是一个简单的一阶微分方程
    :param data: 输入数据
    :return: 返回数据
    """
    # 步进方向为时间
    data['t'] = data['t'] + data['der(t)']

    # 使用前向欧拉法进行迭代
    data['x'] = data['x'] + data['der(t)'] * data['der(x)']

    # Dahlquist 的一阶微分方程
    data['der(x)'] = - data['k'] * data['x']

    # 返回数据
    return data


def termination(data):
    """
    终止函数，检测迭代是否应当停止
    :param data: 输入数据
    :return: 输出 True 或者 False，如果为 Ture 则表明应当终止迭代
    """
    # 当时间大于10的时候停止
    if data['t'] > 10:
        return True
    else:
        return False


if __name__ == '__main__':
    # 定义数据类型
    dtype = np.dtype([
        ("t", np.float64),
        ("der(t)", np.float64),
        ("x", np.float64),
        ("der(x)", np.float64),
        ("k", np.float64),
    ])

    # 定义初始值
    start_data = np.array(
        (0, 0.001, 1, 0, 1),
        dtype=dtype
    )

    # 实例化模型
    model = Iterator(
        start_data=start_data,
        iterative_method=dahlquist,
        termination_method=termination
    )

    # 进行迭代
    result = model.run()

    # 结果展示
    basic_2d_plot(result, 't', 'x')
