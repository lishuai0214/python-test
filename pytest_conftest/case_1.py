import pytest
class TestLogin1():
    def test_1(self, login):
        print("用例1")

    def test_2(self):
        print("用例2")

    def test_3(self, login):
        print("用例3")

if __name__ == '__main__':
    pytest.main()