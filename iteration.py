# AISimulation 的迭代器
#
# 该模块提供了一个基本的迭代框架以供使用
#
# 陈立明 2023.2.16

import numpy as np


class Iterator:
    """
    一个迭代器类。

    迭代器是人工智能和仿真的根本。因为相比人来说，计算机更适合处理这些重
    复的事情，而迭代即意味着这个程序会反反复复的根据一个算法反复的计算。

    所以，在这个模块中，我们构建了一个基本的迭代框架，以便大家的使用。
    """
    def __init__(
            self,
            start_data,
            iterative_method,
            termination_method,
            max_iterations=np.inf,
    ):
        """
        初始化迭代器
        :param start_data: 初始数据
        :param iterative_method: 迭代方法
        :param termination_method: 终止方法
        :param max_iterations: 最大迭代次数
        """
        # 数据初始化
        self.data = start_data
        self.max_iterations = max_iterations
        self.iterations = 0

        # 是否终止
        self.terminate = False

        # 方法初始化
        self.iterative_method = iterative_method
        self.termination_method = termination_method

    def forward(self):
        """
        前向计算函数，用来计算下一迭代步 data 的值
        :return: None
        """
        # 步进
        self.iterations += 1
        self.iterative_method(self.data)

        # 检测是否继续迭代
        if self.iterations >= self.max_iterations:
            self.terminate = True
        if self.termination_method(self.data):
            self.terminate = True

    def run(self):
        """
        运行函数，调用该函数完成整个迭代过程
        :return: 运行的全历史
        """
        # 定义结果类型
        result = []

        # 开始迭代
        while not self.terminate:
            # 前向计算
            self.forward()
            result.append(np.array(self.data))

        # 整理并返回数据
        return np.array(result, dtype=self.data.dtype)
