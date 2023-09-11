### 如何使用开发模式，实时更新gentopia的代码
- 在项目根路径执行
```
pip install -e .
```

### 项目引入环境变量
```
# OpenAI Key
OPENAI_API_KEY=sk-r2gtKbpBT

# HTTP代理
# export https_proxy=http://127.0.0.1:23457;export http_proxy=http://127.0.0.1:23457;
ENABLE_PROXY=True
HTTP_PROXY=http://127.0.0.1:23457
HTTPS_PROXY=https://127.0.0.1:23457
```