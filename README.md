# rest-framework-tutorials

rest-framework-tutorials を実践し、学習したことを記述していく。

## 終了した tutorial

1. Serialization
2. Requests and Response
3. Class-based Views
4. Authentication & Permissions
5. Relationships & Hyperlinked APIs

## tips

2. Requests and Response
   - request オブジェクト・Response オブジェクトはそれぞれ非常に万能。
   - status_code を明示的に記載することで意図しないステータスハンドリングを防ぐ。
   - api_view デコレータを利用するためには、JsonResponse ではなく、Response を利用する。
3. Class-based Views
   - 関数ベースの api_view よりもクラスベース api_view の方がコードを DRY に保つことができ、再利用性が高い。
   - 用途に応じて API_ViewClass を継承する。
     - generics.ListCreateAPIView
       - get, post メソッドを適切な形で作成してくれる。この場合、情報をリスト化することや情報を新規で作成することができる。
     - generics.RetrieveUpdateDestroyAPIView
       - get, put, delete メソッドを適切な形で作成してくれる。この場合、取得対象のデータを取得、アップデート、削除を実施することができる。
   - DRY : 重複を防ぐ考え方が含まれている。
     - 情報の重複は変更を困難にし、透明性の減少させる。
     - [DRY（wiki）](https://ja.wikipedia.org/wiki/Don%27t_repeat_yourself)
4. Authentication & Permissions
   - 認証済みのユーザーだけがアクセスできるようにできる。
   - 未認証のユーザーには読み取りのみの機能を与えることができる。
   - コンテンツを作成したオーナーユーザーにのみ更新・削除イベントの権限を付与することができる。
5. Relationships & Hyperlinked APIs
   - エントリーポイントを作成する。
   - ハイパーリンクを作成し、users, snippets へのリンクをルート api_view に作成する。

## 不具合

tutorial 通りにやるも、下記は期待とは違った。

```terminal
http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"

-- response --
{
    "detail": "JSON parse error - Expecting value: line 1 column 1 (char 0)"
}
```
