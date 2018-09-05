from model import Model
import sys


def main():
	model = Model()
	textFiles = sys.argv[1:-2]
	for textFile in textFiles:
		try:
			print('fit', textFile)
			model.fit(textFile)
		except FileNotFoundError:
			print("Error:", textFile, "not found")
			return
	outputFile = sys.argv[-2]
	numWords = sys.argv[-1]
	model.generate(outputFile, int(numWords))


if __name__ == '__main__':
	main()
