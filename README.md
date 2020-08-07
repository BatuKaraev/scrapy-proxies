Random proxy middleware for Scrapy (http://scrapy.org/)
=======================================================

**base on https://github.com/aivarsk/scrapy-proxies , support  load proxies from https://github.com/qiyeboy/IPProxyPool**

Processes Scrapy requests using a random proxy from list to avoid IP ban and
improve crawling speed.

Get your proxy list from sites like http://www.hidemyass.com/ (copy-paste into text file
and reformat to http://host:port format)

Install
--------

The quick way:

```bash
pip install scrapy-proxies-tool
```

Or checkout the source and run

```bash
python setup.py install
```

settings.py
-----------

```python

# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
# Retry if get timeout
RETRY_PROXY_CHANGE = 2


DOWNLOADER_MIDDLEWARES = {
  'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
  'scrapy_proxies.RandomProxy': 100,
  'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

PROXY_SETTINGS = {
  # Proxy list containing entries like
  # http://host1:port
  # http://username:password@host2:port
  # http://host3:port
  # ...
  # if PROXY_SETTINGS[from_proxies_server] = True , proxy_list is server address (ref https://github.com/qiyeboy/IPProxyPool and https://github.com/awolfly9/IPProxyTool )
  # Only support http(ref https://github.com/qiyeboy/IPProxyPool#%E5%8F%82%E6%95%B0)
  # list : ['http://localhost:8000?protocol=0'],
  'list':['/path/to/proxy/list.txt'],

  # disable proxy settings and  use real ip when all proxies are unusable
  'use_real_when_empty':False,
  'from_proxies_server':False,

  # If proxy mode is 2 uncomment this sentence :
  # 'custom_proxy': "http://host1:port",

  # Proxy mode
  # 0 = Every requests have different proxy
  # 1 = Take only one proxy from the list and assign it to every requests
  # 2 = Put a custom proxy to use in the settings
  'mode':0
}
```

For older versions of Scrapy (before 1.0.0) you have to use
`scrapy.contrib.downloadermiddleware.retry.RetryMiddleware` and
`scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware`
middlewares instead.


Your spider
-----------

In each callback ensure that proxy /really/ returned your target page by
checking for site logo or some other significant element.
If not - retry request with dont_filter=True

```python
  if not hxs.select('//get/site/logo'):
    yield Request(url=response.url, dont_filter=True)
```
