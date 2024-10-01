# RAGnews ![Tests](https://github.com/RowanGray472/RAGnews/actions/workflows/tests.yml/badge.svg?branch=evaluate)
 
This branch adds an evaluate.py file that we can use to more robustly evaluate the RAG model set up in RAGnews.

If you're running this code on a mac, make sure to run this to ensure the pathing doesn't break.

```
export PYTHONPATH=.
```

Here's a sample interaction with the code (after setting up the virtual environment).

```
python3 RAGnews/evaluate.py
```

The system will chug along for a while—right now it's using (by default) the hairy-trumpet submodule to test its knowledge of recent political events and that dataset contains 127 masked examples. Once it finishes it'll print out how many it got right, the total number it checked, and its success rate. It usually gets around 79% of them right, but many more than that are pretty close to right.

You can change the dataset you want to use to test the RAGnews.py code by changing --data to your source.

This large language model I'm using runs into semi-consistent internal server errors. It used to only do this on GitHub actions workflows but now it does it locally too. My best guess is that Groq is just mad at me and that things will start working again soon. All this to say that if the tests aren't passing, this is likely why and I don't think there's much I can do about it, short of changing my API entirely. Check the error messages of the tests to make sure that's what's going wrong.
