# Hello World Tensorflow

import tensorflow as tf

# Criando um tensor. uma constante no tensorflow
hello = tf.constant('Hello World!')

with tf.Session() as sess:
    # inicializa a sessão.
    output = sess.run(hello)
    print(output)