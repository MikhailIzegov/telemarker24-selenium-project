## Проект UI-автотестов для telemarket24 (WEB)
<!-- Технологии -->

## :gear: Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>
  <code><img width="5%" title="Python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
  <code><img width="5%" title="Pytest" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

## 📹: Видео-прогон

<p align="center">
  <img title="Video" src="images/videos/telemarket24_smoke_video.gif">
</p>

## :open_book: Описание
В проекте представлен один **высокоуровневый** смоук-тест всего бизнес-пути, написанный на Python + Selenium с применением модели PageObject.  
  
По факту этот высокоуровневый тест может быть разбит на **множество низкоуровневых**, ведь частью общего "смоука" являются отдельные смысловые блоки такие как:  
- [x] Авторизация пользователя
- [x] Работа с товаром: добавление в коризину, сохранение и проверка названия и цены в разных частях UI
- [x] Работа фильтров
- [x] Отдельные тесты каждой из страниц/модулей (модуль авторизации, главная страница, страница с выбором товара, страница корзины, модуль корзины в хэдэре)
  
UI-тест на сайте `telemarket24.ru`  
  
Точка `A`: главная страница сайта 
  
Точка `B`: страница корзины, сверка товара, очистка корзины и куков как постусловие
  
Подключена система отчетности Allure Reports с вложениями (логи, скриншоты, видео и пр.)   
  
Шаги отображены в виде степов через `with allure.step`  
  
Также по факту прохождения теста отправляется уведомление с результатами в Telegram.  
  
Браузер в UI-тестах запускается удаленно в Selenoid.  

## :heavy_check_mark: Кратко
- [x] `UI` тесты
- [x] Запуск WEB тестов, используя `Jenkins` и `Selenoid`
- [x] `Allure Reports` с вложениями (логи, скриншоты, видео)
- [x] Отправка результатов тестирования в `Telegram`

<!-- Тест кейсы -->

## :heavy_check_mark: Что проверяют WEB тесты?
- [x] Работа на главной странице - переход к модулю авторизации, открытие вкладок
- [x] Авторизация
- [x] Переход в раздел смартфонов Apple
- [x] Применение фильтров: выбор товара
- [x] Проверка соответствия названия товара и цены
- [x] Проверка итоговой цены, переход на страницу корзины
- [x] Итоговый чекаут на странице корзины
- [x] Чистка корзины

<!-- Jenkins -->

## <img width="5%" title="Jenkins" src="images/logo/jenkins.png"> Запуск тестов из Jenkins

Для запуска тестов из Jenkins:
Нажмите кнопку "Build"

<p><img src="images/screenshots/Jenkins_build.png" alt="Jenkins"/></p>

<!-- Отчеты -->

## :bar_chart: Отчеты о прохождении тестов доступны в Allure

> При локальном запуске введите в командной строке: 
```bash
allure serve 
```

### <img width="3%" title="Allure" src="images/logo/allure_report.png"> Allure

#### Примеры отображения тестов

<img src="images/screenshots/Allure-1.png" alt="Allure"/>

#### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.

<img src="images/screenshots/Allure_graphs.png" alt="Allure"/>

### <img width="2.5%" title="Telegram" src="images/logo/tg.png"> Telegram

Настроена отправка отчета в Telegram

<img src="images/screenshots/Telegram_notifications.png" alt="Telegram"/>
