# -*- coding: utf-8 -*-
# @Author: Zhiwei Yang
# @Date:   2018-04-09 18:30:57
# @Last Modified by:   Zhiwei Yang
# @Last Modified time: 2018-04-09 18:31:44
# python requests发送multipart/form-data编码
from requests_toolbelt import MultipartEncoder
import requests

def get0():
    m = MultipartEncoder(
        fields={'field0': 'value', 'field1': 'value',
                'field2': ('filename', open('/Users/yang/Desktop/Screen Shot 2018-04-02 at 3.20.23 PM.png', 'rb'), 'text/plain')}
        )

    r = requests.post('http://httpbin.org/post', data=m,
                      headers={'Content-Type': m.content_type})
    print (r.status_code)

def get1():
    m = MultipartEncoder(fields={'field0': 'value', 'field1': 'value'})

    r = requests.post('http://httpbin.org/post', data=m,
                      headers={'Content-Type': m.content_type})
    print (r.status_code)