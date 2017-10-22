# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-07-30 13:53:05
# @Last Modified by:   jerry
# @Last Modified time: 2017-08-25 18:12:58

from __future__ import print_function

import tensorflow.examples.tutorials.mnist.input_data as input_data
import tensorflow as tf

mnist = input_data.read_data_sets("./MNIST_data/", one_hot=False)
print("Training data size:",mnist.train.num_examples)

print(mnist.train.images.shape,mnist.train.labels.shape)
print(mnist.test.images.shape,mnist.test.labels.shape)
print(mnist.validation.images.shape,mnist.validation.labels.shape)

sess = tf.InteractiveSession()
x = tf.placeholder(tf.float32, [None, 784])
w = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

# y = softmax(Wx + b)
y = tf.nn.softmax(tf.matmul(x,w) + b )

y_ = tf.placeholder(tf.float32, [None,10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),
    reduction_indices = [1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

tf.global_variables_initializer().run()


for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    train_step.run({x: batch_xs,y_: batch_ys})

correct_preditcion = tf.equal(tf.argmax(y, 1),tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_preditcion, tf.float32))

print(accuracy.eval({x: mnist.test.images, y_:mnist.test.labels}))



