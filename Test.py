import spacy

nlp = spacy.load('en_core_web_sm')

sentence = "Apple acquires the Zoom app of China and stock\
	 in NYSE rise by 5%. And Virtusa is now trying to buy Apple insted."
doc = nlp(sentence)

for entity in doc.ents:
	print(entity.text, entity.label_)