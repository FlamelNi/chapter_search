import tensorflow as tf
import numpy  
  
# Preparing training data (inputs-outputs)  
training_inputs = tf.placeholder(shape=[None, ], dtype=tf.float32)  
training_outputs = tf.placeholder(shape=[None, 6], dtype=tf.float32) #Desired outputs for each input  
  
""" 
Hidden layer with 12 neurons 
"""  
  
# Preparing neural network parameters (weights and bias) using TensorFlow Variables  
weights_hiddenLayer = tf.Variable(tf.truncated_normal(shape=[,12], dtype=tf.float32))  
bias_hiddenLayer = tf.Variable(tf.truncated_normal(shape=[1,12], dtype=tf.float32))  
  
# Preparing inputs of the activation function  
af_input_hiddenLayer = tf.matmul(training_inputs, weights_hiddenLayer) + bias_hiddenLayer  
  
# Activation function of the output layer neuron  
hiddenLayer_output = tf.nn.sigmoid(af_input_hiddenLayer)  
  
 
""" 
Output layer with six neuron 
"""  
  
# Preparing neural network parameters (weights and bias) using TensorFlow Variables  
weights_outputLayer = tf.Variable(tf.truncated_normal(shape=[12,6], dtype=tf.float32))  
bias_outputLayer = tf.Variable(tf.truncated_normal(shape=[1,6], dtype=tf.float32))  
  
# Preparing inputs of the activation function  
af_input_outputLayer = tf.matmul(hiddenLayer_output, weights_outputLayer) + bias_outputLayer  
  
# Activation function of the output layer neuron  
predictions = tf.nn.sigmoid(af_input_outputLayer)  
  
 
#-------------------------------------------------------------------- 
  
# Measuring the prediction error of the network after being trained  
prediction_error = 0.5 * tf.reduce_sum(tf.subtract(predictions, training_outputs) * tf.subtract(predictions, training_inputs))  
  
# Minimizing the prediction error using gradient descent optimizer  
train_op = tf.train.GradientDescentOptimizer(0.05).minimize(prediction_error)  
  
# Creating a TensorFlow Session  
sess = tf.Session()  
  
# Initializing the TensorFlow Variables (weights and bias)  
sess.run(tf.global_variables_initializer())  
 
# Input from our training_sample

# Training data inputs  
training_inputs_data = []
  
# Training data desired outputs  
training_outputs_data = []  
  
# Training loop of the neural network  
for step in range(1000): 
    trainOp, err, prediction = sess.run(fetches=[train_op, prediction_error, predictions],
                          feed_dict={training_inputs: training_inputs_data,  
                                     training_outputs: training_outputs_data})  
#    print(str(step), ": ", err)  

#--------------------------------------------------------------------------

# Finding out the trained weights and biased used for prediction
  
# Class scores of some testing data  
#print("Expected class scores : ", sess.run(predictions, feed_dict={training_inputs: training_inputs_data}))  
  
# Printing hidden layer weights initially generated using tf.truncated_normal()  
#print("Hidden layer initial weights : ", sess.run(weights_hidden))  
  
# Printing hidden layer bias initially generated using tf.truncated_normal()  
#print("Hidden layer initial bias : ", sess.run(bias_hidden))  
  
# Printing output layer weights initially generated using tf.truncated_normal()  
#print("Output layer initial weights : ", sess.run(weights_output))  
  
# Printing output layer bias initially generated using tf.truncated_normal()  
#print("Output layer initial bias : ", sess.run(bias_output))

#Write a code that saves sess.run(variables and make it into a function)

#--------------------------------------------------------------------------------

# This time you use the trained weight and bias to predict the questions that is inputed in the page
# At the end, instead of using the sigmoid function, we use the softmax function to show the percentage of which node

def softmax(af_input_outputLayer):
    af_input_outputLayer_max = np.max(af_input_outputLayer)
    af_input_outputLayer_exp = np.exp(af_input_outputLayer - af_input_outputLayer_max)
    af_input_outputLayer_exp_sum = np.sum(af_input_outputLayer_exp)
    y = af_input_outputLayer_exp / af_input_outputLayer_exp_sum

    return y

# percentage_array = softmax(af_input_outputLayer)
# print(np.max(percentage_array))


#-------------------------------------------------------------------------------- 
  
# Closing the TensorFlow Session to free resources  
sess.close()  