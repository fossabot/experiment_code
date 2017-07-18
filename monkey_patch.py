# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-07-18 14:08:38
# @Last Modified by:   jerry
# @Last Modified time: 2017-07-18 14:19:05

import json
def get_info(self, *args):
    return "Test data"

json.get_info = get_info
print json.get_info("xx")
