# Django Setup Tool

## Requirements
- Python (3.6, 3.7, 3.8, 3.9, 3.10)
- Django (2.2, 3.0, 3.1, 3.2, 4.0)

Python 과 Django 의 공식적인 최신 릴리즈 버전을 사용하는 것을 권장드립니다.

## Installation
``pip`` 를 사용합니다

```text
pip install django-setup-tool
```

Example

라이브러리 INSTALLED_APP 에 등록

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    ...
    "django.contrib.staticfiles",
    
    "setup_tool",
]
```

앱 등록
```text
python manage.py prettystartapp {{ app_name }}
```