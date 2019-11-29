# coding:utf-8
from util.send_mail import main3
import datetime
from new_api_cases.execute_cases import deal_request_method
from new_api_cases.execute_cases import CheckResult
from basic_info.setting import host
from basic_info.setting import receivers_list,receivers_test
from jihuo.acvt import isA

# from newSuite import NewSuite

# 添加用例集的API用例。暂停执行该用例集!
# testcase = unittest.TestSuite()
# discover = unittest.defaultTestLoader.discover(start_dir='./api_test_cases', pattern='cases_for_*.py')
# for test_suite in discover:
#     for test_case in test_suite:
#         # print(test_case)
#         testcase.addTest(test_case)
# filename = time.strftime("%Y%m%d%H", time.localtime()) + '_report.html'
# # report_path = 'E:\Reports\\' + filename
# # report_path = '/root/gbj/Reports/' + filename  # 192.168.1.87环境Jenkins使用
# report_path = './Reports/' + filename  # 192.168.1.87环境Jenkins使用
# fp = open(report_path, 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='API自动化测试报告', description='覆盖dataset,schema,schedulers,execution等测试场景')
# print('开始执行用例集用例')
# runner.run(testcase)
# fp.close()
#校验是否激活并自动激活, 第一个参数key，第二个 value
isA('yabyAbIpYEE35Im0PivPQQ==','052bb4b34cf6db508e555fd39df82dbc6b97698f6117ec627fc92463a58ae959ed9252900ffa0d6f0ed294e39d311ec25faf41440116f3983efa00fed048e2667a34fd83b050647c41539e8365c2558126a2d2be3c4fa8272a764409fab2fe42d3e8110f4b0906141fce3650a6cdabd86bc1c4a4cfdb26304087f35e8009476f7904a6c532870e8787473a30f7406073c054377a933f93f2961349f54c1751b1360359d5bd11c8b2407240d77375edbfe31dd60bbf1d0cc5492ef3174fb8b5a2d83667b29231a4dbe3f53564fc9aea22888d1d9aa8dc117408df322ce7cedbe4474560a8a10b0b7b0bf7be2d8fad75f437567506b234e191383852f118bf6defbdae115c15192877631e8a713be46cb6ddc2eff3dfb4aa586508c765806beb2040f7bb3cfd0fd9f2f3982ff62e77d122046bfa23538bda6bf6f9a9b8f39c7173d8b889dd88d7555bc2f941485737ff985bac55eec9a36d5d99eada591da97617cbdb879e67ab5c423626f970223127d15febcc9d5c2d1769bdccdf5e46e5429705c471c5a45c3f59839146af50d36c8ea2fbe2ecea876ddab582fd11d7144fe8cc58b071219606a00ec14f1df2992fdd870d8217d6d1df2e34dbf7683424e930c5ad9fc66ecfbdc92b16669c53309da1317336970e0871e1f1f763f78ede3491dd1ee1d0c55823ff143ebe319956597b6a9fb92fe8c5c7b7d4dcbf8e47e74f00fc4ebbb2c01fdacad888b2623df8bc2ba0219879f1016d88e2a055d4e40460e11c6319072516e799ff4d85c050d51d304b47973c04bde33cd2a12fa938acbd833532db559df2bf4c0b8deb1c1a88180043cff81d0b308c1881e8b94a5c7b2cd60a00e29246ea136017f7074ed0526b0c7f27f54e21a145b9589c22320f732ad23d3399370c3c1be898b5acdbbb5544d72d25e82200f72f1fb97a113f8d2f638d299d96e3bebbc1ad4021dae46a97de20082ee5eb31776b63626f448a55eb9d67aeaf17f1ea23bfb7')
print('------开始执行用例-------')
start_time = datetime.datetime.now()
print('开始时间：', start_time)
print('------开始执行api case------')
# 执行API用例并对比结果
deal_request_method()
CheckResult().deal_result()
stop_time = datetime.datetime.now()
print('结束时间：', stop_time)
print('耗时:', stop_time-start_time)
# 发送邮件
main3(host,receivers_list)













