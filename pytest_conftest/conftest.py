#!/usr/bin/env python3

import pytest
@pytest.fixture(scope="session")
def login():
    print("输入账号密码")
    yield
    print("清理数据完成")



