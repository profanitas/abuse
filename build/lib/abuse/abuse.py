from dataset import dataset
import random

def ListAbusesFrom(data_in):
	_temp=[]
	if type(data_in) is not str:
		return("No Abuse Words from", data_in, "Provide input between a-z instead")
	data_in=str(data_in).lower()
	for i in dataset:
		if i.startswith(data_in):
			_temp.append(i)


	return _temp

def RandomAbuseFrom(data_in):
	_temp=[]
	if type(data_in) is not str:
		return("No Abuse Words from", data_in, "Provide input between a-z instead")
	data_in=str(data_in).lower()
	for i in dataset:
		if i.startswith(data_in):
			_temp.append(i)

	return random.choice(_temp)


def ListAnyAbuse():
	return random.choice(dataset)

def ListAllAbuses():
	return dataset
