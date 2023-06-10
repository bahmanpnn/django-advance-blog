{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user_name }}
{% endblock %}

{% block html %}
This is an <strong>html</strong> message.
#for using images from internet with source we should copy image address option not link!
<img src="https://img.freepik.com/free-photo/mysterious-glowing-galaxy-creates-deep-blue-backdrop-generated-by-ai_188544-9577.jpg" alt="">
{% endblock %}