#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from setuptools import setup, find_packages

setup(name='scrapy-proxies-tool',
  version='0.1',
  keywords = ("Scrapy", "scrapy-proxies","proxies", "IPProxyTool"),
  description='Scrapy Proxies: random proxy middleware for Scrapy(support load proxies from IPProxyTool)',
  long_description = "base on https://github.com/aivarsk/scrapy-proxies , support  load proxies from https://github.com/qiyeboy/IPProxyPool",
  license = "MIT Licence",
  author='AnJia',
  author_email='anjia0532@gmail.com',
  url='https://github.com/anjia0532/scrapy-proxies',
  packages = find_packages(),
  include_package_data = True,
  platforms = "any"
)
