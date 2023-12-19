# rest-framework-tutorials

rest-framework-tutorials を実践し、学習したことを記述していく。

## 終了した tutorial

1. Serialization
2. Requests and Response

## 不具合

tutorial 通りにやるも、下記は期待とは違った。

```terminal
http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"

-- response --
{
    "detail": "JSON parse error - Expecting value: line 1 column 1 (char 0)"
}
```
