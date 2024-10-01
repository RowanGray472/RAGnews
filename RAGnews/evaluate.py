"""
This file will evaluate the functionality of the RAGnews model using the
Hairy-Trumpet dataset.

1. python3 -m venv env
2. source env/bin/activate
3. pip install -r requirements.txt
4. export PYTHONPATH=.
5. python3 RAGnews/evaluate.py

"""

import RAGnews

class RAGEvaluator:
    def __init__(self, correct_labels):
        self.labels = correct_labels
    def predict(self, text, correct_labels):
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
        output = RAGnews.rag(text, db, text, correct_labels)
        return output
    
if __name__ == '__main__':
    import argparse
    import json
    import os

    filepath = r"hairy-trumpet/data/wiki__page=2024_United_States_presidential_election,recursive_depth=0__dpsize=paragraph,transformations=[canonicalize, group, rmtitles, split]"

    # Argument parser for command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default=filepath)
    args = parser.parse_args()

    # Load data from the current file
    with open(args.data, 'r') as f:
        data = [json.loads(line) for line in f]

    # Extract unique labels from the data
    labels = set()
    with open(args.data, 'r') as fin:
        for i, line in enumerate(fin):
            dp = json.loads(line)
            labels.update(dp['masks'])

    n_correct = 0
    n_tests = 127
    print(labels)
    evaluator = RAGEvaluator(correct_labels=labels)
    for i, text_case in enumerate(data[:n_tests]):
        prediction = evaluator.predict(text_case["masked_text"], labels)
        if prediction == str(text_case["masks"]):
            n_correct += 1
        print(f"number processed: {i} out of {n_tests}")
    correct_ratio = n_correct / n_tests

    print("Number Correct:", n_correct)
    print("Total Test Cases:", n_tests)

    print("Correct Ratio:", correct_ratio)
