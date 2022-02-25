"""
Usage:
    csv-to-latex-card.py <input-csv-file> <output-file> [<preamable-file>] [<postamble file>]
Generates latex cards from an input file.
"""

#you may need to pip3 install nltk

import argparse
import csv
import re

max_chars = 400

#raw first

def get_sentences(text):
	sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',text)#https://intellipaat.com/community/18380/python-regex-for-splitting-text-into-sentences
	# print(sentences)
	return sentences


def main(files):
	for f in files:
		print(f)
	preamble = open("preamble.txt").read()
	postamble = open("postamble.txt").read()
	infile = open(files[0])
	outfile = open(files[1],"w")
	outfile.write(preamble)
	rows = csv.DictReader(infile)
	for row in rows:
		# print(row)
		sentences = get_sentences(row['text'])
		auto_chunks = []
		running_chars = 0
		current_chunk = ""
		for s in sentences:
			# print(len(s))
			if running_chars + len(s) < max_chars:
				if running_chars > 0:
					current_chunk += " "
				running_chars += len(s)
				current_chunk += s
			else:
				auto_chunks += [current_chunk]
				running_chars = len(s)
				current_chunk = s
		auto_chunks += [current_chunk]
		# print("AUTOS")
		# print(len(auto_chunks))
		i = 0
		for chunk in auto_chunks:
			#context etc.
			i+=1
			outfile.write("\\textbf{ID: "+row["id"]+"."+str(i)+"} \\emph{Context: "+row["context"]+"}\\\\ \n")
			outfile.write(chunk+" \\newpage \n\n")
	outfile.write(postamble)


	print("done with main")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    opts = parser.parse_args()
    print(opts.files)
    main(opts.files)