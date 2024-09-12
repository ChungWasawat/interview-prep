import spacy

"""-----------------------------spacy tokenization-----------------------------"""
nlp = spacy.load("en_core_web_sm")
#nlp.remove_pipe('tagger')      #reduce model size
#nlp.remove_pipe('parser')      #reduce model size

doc = nlp("Colorless green ideas sleep furiously.")
token = doc[3]
#print(f"Type of token: {type(token)}")
#print('Offset of token in source text:', token.idx)
#print('Source text of token:', token.text)
#print('Part of speech (e.g. noun, verb, etc):', token.pos_)
#print('Lemma (shortened/standardized form of word):', token.lemma_)
#print('Is this token a stopword (a common word which can be ignored)?:', token.is_stop)
#print('Is this token punctuation?:', token.is_punct)
#print('Is this token whitespace (e.g. spaces, tabs, newlines, etc)?:', token.is_space)

"""-----------------------------spacy example-----------------------------"""
from typing import List, Any
import spacy
import os
#from openai import OpenAI

nlp = spacy.load("en_core_web_sm")
def transform_data(data: List[str]) -> List[dict[str, Any]]:
    id = 0
    result = []
    for d in data:
        row = {}
        row['id'] = id
        row['content'] = d
        row['keywords'] = []
        for token in nlp(d):
            if token.pos_ == "NOUN" or token.pos_ == "PROPN":
                row['keywords'].append(token)
        row['summary'] = summarise(d)

        result.append(row)
        id += 1
    return result

def summarise(content: str) -> str:
    #client = OpenAI( api_key=os.environ.get("OPENAI_API_KEY") )
    #prompt = f"Summarize the following text: {content}"
    #low temperature -> more concise and accurate 
    #summary = client.chat.completions.create( model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], temperature=0.2)
    return #summary.choices[0].text.strip()

def ai_search(query: str) -> str:
    #client = OpenAI( api_key=os.environ.get("OPENAI_API_KEY") )
    #chat_completion = client.chat.completions.create( model="gpt-4o-mini", messages=[{"role": "user", "content": query}], temperature=0.3 )
    return #chat_completion

input = [ "OpenAI creates advanced AI tools.", "Python is widely used for data science."]
output = transform_data(input)
#print(output)

# example 2
input = "Tell me about OpenAI"
ouptu = ai_search(input)