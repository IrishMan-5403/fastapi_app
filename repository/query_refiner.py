import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class QueryRefiner:
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        
    def get_synonyms(self, word):
        synonyms_with_counts = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms_with_counts.append((lemma.name(), lemma.count()))
        synonyms_with_counts.sort(key=lambda x: x[1], reverse=True)
        top_synonyms = [synonym[0] for synonym in synonyms_with_counts[:2]]
        return top_synonyms

    def get_refined_query(self, query):
        tokens = word_tokenize(query.lower())
        
        tokens = [word for word in tokens if word not in self.stop_words]
        
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]
        

        refined_tokens = []
        for word in tokens:
            refined_tokens.append(word)
            refined_tokens.extend(self.get_synonyms(word))



        
        refined_query = ' '.join(refined_tokens)
        
        return refined_query