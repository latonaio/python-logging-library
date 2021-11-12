# python-logging-library  
python-logging-library は、Pythonランタイム の マイクロサービス の ログ を出力する際に、ログのjsonフォーマットを統一するためのライブラリです。  

## 動作環境
動作には以下の環境であることを前提とします。  

* OS: Linux OS  
* CPU: ARM/AMD/Intel  
* Python Runtime

## 利用方法  
本リポジトリをインストールしてください。
```sh
pip install "git+ssh://git@github.com/latonaio/python-logging-library.git@develop#egg=custom_logger"
```

各マイクロサービスのソース内に以下を配置してください。
```python
from custom_logger import init_logger
init_logger()
```