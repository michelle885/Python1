# pytest会先从当前路径下找conftest.py文件，如果有，就先加载
# 引入pytest类
import pytest

# 复写pytest源码里收集测试用例的方法
def pytest_collection_modifyitems(session, config, items:list):
    # for循环每一个收集到的测试用例
    for item in items:
        # nodeid是item的一个属性，打印测试用例
        print(item.nodeid)
        # 如果测试用例有‘add’, 就自动添加add标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        # 如果测试用例有‘sub’, 就自动添加sub标签
        if 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        # 如果测试用例有‘mul’, 就自动添加mul标签
        if 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
        # 如果测试用例有‘div’, 就自动添加div标签
        if 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
        # 如果测试用例有‘mix’, 就自动添加mix标签
        if 'mix' in item.nodeid:
            item.add_marker(pytest.mark.mix)

