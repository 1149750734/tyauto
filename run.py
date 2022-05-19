# -*- encoding: utf-8 -*-
from tyauto.test_case.test_cases import TestCases
import unittest
import HTMLTestRunner
from tyauto.common import project_path
from tyauto.test_case import test_cases#具体到类
#新建一个测试集
suite=unittest.TestSuite()

#添加用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_cases))

#执行用例 生成测试报告
with open(project_path.report_path,'wb')as file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                     verbosity=2,
                                     title='测试报告',
                                     description='《特药理赔》测试报告',
                                     tester='Sally')
    runner.run(suite)#执行用例 传入suite suite里面是我们收集的测试用例


