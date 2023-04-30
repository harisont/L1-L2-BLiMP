import os 
import conllu

def write_conllu(path,sentences):
		with open(path,"w") as outfile:
				outfile.write(
					"".join([sentence.serialize() for sentence in sentences]))

if __name__ == "__main__":
	treebanks_dir = "treebanks"
	morphosyntax = ["morphology", "syntax"]
	treebanks = sorted(os.listdir(treebanks_dir))
	l1_treebanks = list(filter(lambda p: p.endswith("L1.conllu"), treebanks))
	l2_treebanks = list(filter(lambda p: p.endswith("L2.conllu"), treebanks))
	l1_ms_sentences = []
	l2_ms_sentences = []
	for (l1_treebank,l2_treebank) in zip(l1_treebanks,l2_treebanks):
		with open(os.path.join(treebanks_dir, l1_treebank)) as conllu_file:
			l1_txt = conllu_file.read()
		with open(os.path.join(treebanks_dir, l2_treebank)) as conllu_file:
			l2_txt = conllu_file.read()
		l1_sentences = conllu.parse(l1_txt)
		l2_sentences = conllu.parse(l2_txt)
		for (l1_sentence,l2_sentence) in zip(l1_sentences,l2_sentences):
			# double check alignment
			l1_sentence_id = l1_sentence.metadata["sent_id"]
			l2_sentence_id = l2_sentence.metadata["sent_id"]
			try:
				assert l1_sentence_id == l2_sentence_id
			except:
				print(l1_sentence_id, l2_sentence_id)
				exit(-1)

			# enough to check one sentence
			field = l1_sentence.metadata["field"]
			lexically_id = l1_sentence.metadata["lexically_identical"] == "True" 
			if field in morphosyntax and lexically_id:
				l1_ms_sentences.append(l1_sentence)
				l2_ms_sentences.append(l2_sentence)
	assert len(l1_ms_sentences) == len(l1_ms_sentences)
	write_conllu(os.path.join(treebanks_dir, "MS_L1.conllu"), l1_ms_sentences)
	write_conllu(os.path.join(treebanks_dir, "MS_L2.conllu"), l2_ms_sentences)	  
			
					
				

	