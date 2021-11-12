# golang-logging-library

golang-logging-library は Go ランタイム の マイクロサービス の ログ を出力する際に、ログの json フォーマットを統一するためのライブラリです。

## 動作環境

動作には以下の環境であることを前提とします。

* OS: Linux OS    
* CPU: ARM/AMD/Intel   
* Golang Runtime

## 利用方法

#### 本リポジトリを2通りの方法のいずれかでインストールしてください。

【インストール方法①】  
go getでインストールしてください。  

```sh
go get v0.0.0 github.com/latonaio/golang-logging-library/logger
```

【インストール方法②】  
各マイクロサービスのgo.modに以下のように定義してから、go mod downloadでインストールしてください。  

```
module github.com/latonaio/golang-logging-library

go 1.17

require (
	github.com/latonaio/golang-logging-library v0.0.0
)
```

```
go mod download   #全てインストールする場合
go mod download github.com/latonaio/golang-logging-library v0.0.0   #一部のみインストールする場合
```

#### 各マイクロサービスのソース内に以下を配置してください。

```go
import "github.com/latonaio/golang-logging-library/logger"
```

#### インスタンスの作成は下記のように実行します。

```go
l := logger.NewLogger()
```

#### 出力の形式

- log.Fatal(msg) 
- log.Error(msg)
- log.Warn (msg)
- log.Info (msg)
- log.Debug(msg)
 
#### パラメーター

- msg: interface型、文字列で渡した場合とJSONにマッピングできるmapや構造体の形式で渡した場合で挙動が異なります。

#### ログ出力例は以下の通りです。

```go
// 引数に文字列を渡した場合
logging.Debug("This is Test")
{"cursor":"/Users/xxx/test/test.go#L35","level":"DEBUG","message":"This is Test","time":"2021-11-05T18:33:49.495918+09:00"}

// 引数を文字列に渡した場合、フォーマット指定することも可能です
var A = "test"
var B = 111
logging.Debug("%v %v", A, B)
{"cursor":"/Users/xxx/test/test.go#L36","level":"DEBUG","message":"test 111","time":"2021-11-05T18:33:49.496388+09:00"}

// JSONにマッピング可能なマップを渡した場合
var testJson1 = map[string]interface{}{
    "message": "debug",
    "params": []string{
        "nested", "world",
    },
}
logging.Debug(testJson1)
{"cursor":"/Users/xxx/test/test.go#L39","level":"DEBUG","message":"debug","params":["nested","world"],"time":"2021-11-05T18:33:49.496445+09:00"}

// JSONにマッピング可能な構造体を渡した場合
type testStruct struct {
	This string `json:"message"`
	Is   string `json:"is"`
	Test int    `json:"test"`
}

var testJson2 = testStruct{
    "hello", "world", 100,
}
logging.Debug(testJson2)
{"cursor":"/Users/xxx/test/test.go#L40","is":"world","level":"DEBUG","message":"hello","test":100,"time":"2021-11-05T18:33:49.496519+09:00"}

```
