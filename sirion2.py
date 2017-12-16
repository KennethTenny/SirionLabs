import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize

train_text="The Executive agrees that during his/her employment hereunder, and for the one (1) year period immediately following the separation of employment for any reason, the Executive shall not solicit or contact any established client or customer of the Company with a view to inducing or encouraging such established client or customer to discontinue or curtail any business relationship with the Company. The Executive further agrees that the Executive will not request or advise any established clients, customers or suppliers of the Company to withdraw, curtail or cancel its business with the Company."
sample_text=input("Enter Input!")

custom_sent_tokenizer= PunktSentenceTokenizer(train_text)

tokenized= custom_sent_tokenizer.tokenize(sample_text)

def process_content():
		for i in tokenized[:]:
			words= nltk.word_tokenize(i)
			tagged= nltk.pos_tag(words)

			namedEnt = nltk.ne_chunk(tagged)

			namedEnt.draw()
#print(sent_tokenize(train_text))

process_content()

# print(word_tokenize(train_text))