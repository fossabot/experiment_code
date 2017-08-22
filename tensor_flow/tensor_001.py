# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-07-30 13:53:05
# @Last Modified by:   jerry
# @Last Modified time: 2017-07-30 14:13:22

import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)
print "Training data size:",mnist.train.num_examples

