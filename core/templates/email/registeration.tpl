{% extends "mail_templated/base.tpl" %}

{% block subject %}
account activation
{% endblock %}

{% block html %}
<h1>Hello {{ user_name }}</h1>
for activating your account click on this link: http://127.0.0.1:8000/accounts/api/v1/activate/confirm/{{token}}
{% endblock %}