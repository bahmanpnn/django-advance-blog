{% extends "mail_templated/base.tpl" %}

{% block subject %}
account activation
{% endblock %}

{% block html %}
<h1>Hello {{ user_name }}</h1>

This is an <strong>html</strong> message.
#for using images from internet with source we should copy image address option not link!
<img src="https://img.freepik.com/free-photo/mysterious-glowing-galaxy-creates-deep-blue-backdrop-generated-by-ai_188544-9577.jpg" alt="">

for activating your account click on this link:{{token}}
{% endblock %}