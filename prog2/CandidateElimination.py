import csv
import numpy as np
import pandas as pd

def predict(data, model):
	flag = True
	for i, ele in enumerate(model):
		if ele != "?" and ele != data[i]:
			flag = False
			break 
	return flag

def train():
	S = ["", "", "", "", "", ""]
	G = [["?", "?", "?", "?", "?", "?"]]
	print("S0: " + str(S))
	print("G0: " + str(G) + "\n")
	
	with open("prog2_data.csv") as csv_file:
		data = csv.reader(csv_file, delimiter = ',')		
		for i, row in enumerate(data): 
			# positive example
			if row[6] == "Yes":
				
				# update S
				for j, col in enumerate(row[:6]):
					if S[j] == "":
						S[j] = col
					elif col != S[j]:
						S[j] = "?"
				
				# eliminate from G
				n = len(G)
				m = 0
				while m<n:
					if(predict(row[:6], G[m]) == False):
						G = G[:m] + G[m+1:]
						n = n - 1
					m = m+1						
									
			# negative example
			else:
				# update G
				for m in range(len(G)):
					# generate candidates						
					if(predict(row[:6], G[m]) == True):
						toSpecific = G[m]
						G = G[:m] + G[m+1:]
						
						for j, col in enumerate(toSpecific):
							if S[j] != "?" and S[j] != col and S[j] != row[j]:
								temp = toSpecific[:]
								temp[j] = S[j]								
								G += [temp]							
						
			print("S" + str(i+1) + ": " + str(S))
			print("G" + str(i+1) + ": " + str(G) + "\n") 	
		
		return S, G

train()
