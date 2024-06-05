# Kyiv Metro Party

This static website was created for Kyiv Metro Party in Tokyo on June 9th, 2024.

## Quest

Encrypting a secret page with staticrypt tool https://github.com/robinmoisson/staticrypt

```sh
npm -g install staticrypt --registry http://registry.yarnpkg.com

staticrypt quest.html \
  --template-title "Секретна сторінка<br>秘密のページ" \
  --template-instructions "Введіть пароль щоб побачити вміст сторінки.<br>このページのロックを解除するには、秘密のパスワードを入力してください。" \
  --template-error "Невірний пароль / パスワードが間違っています" \
  --template-placeholder "Пароль / パスワード" \
  --remember "false" \
  --template-button "OK" \
  --template-toggle-hide "Приховати пароль / パスワードを隠す" \
  --template-toggle-show "Показати пароль / パスワードを表示" \
  --short
```
