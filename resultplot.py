# AISimulation 的数据展示
#
# 该模块提供了一个基本的数据展示框架以供使用
#
# 陈立明 2023.2.16

import matplotlib.pyplot as plt


def basic_2d_plot(data, x_name, y_name):
    """
    展示一个简单的 matplotlib 库的 2Dplot
    :param data: 数据
    :param x_name: x 坐标的名称
    :param y_name: y 坐标的名称
    :return: None
    """
    plt.figure(figsize=(7.2, 4.8))
    plt.plot(data[x_name], data[y_name])
    plt.title('{} VS. {}'.format(y_name, x_name), fontdict={'fontsize': 20}, y=1.02)
    plt.xlabel('{}'.format(x_name), fontdict={'fontsize': 18})
    plt.ylabel('{}'.format(y_name), fontdict={'fontsize': 18})
    plt.grid()
    plt.show()
