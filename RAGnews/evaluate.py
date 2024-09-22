"""
This file will evaluate the functionality of the RAGnews model using the
Hairy-Trumpet dataset.
"""

import RAGnews

class RAGEvaluator:
    def predict(self, text, keywords, masks):
        """
        >>> model = RAGEvaluator()
        >>> model.predict("The current democratic candidate for president 
        is [MASK0])
        ['Harris']
        >>> model.predict("There is no mask in here")
        []
        >>> model.predict("The current democratic candidate 
        for president is [MASK0] and the republican candidate is [MASK1]")
        ['Harris', 'Trump']
        """
        db = RAGnews.ArticleDB()
        output = RAGnews.rag(text, db, keywords)
        return output
    
import json
import glob

def load_data(directory):
    files = glob.glob(f"{directory}/*")
    data = []
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                data.append(json.loads(line))
    return data

# Use the function to load data from the 'hairy-trumpet/data' directory
data = load_data('hairy-trumpet/data')

model = RAGEvaluator()
correct = 0
total = 0
for d in data:
    text = d['masked_text']
    keywords = d['masked_text']
    masks = d['masks']
    prediction = model.predict(text, keywords, masks)
    if prediction == masks:
        correct += 1
    total += 1
print(f"Accuracy: {correct/total}")