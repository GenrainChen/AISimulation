# BouncingBall 弹跳球模型，描述了一个小球从空中自由落体并不断撞击地面反弹的模型
#
# 陈立明 2023.2.16

from AISimulation.iteration import Iterator
from AISimulation.resultplot import basic_2d_plot

import numpy as np


def bouncing_ball(data):
    """
    BouncingBall 模型，小球只受重力加速度影响。当小球撞击地面时，会损失 30% 的
    动能。
    :param data: 输入数据
    :return: 返回数据
    """
    # 步进方向为时间
    data['t'] = data['t'] + data['der(t)']

    # 计算导数的大小
    data['der(h)'] = data['v']
    data['der(v)'] = data['g']

    # 使用前向欧拉法进行迭代
    data['h'] = data['h'] + data['der(t)'] * data['der(h)']
    data['v'] = data['v'] + data['der(t)'] * data['der(v)']

    # 检查小球是否撞击地面
    if data['h'] < 0:
        data['h'] = - data['h']
        data['v'] = - data['v'] * data['e']  # 速度相反，并且能量产生一定损耗

    # 返回数据
    return data


def termination(data):
    """
    终止函数，检测迭代是否应当停止
    :param data: 输入数据
    :return: 输出 True 或者 False，如果为 Ture 则表明应当终止迭代
    """
    # 当时间大于 3s 时，停止模拟
    if data['t'] > 3:
        return True
    else:
        return False


if __name__ == '__main__':
    # 定义数据类型
    dtype = np.dtype([
        ("t", np.float64),
        ("der(t)", np.float64),
        ("h", np.float64),
        ("der(h)", np.float64),
        ("v", np.float64),
        ("der(v)", np.float64),
        ("e", np.float64),
        ("g", np.float64),
    ])

    # 定义初始值
    start_data = np.array(
        (0, 0.001, 1, 0, 0, 0, 0.7, -9.8),
        dtype=dtype
    )

    # 实例化模型
    model = Iterator(
        start_data=start_data,
        iterative_method=bouncing_ball,
        termination_method=termination,
    )

    # 进行迭代
    result = model.run()

    # 结果展示
    basic_2d_plot(result, 't', 'h')
    basic_2d_plot(result, 't', 'v')
