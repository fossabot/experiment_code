# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-07-21 10:14:59
# @Last Modified by:   jerry
# @Last Modified time: 2017-07-21 11:56:38

import datetime
from flask import url_for
from factory import db


class Post(db.Document):
    title = db.StringField(max_length=255,required=True)
    slug = db.StringField(max_length=255,required=True,unique=True)
    abstract = db.StringField()
    raw = db.StringField(required=True)
    pub_time = db.DateTimeField()
    update_time = db.DateTimeField()
    author = db.StringField(max_length=64)
    tags = db.ListField(db.StringField(max_length=30))

    def save(self,*args,**kargs):
        now = datetime.datetime.now()
        if not self.pub_time:
            self.pub_time = now

        self.update_time = now

        return super(Post,self).save(*args,**kargs)

    def to_dict(self):
        post_dict = {}
        post_dict={
            'title':self.title,
            'slug':self.slug,
            'abstract':self.abstract,
            'raw':self.raw,
            'pub_time':self.pub_time.strftime('%Y-%m-%d %H:%M:%S'),
            'update_time':self.update_time.strftime('%Y-%m-%d %H:%M:%S'),
            'author':self.author,
            'category':self.category,
            'tags':self.tags
        }

        return post_dict


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    meta = {
        'allow_inheritance':True,
        'indexex':['slug'],
        'ordering':['-pub_time']
    }

