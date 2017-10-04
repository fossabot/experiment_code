# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-04 16:22:02
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-04 16:24:38


# test success under python3.6

import urllib
from unittest.mock import patch, mock_open
def send_req(url):
    with urllib.request.urlopen(url) as f:
        if f.status == 200:
            return f.read()
        raise urllib.error.URLError
fake_html = b'<html><h1>Mock Content</h1></html>'
mock_urlopen = mock_open(read_data=fake_html)
ret = mock_urlopen.return_value
ret.status = 200
@patch('urllib.request.urlopen', mock_urlopen)
def test_send_req_success():
    try:
        ret = send_req('http://www.mockurl.com')
        assert ret == fake_html
    except Exception as e:
        print(e)
    else:
        print('test send_req success')


test_send_req_success()

ret = mock_urlopen.return_value
ret.status = 404

@patch('urllib.request.urlopen', mock_urlopen)
def test_send_req_fail():
    try:
        ret = send_req('http://www.mockurl.com')
        assert ret == fake_html
    except Exception as e:
        print('test fail success')

test_send_req_fail()
