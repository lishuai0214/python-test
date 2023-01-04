import pytest


@pytest.fixture(scope="class")
def test_01():
    a = 6
    b = 7
    print("test_01:", a, b)
    return (a, b)


@pytest.fixture(scope="class")
def test_02():
    print("你是第二个执行")


@pytest.mark.usefixtures("test_02")
@pytest.mark.usefixtures("test_01")  # 优先执行
class TestNum:
    def test_03(self, test_01):
        print("test_03:", test_01)
        a = test_01[0]
        b = test_01[1]
        assert a < b
        print("断言成功")
