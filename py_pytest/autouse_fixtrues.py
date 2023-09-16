import pytest

@pytest.fixture(autouse=True)
def login():
    print('完成登录')
    yield
    print('退出登录')


class Test_01:
    def test_01(self):
        print('---用例01---')

    def test_02(self):
        print('---用例02---')


if __name__ == '__main__':
    pytest.main(['-vs'])