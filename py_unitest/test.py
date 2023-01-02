from calculate import Count
import unittest           # 引入unittest模块

class TestAdd(unittest.TestCase):   # 创建TestAdd类，继承TestCase类
    def setUp(self):       # setUp()方法，用于测试用例执行前的初始化工作
        print('setUp')

    def tearDown(self):    # tearDown()方法，用于测试用例执行之后的善后工作
        print('tearDown')

    def test_add_1(self):   # 测试方法，必须以test开头
        print('add 1')
        self.assertEqual(Count(2, 4).add(), 6)  # 使用unittest框架提供的assertEqual()方法进行断言，assertEqual()方法由父类TestCase类继承而来，所以可以通过self调用


if __name__ == '__main__':
    unittest.main()    # 调用unittest的main()来执行测试用例