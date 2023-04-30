import os
import json
import requests

def udpipe2_parse(sentence):
  response = requests.get(
    'http://lindat.mff.cuni.cz/services/udpipe/api/process', 
    params= {
	    "tokenizer": "", 
	    "tagger": "",
	    "parser": "",
		  "model": "english",
	    "data": sentence})
  result = json.loads(response.text)["result"]
  not_comment = lambda line: not line.startswith("#")
  return "\n".join(list(filter(not_comment, result.split("\n"))))

	
	
if __name__ == "__main__":
	data = "data"
	treebanks = "treebanks"
	if not os.path.exists(treebanks):
		os.mkdir(treebanks)
	for json_path in sorted(os.listdir(data)):
		with open(os.path.join(data, json_path)) as json_file:
			subset = [json.loads(line) for line in json_file] 
		(subset_name,_) = os.path.splitext(json_path)
		subset_size = len(subset)
		print("Processing subset", subset_name)
		l1_conllu = []
		l2_conllu = []
		for (i,pair) in enumerate(subset):
			print("- sentence {} of {}".format(i + 1,subset_size))
			l1_sent = udpipe2_parse(pair["sentence_good"])
			l2_sent = udpipe2_parse(pair["sentence_bad"])
			comment_line = lambda keyval: "# {} = {}".format(
				keyval[0] if keyval[0] != "pairID" else "sent_id", 
				keyval[1] if keyval[0] != "pairID" else subset_name + keyval[1])
			comment_lines = list(map(comment_line, pair.items()))
			l1_conllu.append("\n".join(comment_lines) + "\n" + l1_sent)
			l2_conllu.append("\n".join(comment_lines) + "\n" + l2_sent)
		conllu_1_path = os.path.join(treebanks,subset_name + "_L1.conllu"
		conllu_2_path = os.path.join(treebanks,subset_name + "_L2.conllu"
		with open(conllu_1_path, 'w') as conllu_file:
			conllu_file.write("\n\n".join(l1_conllu))
		with open(conllu_2_path, 'w') as conllu_file:
			conllu_file.write("\n\n".join(l2_conllu))  
      