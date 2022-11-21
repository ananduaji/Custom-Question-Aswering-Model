# Question Answering System
### link: https://huggingface.co/spaces/ananduaji/question_answering

## Overview
The Question Answering System is a web app which answers the questions based on the context given in the text area. The model is based on the RoBERTa transformer, which is a Transformer model. Also fine tuned using SQuAD[Stanford Question Answering Dataset] dataset with the help of Haystack library, which is an open source NLP framework that leverages pre-trained Transformer models. Used Streamlit to make the web app and deployed in the Hugging Face Spaces.

The web app contains two boxes of context and question. User should paste the context before asking the question.




which is a transformer model pretrained on a large corpus of English data in a self-supervised fashion. RoBERTa builds on BERT's language masking strategy, wherein the system learns to predict intentionally hidden sections of text within otherwise unannotated language examples. BERT uses static masking i.e. the same part of the sentence is masked in each Epoch. In contrast, RoBERTa uses dynamic masking, wherein for different Epochs different part of the sentences are masked. This makes the model more robust.
