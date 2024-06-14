<h4>TeamWorkSystem API  </h4> Пилотный проект personnel management system - призванный управлять распределенной команды посредством задач. С открытым исходным кодом. Pet-проект*.

<h3> Разработан с помощью Django Rest Framework </h3>

PostgreSQL

OpenAPI & SwaggerUI <br>

Версия 1.0.0 (актуальная)   –  <strong>  2 app </strong>

![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![openapi initiative](https://img.shields.io/badge/openapiinitiative-%23000000.svg?style=for-the-badge&logo=openapiinitiative&logoColor=white)


<em>Конечные точки API. Apps </em> <br>

Login (вход) + получение токина. Базовая аутентификация  <br>
<code> POST api/v1/login/ </code>  <br>
Logout<br>
<code> POST api/v1/logout/ </code> <br>
Logout All<br>
<code> POST /api/v1/logoutall/ </code> <br>

<h4>Staff</h4>

Доска из “карточек” сотрудников и профиль работника (сотрудника).<br>
Profile Api List - Список (лист) сотрудников компании<br>
<code> GET /api/v1/profile/ </code> <br>

Profile Api Instance - Cтраница сотрутдинка<br>
<code> GET /api/v1/profile/<strong>pk</strong>/ </code><br>
*где <strong>pk</strong> это "id" сотрутдинка <br>

Current  - Профиль (личная страница сотрудника)<br>
<code> GET, PUT, PATCH, /api/v1/profile/current/ </code> <br>

Departament Api - Структура компании (список департаментов с участниками)<br>
<code> GET /api/v1/company/ </code> <br>

Для облегчения нагрузки на фронтент созданы profile-short.<br>
Другая пагинация и кол-во полей.<br>

Profile Short Api List - Список (лист) сотрудников компании <br>
<code> GET api/v1/profile-short/ </code> <br>
Profile Short Api Instance - Краткие данные о конкретном сотруднике<br>
<code> GET /api/v1/profile-short/<strong>pk</strong>/ </code> <br>
*где <strong>pk</strong> это "id" сотрутдинка <br>

<h4>News</h4>
Полноценная новостная лента (общекорпоративный блог) <br>

News List - Список новостей компании с возможностью добавление новости <br>
<code> GET, POST, /api/v1/news/<br> </code>

News Instance - Страница новости<br>
<code> GET, PUT, PATCH, DELETE /api/v1/news/<strong>news_pk</strong>/ </code>  <br> 
*где <strong>news_pk</strong> это "id" новости <br>
PUT, PATCH, DELETE - права только у автора новости<br>

Comments List - Комментарии к новости<br>
<code> GET, POST /api/v1/news/<strong>news_pk</strong>/comments/ </code> <br>
*где <strong>news_pk</strong> это "id" новости <br>

Comments Instance - комментарий (для редактирования и удаления)<br>
<code> GET, PUT, PATCH, DELETE /api/v1/news/<strong>news_pk</strong>/comments/<strong>pk</strong>/ </code> <br>
*где <strong>news_pk</strong> это "id" новости, где <strong>pk</strong> это "id" комментария <br>
PUT, PATCH, DELETE - права только у автора комментария<br>


<em>Проект создан не по шаблону или туториалу (курсам). Полностью кастовый проект. 
Сбор требования осуществлял исходя из опыта  5 лет администрирования
и внедрения Битрик24 в компании различной направленности.
Выявил наиболее понятные  - пользовательские истории. </em> <br>
<br>

<strong> Версия 1.0.1  </strong> — находиться в разработке

Кастовый Middleware - Django Middleware <br>
Celery + Redis<br>

![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)

Messenger - полноценный внутри корпоративный менеджер <br>
Tasks - менеджер задач<br>

<strong> Версия 1.0.2  </strong> — в перспективе

Calendar - календарь для планирования встречи и иных мероприятий<br>
Dashboard -  кастомная BI система <br>

<br>

<h5> По всем вопросам </h5>
https://t.me/ostrovsky_I <br>
ivan.only.art@gmail.com <br>
Инфо блог основного проекта <br>
https://ost.pythonanywhere.com/pro/<br>
Персональный сайт разработчика<br>
https://ost.pythonanywhere.com/<br>

<br>
<br>
<br>
<em> *данный Pet-проект являеться учебной разработкой и предоставляется «как есть», разработчик не несет ответственности за его использованеие.</em>
