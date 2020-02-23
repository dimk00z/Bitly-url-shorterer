# Обрезка ссылок с помощью Битли

Программа для генерации коротких ссылок с помщью сервиса bitly.com, а так же для проверки количества кликов по уже созданным ссылкам.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для работы скрипта нужна регистрация на сервисе https://bit.ly/. 
Регистрируйтесь на Bitly через e-mail вместо социальных сетей. 
После регистрации на получите GENERIC ACCESS TOKEN — нужный тип токена вида 17c09e20ad155405123ac1977542fecf00231da7. 
После поучения уникального токена в папке со скриптом создайте текстовый файл .env, в который запишите следующее:
```
ACCESS_TOKEN=ВАШ_ТОКЕН
```

Для запуска в консоли:

$ python main.py http://ссылка_для_сокращения и/или bit.ly/сокращенная_ссылка 
количество ссылок для сокращения или проверки на клики не ограничено.

Пример использования:
```
python.exe .\main.py https://ya.ru/ bit.ly/39y79Qk
Your bitlink for https://ya.ru/ : http://bit.ly/38qqiUa
Total clicks for bit.ly/39y79Qk : 1
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
