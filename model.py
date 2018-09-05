import re
import random


class Model:

	def __init__(self):
		self.bgram = dict()
		open('bgramlist.txt', 'w')
		self.bgramFiles = open('bgramlist.txt', 'r').read().split(',')
		for file in self.bgramFiles:
			if file != '':
				self.readBgram(file)


	def readBgram(self, filename):
		lines = open(filename, 'r').readlines()
		for line in lines:
			words = line.split(',')
			first = words[0]
			other = words[1:-1]
			if first not in self.bgram.keys():
				self.bgram[first] = other
			else:
				self.bgram[first].extend(other)


	def addBgram(self, filename, currBgram):
		if filename not in self.bgramFiles:
			output = open(filename, 'w')
			for el in currBgram.keys():
				output.write(el + ',')
				for word in currBgram[el]:
					output.write(word + ',')
				output.write('\n')
			output.close()
			self.bgramFiles.append(filename)
			open('bgramlist.txt', 'a').write(',' + self.bgramFiles[-1])



	def fit(self, filename):
		bgramFile = filename + '.bgram'
		if bgramFile not in self.bgramFiles:
			data = open(filename, 'r').read() 
			words = [word.lower() for word in re.findall(r'\w+', data)]
			currBgram = dict()
			for i in range(len(words) - 1):
				if words[i] not in currBgram.keys():
					currBgram[words[i]] = [words[i + 1]]
				else:
					currBgram[words[i]].append(words[i + 1])

			self.addBgram(filename + '.bgram', currBgram)
			self.readBgram(filename + '.bgram')


	def generate(self, outputFile, wordsNum):
		output = ''
		state = random.choice(list(self.bgram.keys()))
		for i in range(wordsNum):
			output += state + ' '
			if state in self.bgram.keys():
				state = random.choice(self.bgram[state])
			else:
				state = random.choice(list(self.bgram.keys()))
		open(outputFile, 'w').write(output)




