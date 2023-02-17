# 基于 BouncingBall 模型的降阶模型
#
# 通过深度学习方法拟合 BouncingBall 模型的结果从而实现缩短模拟时间的目的。对于
# BouncingBall 来说，这个操作可能并没有什么太大的意义。但是对于某些极其复杂的大
# 型模型来说，这将大大压缩计算时间，并且精确度不会有太大的变化。
#
# 陈立明 2023.2.17

from iteration import Iterator
from resultplot import basic_2d_plot

import numpy as np


def get_model_result():
    """
    获取 Bouncing Ball 模型的结果，其代码和 Simple 算例中的 BouncingBall 完全一致
    :return:
    """
    def bouncing_ball(data):
        data['t'] = data['t'] + data['der(t)']
        data['der(h)'] = data['v']
        data['der(v)'] = data['g']
        data['h'] = data['h'] + data['der(t)'] * data['der(h)']
        data['v'] = data['v'] + data['der(t)'] * data['der(v)']
        if data['h'] < 0:
            data['h'] = - data['h']
            data['v'] = - data['v'] * data['e']
        return data

    def termination(data):
        if data['t'] > 3:
            return True
        else:
            return False

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
    start_data = np.array(
        (0, 0.001, 1, 0, 0, 0, 0.7, -9.8),
        dtype=dtype
    )
    model = Iterator(
        start_data=start_data,
        iterative_method=bouncing_ball,
        termination_method=termination,
    )
    return model.run()
