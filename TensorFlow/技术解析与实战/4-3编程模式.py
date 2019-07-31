import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
with tf.Session() as sess1:
  # 指定在第二个gpu上运行
  matrix1 = tf.constant([[3., 3.]])
  matrix2 = tf.constant([[2.],[2.]])
  product = tf.matmul(matrix1, matrix2)
  print(sess1.run(product))

sess = tf.Session()
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)
print(sess.run([output], feed_dict={input1: [7.0], input2: [2.0]}))–
