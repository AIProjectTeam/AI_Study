import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
with tf.variable_scope('                                                                                                                                                                                                                                                                                                                                                                                                                                          foo') as scope:
  v = tf.get_variable("v", [1])
with tf.variable_scope('foo', reuse=True):
  # 也可以写成：
  # scope.reuse_variables();
  v1 = tf.get_variable("v", [1])
print(v.name);

with tf.variable_scope('foo1') as foo1_scope:
  v = tf.get_variable('v', [1])
with tf.variable_scope(foo1_scope):
  v1 = tf.get_variable('w', [1])
print(v.name);
print(v1.name);
