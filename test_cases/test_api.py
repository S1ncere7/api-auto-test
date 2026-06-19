import pytest
import requests

def test_get_posts():
    # 测试查询用户1的帖子
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}
    response = requests.get(url, params=params)
    assert response.status_code == 200, "GET请求失败"

def test_create_post():
    # 测试创建新帖子
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "test",
        "body": "test",
        "userId": 1
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201, "POST请求失败"