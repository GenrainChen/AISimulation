"""一款结合人工智能和仿真的 Python 第三方库

AISimulation 是一款结合人工智能和仿真的工具，其注释完全由中文组成，希望各位能够
流利的使用该库。通过这个工具，大家可以通过非常简单的代码来构建人工智能系统或者仿真
系统，亦或者这两者的结合。也可以仔细了解该库的构成及其源代码，深入了解人工智能和仿
真的奥妙，并对其结合模式一探究竟。

对于这个库的使用方法，我的建议是直接对示例代码进行修改，当熟练后再自行构建。示例代
码被分成了三个难度等级，大家可以根据自己的需求选择合适的代码进行修改。

示例代码：
from AISimulation.iteration import Iterator
from AISimulation.resultplot import basic_2d_plot

import numpy as np


def dahlquist(data):
    # 步进方向为时间
    data['t'] = data['t'] + data['der(t)']

    # 根据步进方向求导数
    data['x'] = data['x'] + data['der(t)'] * data['der(x)']

    # Dahlquist 的一阶方程
    data['der(x)'] = - data['k'] * data['x']

    # 返回数据
    return data


def termination(data):
    # 当时间大于5的时候停止
    if data['t'] > 5:
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
    start_data = np.array([
        (0, 1, 0, 1, 0.01)
    ], dtype=dtype)

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
"""