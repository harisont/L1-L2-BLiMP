# L1-L2-BLiMP

The [BLiMP Benchmark of Linguistic Minimal Pairs](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00321/96452/BLiMP-The-Benchmark-of-Linguistic-Minimal-Pairs) as an [L1-L2 parallel UD treebank][L1-L2 parallel UD treebank](https://aclanthology.org/W17-6306/).

## Repository Contents
- original BLiMP data: `blimp/data/`
- L1-L2 BLiMP data: `blimp/treebanks/`
- Python script to build the treebanks with UDPipe 2: `blimp/gen_treebanks.py`
- description of all paradigms, for reference: ```blimp/BLiMP_Paradigms.pdf```

## Original BLiMP data

All 67 sub-datasets of BLiMP are available in .jsonl format.

Each contains 1000 lines in json format, with the following fields:
- `sentence_good`: The acceptable sentence 
- `sentence_bad`: The unacceptable sentence 
- `field`: Subfield of linguistics associated with the paradigm (there are 4 possible values: morphology, syntax, syntax-semantics, and semantics)
- `linguistics_term`: The category of phenomenon illustrated by the paradigm (there are 12 possible values, discussed in the paper)
- `UID`: The unique identifier for the paradigm 
- `simple_LM_method`: Boolean, identifies whether the paradigm is consistent with the `simple LM method` 
- `one_prefix_method`: Boolean, identifies whether the paradigm is consistent with the `one prefix method` 
- `two_prefix_method`: Boolean, identifies whether the paradigm is consistent with the `two prefix method`
- `lexically_identical`: Boolean, identifies whether the sentences in the paradigm are lexically identical
- `pairID`: A number from 0-999 identifying the index of the pair in the paradigm.

## L1-L2 treebanks
For each sub-dataset of BLiMP, two CoNNL-U files called `subset_name_L1.conllu` an2 `subset_name_L1.conllu` were created with the `blimp/gen_treebanks.py` script.

Each L1 (resp. L2) file contains the UD parse of the `sentence_good` (resp. `sentence_bad`) fields of each line of the correpsonding `.jsonl` file.
All other fields were added to both the L1 and L2 sentences as metadata without changes, excepts for the `pairID`, which was concatenated to the sub-dataset name and used as `sent_id`.  

For instance, the L1 CoNNL-U for  

```json
{"sentence_good": "Rebecca was criticizing those good documentaries.", "sentence_bad": "Rebecca was criticizing those good documentary.", "one_prefix_prefix": "Rebecca was criticizing those good", "one_prefix_word_good": "documentaries", "one_prefix_word_bad": "documentary", "field": "morphology", "linguistics_term": "determiner_noun_agreement", "UID": "determiner_noun_agreement_with_adjective_1", "simple_LM_method": true, "one_prefix_method": true, "two_prefix_method": false, "lexically_identical": true, "pairID": "0"}
```

from `data/determiner_noun_agreement_with_adjective_1.jsonl` is

```conllu
# sentence_good = Rebecca was criticizing those good documentaries.
# sentence_bad = Rebecca was criticizing those good documentary.
# one_prefix_prefix = Rebecca was criticizing those good
# one_prefix_word_good = documentaries
# one_prefix_word_bad = documentary
# field = morphology
# linguistics_term = determiner_noun_agreement
# UID = determiner_noun_agreement_with_adjective_1
# simple_LM_method = True
# one_prefix_method = True
# two_prefix_method = False
# lexically_identical = True
# sent_id = determiner_noun_agreement_with_adjective_10
1	Rebecca	Rebecca	PROPN	NNP	Number=Sing	3	nsubj	_	_
2	was	be	AUX	VBD	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	3	aux	_	_
3	criticizing	criticize	VERB	VBG	Tense=Pres|VerbForm=Part	0	root	_	_
4	those	that	DET	DT	Number=Plur|PronType=Dem	6	det	_	_
5	good	good	ADJ	JJ	Degree=Pos	6	amod	_	_
6	documentaries	documentary	NOUN	NNS	Number=Plur	3	obj	_	SpaceAfter=No
7	.	.	PUNCT	.	_	3	punct	_	SpaceAfter=No
```

UD annotation was obtained via the [UDPipe REST API](https://lindat.mff.cuni.cz/services/udpipe/api-reference.php), using the default 2.10 UD model for English.


## Recommended Citation
If you use BLiMP (original or this L1-L2 UD version) in your work, please cite it as follows:

```
@article{warstadt2020blimp,
    author = {Warstadt, Alex and Parrish, Alicia and Liu, Haokun and Mohananey, Anhad and Peng, Wei and Wang, Sheng-Fu and Bowman, Samuel R.},
    title = {BLiMP: The Benchmark of Linguistic Minimal Pairs for English},
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {8},
    number = {},
    pages = {377-392},
    year = {2020},
    doi = {10.1162/tacl\_a\_00321},
    URL = {https://doi.org/10.1162/tacl_a_00321},
    eprint = {https://doi.org/10.1162/tacl_a_00321},
    abstract = { We introduce The Benchmark of Linguistic Minimal Pairs (BLiMP),1 a challenge set for evaluating the linguistic knowledge of language models (LMs) on major grammatical phenomena in English. BLiMP consists of 67 individual datasets, each containing 1,000 minimal pairs—that is, pairs of minimally different sentences that contrast in grammatical acceptability and isolate specific phenomenon in syntax, morphology, or semantics. We generate the data according to linguist-crafted grammar templates, and human aggregate agreement with the labels is 96.4\%. We evaluate n-gram, LSTM, and Transformer (GPT-2 and Transformer-XL) LMs by observing whether they assign a higher probability to the acceptable sentence in each minimal pair. We find that state-of-the-art models identify morphological contrasts related to agreement reliably, but they struggle with some subtle semantic and syntactic phenomena, such as negative polarity items and extraction islands. }
}
```

If you use this particular version of the data, please also cite:

```
TBA
```

## License
BLiMP is distributed under a [CC-BY](https://creativecommons.org/licenses/by/4.0/) license.
