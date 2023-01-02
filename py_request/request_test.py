# 导入 requests 包
import requests

def get_request():
    payload = {'key1': 'value1', 'key2': 'value2'}
    response = requests.get('https://httpbin.org/get', params=payload)
    # 查看响应状态码
    print(response.status_code)

    # 查看响应头部字符编码
    print(response.encoding)

    # 查看完整url地址
    print(response.url)

    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print(response.text)

def post_request():
    kw = {'s': 'python 教程'}

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    response = requests.post("https://httpbin.org/post", params=kw, headers=headers)

    # 查看响应状态码
    print(response.status_code)

    # 查看响应头部字符编码
    print(response.encoding)

    # 查看完整url地址
    print(response.url)

    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print(response.text)

    print(response.json())

if __name__ == '__main__':
    post_request()