import pandas as pd
import math
from random import random, seed

network = list()
eta = 0.5 #learning rate
inputs = [0.05, 0.1]
target_output = [0.01, 0.99]
classes = []

def initialize_network(n_inputs, n_hiddens, n_outputs):
	seed(1)
	for k in range(len(n_hiddens)):
		hidden_bias = random()
		if(k == 0):
			hidden_layer = [{'id':j, 'weights':[random() for i in range(n_inputs)], 'bias':hidden_bias, 'output':0, 'net':0, 'inputs':[]} for j in range(n_hiddens[k])]
		else:
			hidden_layer = [{'id':j, 'weights':[random() for i in range(n_hiddens[k-1])], 'bias':hidden_bias, 'output':0, 'net':0, 'inputs':[]} for j in range(n_hiddens[k])]
		network.append(hidden_layer)
	output_bias = random()
	output_layer = [{'id':j, 'weights':[random() for i in range(n_hiddens[-1])], 'bias':output_bias, 'output':0, 'net':0, 'inputs':[]} for j in range(n_outputs)]
	network.append(output_layer)
#	hidden_bias = 0.35
#	hidden_layer = []
#	hidden_layer.append({'id':1, 'weights':[0.15, 0.2], 'bias':hidden_bias, 'output':0, 'net':0, 'inputs':[]})
#	hidden_layer.append({'id':2, 'weights':[0.25, 0.3], 'bias':hidden_bias, 'output':0, 'net':0, 'inputs':[]})
#	network.append(hidden_layer)
#	output_layer = []
#	output_bias = 0.6
#	output_layer.append({'id':1, 'weights':[0.4, 0.45], 'bias':output_bias, 'output':0, 'net':0, 'inputs':[]})
#	output_layer.append({'id':2, 'weights':[0.5, 0.55], 'bias':output_bias, 'output':0, 'net':0, 'inputs':[]})
#	network.append(output_layer)
	
	

def weighted_sum(weights, bias, inputs):
	net = bias
#	print("Net:{}".format(net))
#	print(weights)
#	print(inputs)
#	print()
	for i in range(len(weights)):
		net += weights[i] * inputs[i]
#		print("Net:{}".format(net))
	return net

def activate(net):
	return 1.0/(1.0 + math.exp(-net))

def forward_propogate(network, inputs):
	theInputs = inputs
	for layer in network:
		new_inputs = []
		for node in layer:
			node['inputs'] = theInputs
			node['net'] = weighted_sum(node['weights'], node['bias'], theInputs)
#			print("node[Net]:{}".format(node['net']))
			node['output'] = activate(node['net'])
			new_inputs.append(node['output'])
		theInputs = new_inputs
	return theInputs
	
def activation_derivative(value):
	return value * (1.0 - value)

def backward_propogate_error(network, target_output):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if (i != len(network)-1):
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i+1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(target_output[j] - neuron['output'])
		
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * activation_derivative(neuron['output'])

def update_weights(network, inputs, eta):
	for layer in network:
		for neuron in layer:
			for j in range(len(neuron['weights'])):
				neuron['weights'][j] += eta * neuron['delta'] * neuron['inputs'][j]
			neuron['bias'] += eta * neuron['delta']
			
def train_network(network, inputs, eta, n_epoch, n_outputs):
	classes = list(set(inputs[:,-1]))
	# print("Classes: {}".format(classes))
	for epoch in range(n_epoch):
		sum_error = 0.0
		for row in inputs:
			target_output = [0 for i in range(n_outputs)]
			target_output[classes.index(row[-1])] = 1
			# if (row[-1] == 1):
			# 	target_output[0] = 0.99
			# 	target_output[1] = 0.01
			# if (row[-1] == -1):
			# 	target_output[0] = 0.01
			# 	target_output[1] = 0.99
			row = row[:-1]
			outputs = forward_propogate(network, row)
			sum_error += sum([(target_output[i] - outputs[i]) ** 2 for i in range(len(outputs))])
			backward_propogate_error(network, target_output)
			update_weights(network, row, eta)
		#print('epoch=%d, error=%.3f' %(epoch, sum_error) )

def test_output(network, inputs):
	outputs = forward_propogate(network, inputs)
	max_output = 0
	for i, val in enumerate(outputs):
		if(val > max_output):
			result = classes[i]
			max_output = val
	print("The suggested class is: {} with a probability of {}%".format (result, max_output*100.0))


initialize_network(4,[4],3)
#for layer in network:
#	for node in layer:
#		print(node)
#	print()
	
#output = forward_propogate(network, inputs)
#print(output)

#backward_propogate_error(network, target_output)
#update_weights(network, inputs, eta)
#for layer in network:
#	for node in layer:
#		print(node)
#	print()
data = pd.read_csv('iris.csv', header=None)
classes = list(set(data.values[:,-1]))

train_network(network, data.values, eta, 100, 3)
print('\n\n')

#for layer in network:
#	for node in layer:
#		print(node)
#	print()

inputs = [5.1, 2.5, 3.0, 1.1] #answer: Iris-versicolor
test_output(network, inputs)






#mat = data[['col1','col2']]
