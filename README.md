# RAGnews ![Tests](https://github.com/RowanGray472/RAGnews/actions/workflows/tests.yml/badge.svg)
 
This repo contains code to have a conversation with the Groq API agent about recent events in American politics, using RAG to familiarize the model with recent news.

Here's a sample interaction with the code (after setting up the virtual environment)

```
python3 RAGnews.py
```

Then the system prints this

```
ragnews>
```

And we ask...

```
Who is the current Democratic party candidate for president?
```

And we get...

```
Based on the provided articles, the current Democratic Party candidate for president is not explicitly stated, as Joe Biden has already held the office and is now stepping aside. In fact, Article 6 states that President Joe Biden has withdrawn from the presidential election against Republican candidate Donald Trump. Additionally, Article 9 indicates that Kamala Harris has been chosen as the party's nominee for the presidential election, suggesting that she is the current Democratic Party candidate for president.
```

Soooo, not perfect but closer than you'll get from a non-RAG API!
