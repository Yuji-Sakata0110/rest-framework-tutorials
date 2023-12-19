# rest-framework-tutorials

rest-framework-tutorials を実践し、学習したことを記述していく。

## 終了した tutorial

1. Serialization
2. Requests and Response

## tips

2. Requests and Response
   - request オブジェクト・Response オブジェクトはそれぞれ非常に万能
   - status_code を明示的に記載することで意図しないステータスハンドリングを防ぐ
   - api_view デコレータを利用するためには、JsonResponse ではなく、Response を利用する。

## 不具合

tutorial 通りにやるも、下記は期待とは違った。

```terminal
http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"

-- response --
{
    "detail": "JSON parse error - Expecting value: line 1 column 1 (char 0)"
}
```
