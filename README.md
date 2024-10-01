# RAGnews ![Tests](https://github.com/RowanGray472/RAGnews/actions/workflows/tests.yml/badge.svg?branch=evaluate)
 
This branch adds an evaluate.py file that we can use to more robustly evaluate the RAG model set up in RAGnews.

Here's a sample interaction with the code (after setting up the virtual environment)

```
python3 RAGnews/evaluate.py
```

The system will chug along for a while—right now it's using (by default) the hairy-trumpet submodule to test its knowledge of recent political events and that dataset contains 127 masked examples. Once it finishes it'll print out how many it got right, the total number it checked, and its success rate. It usually gets around 79% of them right, but many more than that are pretty close to right.

You can change the dataset you want to use to test the RAGnews.py code by changing --data to your source.
