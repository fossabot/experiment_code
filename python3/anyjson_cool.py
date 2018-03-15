# -*- coding:utf-8 -*-
# date:2018-03-15 16:42
# auther:yang
import  anyjson
d = {
  "array": [
    1,
    2,
    3
  ],
  "boolean": True,
  "null": "null",
  "number": 123,
  "object": {
    "a": "b",
    "c": "d",
    "e": "f"
  },
  "string": "Hello World"
}
b = anyjson.serialize(d)
print (b)