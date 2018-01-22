
import tensorflow as tf
import numpy as np
import pandas as pd
from pyt import make_y_list, get_x_list
  
# Preparing training data (inputs-outputs)  
training_inputs = tf.placeholder(shape=[None, 4], dtype=tf.float32)  
training_outputs = tf.placeholder(shape=[None, 4], dtype=tf.float32) #Desired outputs for each input  
  
""" 
Hidden layer with 12 neurons 
"""  
  
# Preparing neural network parameters (weights and bias) using TensorFlow Variables  
weights_hiddenLayer = tf.Variable(tf.truncated_normal(shape=[4,108], dtype=tf.float32))
bias_hiddenLayer = tf.Variable(tf.truncated_normal(shape=[1,108], dtype=tf.float32))  
  
# Preparing inputs of the activation function  
af_input_hiddenLayer = tf.matmul(training_inputs, weights_hiddenLayer) + bias_hiddenLayer  
  
# Activation function of the output layer neuron  
hiddenLayer_output = tf.nn.sigmoid(af_input_hiddenLayer)  
  
 
""" 
Output layer with six neuron 
"""  
  
# Preparing neural network parameters (weights and bias) using TensorFlow Variables  
weights_outputLayer = tf.Variable(tf.truncated_normal(shape=[108,4], dtype=tf.float32))  
bias_outputLayer = tf.Variable(tf.truncated_normal(shape=[1,4], dtype=tf.float32))  
  
# Preparing inputs of the activation function  
af_input_outputLayer = tf.matmul(hiddenLayer_output, weights_outputLayer) + bias_outputLayer  
  
# Activation function of the output layer neuron  
predictions = tf.nn.sigmoid(af_input_outputLayer)  
  
 
#-------------------------------------------------------------------- 
  
# Measuring the prediction error of the network after being trained  
prediction_error = -0.05 * tf.reduce_sum(tf.subtract(predictions, training_outputs) * tf.subtract(predictions, training_inputs))  
  
# Minimizing the prediction error using gradient descent optimizer  
train_op = tf.train.GradientDescentOptimizer(0.05).minimize(prediction_error)  
  
# Creating a TensorFlow Session  
sess = tf.Session()  
  
# Initializing the TensorFlow Variables (weights and bias)  
sess.run(tf.global_variables_initializer())  
# print("Hidden layer initial weights : ", sess.run(weights_hiddenLayer)) 
 
# Input from our training_sample

# Training data inputs  
training_inputs_data = get_x_list()
  
# Training data desired outputs  
training_outputs_data = make_y_list()  
  
# Training loop of the neural network  
for step in range(10): 
    trainOp, err, prediction = sess.run(fetches=[train_op, prediction_error, predictions],
                                        feed_dict={training_inputs: training_inputs_data,  
                                                   training_outputs: training_outputs_data})
    pass 
    # print(str(step), ": ", err)  

#--------------------------------------------------------------------------

# Finding out the trained weights and biased used for prediction
  
# # # Class scores of some testing data  
# print("Expected class scores : ", sess.run(predictions, feed_dict={training_inputs: training_inputs_data}))
# print("Actual class scores: ", make_y_list()) 
  
# # # Printing hidden layer weights initially generated using tf.truncated_normal()  
# print("Hidden layer final weights : ", sess.run(weights_hiddenLayer))  
  
# # # # Printing hidden layer bias initially generated using tf.truncated_normal()  
# print("Hidden layer final bias : ", sess.run(bias_hiddenLayer))  
  
# # # Printing output layer weights initially generated using tf.truncated_normal()  
# print("Output layer final weights : ", sess.run(weights_outputLayer))  
  
# # # Printing output layer bias initially generated using tf.truncated_normal()  
# print("Output layer final bias : ", sess.run(bias_outputLayer))

# # #Write a code that saves sess.run(variables and make it into a function)

#--------------------------------------------------------------------------------

# This time you use the trained weight and bias to predict the questions that is inputed in the page
# At the end, instead of using the sigmoid function, we use the softmax function to show the percentage of which node

# def softmax(af_input_outputLayer):
#     af_input_outputLayer_max = np.max(af_input_outputLayer)
#     af_input_outputLayer_exp = np.exp(af_input_outputLayer - af_input_outputLayer_max)
#     af_input_outputLayer_exp_sum = np.sum(af_input_outputLayer_exp)
#     y = af_input_outputLayer_exp / af_input_outputLayer_exp_sum

# #     return y
softmax = tf.exp(af_input_outputLayer) / tf.reduce_sum(tf.exp(af_input_outputLayer), 0)
# softmax = tf.exp(af_input_outputLayer) / tf.reduce_sum(tf.exp(af_input_outputLayer)-tf.reduce_max(af_input_outputLayer), 0)

trainOp, err, softmax_array = sess.run(fetches=[train_op, prediction_error, softmax],
                                    feed_dict={training_inputs: training_inputs_data,
                                               training_outputs: training_outputs_data})
print(softmax_array)
print(np.amax(softmax_array))
def max_column_number():
    maxima = [max(row) for row in softmax_array]  # Find the max values in each column
    m = max(maxima)                        # Find the absolute max value in the array
    for k, rowmax in enumerate(maxima):
        if rowmax == m:                    # Find which row contains the absolute max value
            col = k
            break
    return k

a = max_column_number()
print(a)
#-------------------------------------------------------------------------------- 
  
# Closing the TensorFlow Session to free resources  
sess.close()  