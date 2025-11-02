# Kyiv Metro Party

This static website was created for Kyiv Metro Party in Tokyo on June 9th, 2024.

## Quest

Encrypting a secret page with staticrypt tool https://github.com/robinmoisson/staticrypt

```sh
npm -g install staticrypt

staticrypt quest.html \
  --template-title "Таємна сторінка<br>秘密のページ" \
  --template-instructions "Введіть секретний код щоб побачити вміст сторінки.<br>このページのロックを解除するには、秘密のコードを入力してください。" \
  --template-error "Невірний код / コードが間違っています" \
  --template-placeholder "Код / コード" \
  --remember "false" \
  --template-button "OK" \
  --template-toggle-hide "Приховати код / コードを隠す" \
  --template-toggle-show "Показати код / コードを表示" \
  --short
```
