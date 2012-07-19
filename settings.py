# -*- coding: utf-8
import os
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'views')
TEMPLATE_DIRS = (TEMPLATE_DIR)
MIDDLEWARE_CLASSES = ('django.contrib.sessions.middleware.SessionMiddleware','django.middleware.locale.LocaleMiddleware','django.middleware.common.CommonMiddleware')
LANGUAGES = (('en', 'English'),('ja', '日本語'),('zh', '中文'))
