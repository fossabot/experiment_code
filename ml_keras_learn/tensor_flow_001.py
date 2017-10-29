#coding: utf-8
import tensorflow as tf
import numpy as np

def tensor_flow_001():
    graph = tf.get_default_graph()
    # print graph.get_operations()

    input_value = tf.constant(1.0)
    print input_value
    weight = tf.Variable(0.8)
    output_value = weight * input_value
    operations = graph.get_operations()
    for _op in operations:
        print _op
    print operations[0].node_def
    init = tf.global_variables_initializer()

    sess = tf.Session()
    print sess.run(init)
    print "\n"
    print sess.run(input_value)
    op = graph.get_operations()[-1]
    print op
    print sess.run(output_value)

def get_the_plot():
    sess = tf.Session()
    x = tf.constant(1.0, name='input')
    w = tf.Variable(0.8, name='weight')
    y = tf.mul(w,x, name='ouput')
    summary_writer = tf.summary.FileWriter('log_simple_graph',sess.graph)
    y_ = tf.constant(0.0)
    loss = (y-y_)**2

    optim = tf.train.GradientDescentOptimizer(learning_rate=0.025)

    grads_and_vars = optim.compute_gradients(loss)
    sess.run(tf.global_variables_initializer())
    print sess.run(grads_and_vars[0][0])

    sess.run(optim.apply_gradients(grads_and_vars))
    print sess.run(w)
    train_step = tf.train.GradientDescentOptimizer(0.025).minimize(loss)

    for i in range(100):
        print "before setp {}, y is {}".format(i,sess.run(y))
        sess.run(train_step)

    print sess.run(y)

    summary_y = tf.scalar_summary('output',y)
    summary_writer = tf.summary.FileWriter('log_simple_stats')
    sess.run(tf.global_variables_initializer)
    for i in range(100):
        summary_str = sess.run(summary_y)
        summary_writer.add_summary(summary_str,i)
        sess.run(train_step)

def tf_learn_final_version():
    optimize_params = 0.025
    x = tf.constant(1.0,name='input')
    w = tf.Variable(0.8,name='weight')
    y = tf.mul(w,x,name='output')
    y_ = tf.constant(0.0,name='correct_value')
    loss = tf.pow(y-y_,2,name='loss')
    train_step = tf.train.GradientDescentOptimizer(optimize_params).minimize(loss)

    for value in [x,w,y,y_,loss]:
        tf.summary.scalar(value.op.name,value)


    summaries = tf.summary.merge_all()

    sess = tf.Session()
    summary_writer = tf.summary.FileWriter('log_simple_stats',sess.graph)

    sess.run(tf.global_variables_initializer())
    for i in range(100):
        print "before setp {}, y is {}".format(i,sess.run(y))
        summary_writer.add_summary(sess.run(summaries),i)
        sess.run(train_step)

def get_tensor_started():
    node1 = tf.constant(3.0,tf.float32)
    node2 = tf.constant(4.0)
    print node1,node2
    node3 = tf.add(node1,node2,name='add')
    print node3
    with  tf.Session() as sess:
        print sess.run([node1,node2])
        print "sess.run(node3): ", sess.run(node3)

        a = tf.placeholder(tf.float32)
        b = tf.placeholder(tf.float32)

        adder_node = a + b  # tf.add(a,b)

        print  sess.run(adder_node,{a:3,b:4.5})
        print sess.run(adder_node,{a:[1,3],b:[2,4]})

        add_and_triple = adder_node * 3
        print sess.run(add_and_triple,{a:3,b:4.5})

def tensor_variable():
    """
    We guessed the "perfect" values of W and b, but the whole point of machine learning is to find the correct model parameters automatically. We will show how to accomplish this in the next section.
    """

    W = tf.Variable([0.0],tf.float32)
    b = tf.Variable([0.0],tf.float32)
    x = tf.placeholder(tf.float32)

    linear_model = W * x + b

    y = tf.placeholder(tf.float32)
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        print sess.run(linear_model,{x:[1,2,3,4]})

        y  = tf.placeholder(tf.float32)
        squared_deltas = tf.square(linear_model - y)
        # squared_deltas = tf.square([(0.3*1+(-0.3) - 1),(0.3*2+(-0.3) - 2),(0.3*3+(-0.3) - 3),(0.3*4+(-0.3) - 4)])
        # squared_deltas =  tf.square([-1,-1.7,-2.4,-3.1])
        # 平方后 squared_deltas = [1+2.88+ 5.76 + 9.61]
        loss = tf.reduce_sum(squared_deltas)
        # reduce_sum([1+2.88+ 5.76 + 9.61]) = 19.26
        print sess.run(loss,{x:[1,2,3,4], y:[1,2,3,4]})

        optimizer = tf.train.GradientDescentOptimizer(0.01)
        train = optimizer.minimize(loss)

        sess.run(init)
        for i in range(1000):
            print i, sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})

        print sess.run([W,b])


def learn_tf_train_api():
    """
    The completed trainable linear regression model is shown here:
    """
    # Model Parameters
    W = tf.Variable([.3],tf.float32)
    b = tf.Variable([-.3],tf.float32)

    # Model input and output
    x = tf.placeholder(tf.float32)
    linear_model = W * x + b
    y = tf.placeholder(tf.float32)

    # loss
    loss = tf.reduce_sum(tf.square(linear_model - y))

    # optimizer
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(loss)

    # training data
    x_train = [1,2,3,4]
    y_train = [0,-1,-2,-3]
    train_data = {x:x_train,y:y_train}
    #trainging loop
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        # summary_writer = tf.summary.FileWriter('log_simple_stats_001')
        # summary_y = tf.summary.scalar('output',linear_model)
        # summary_str =sess.run(summary_y)
        sess.run(init)    ## reset values to incorrect defaults.
        for i in range(1000):
            # summary_writer.add_summary(summary_str,i)
            sess.run(train,train_data)
        #evaluate training accuracy
        curr_W, curr_b, curr_loss = sess.run([W, b, loss], train_data)
        print "W: %s b: %s loss: %s" % (curr_W, curr_b, curr_loss)



def tf_contrib_learn():
    '''
    tf.contrib.learn is a high-level TensorFlow library that simplifies the mechanics of machine learning, including the following:
            running training loops
            running evaluation loops
            managing data sets
            managing feeding
            tf.contrib.learn defines many common models.

            Basic usage

            Notice how much simpler the linear regression program becomes with tf.contrib.learn:
    '''



    # Declare list of features. We only have one real-valued feature. There are many
    # other types of columns that are more complicated and useful.
    features = [ tf.contrib.layers.real_valued_column("x",dimension=1)]

    # An estimator is the front end to invoke training (fitting) and evaluation
    # (inference). There are many predefined types like linear regression,
    # logistic regression, linear classification, logistic classification, and
    # many neural network classifiers and regressors. The following code
    # provides an estimator that does linear regression.

    estimater =tf.contrib.learn.LinearRegressor(feature_columns=features)

    # TensorFlow provides many helper methods to read and set up data sets.
    # Here we use `numpy_input_fn`. We have to tell the function how many batches
    # of data (num_epochs) we want and how big each batch should be.

    x = np.array([1.,2.,3.,4.])
    y = np.array([0.,-1.,-2.,-3.])

    input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x}, y, batch_size=4, num_epochs=1000)

    # We can invoke 1000 training steps by invoking the `fit` method and passing the
    # training data set.
    estimater.fit(input_fn=input_fn,steps=1000)

    # Here we evaluate how well our model did. In a real example, we would want
    # to use a separate validation and testing data set to avoid overfitting.
    estimater.evaluate(input_fn=input_fn)


if __name__ == '__main__':
    learn_tf_train_api()
