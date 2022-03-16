import unittest
import HtmlTestRunner

if __name__ == '__main__':
    # 创建测试套件
    suite = unittest.TestSuite()

    # 找到某个目录下所有的以test开头的Python文件里面的测试用例
    all_cases = unittest.defaultTestLoader.discover('src', 'test_*.py')
    for case in all_cases:
        suite.addTests(case)

    runner = HtmlTestRunner.HTMLTestRunner(combine_reports = True, report_name = "测试报告", add_timestamp = True)
    runner.run(suite)