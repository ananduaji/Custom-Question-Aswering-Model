# Question Answering System
### link: https://huggingface.co/spaces/ananduaji/question_answering

## Overview
The Question Answering System is a web app which answers the questions based on the context given in the text area. The model is based on the RoBERTa transformer, which is a Transformer model. Also fine tuned using SQuAD[Stanford Question Answering Dataset] dataset with the help of Haystack library, which is an open source NLP framework that leverages pre-trained Transformer models. Used Streamlit to make the web app and deployed in the Hugging Face Spaces.

The web app contains two boxes of context and question. And a Submit button. User should paste the context before asking the question.

### This is where the context should be in.
![](https://user-images.githubusercontent.com/90780162/203083779-b2c41c60-d488-47ce-afe9-8eb9facae9bf.png)

### The Question should ask here.
![](https://user-images.githubusercontent.com/90780162/203083759-6f929ad6-f53b-48ba-9935-8bb669e3f623.png)

Then after pressing the submit button the answer will be shown below.

## Examples
#### Here, the model predicted the answers correctly.
![](https://user-images.githubusercontent.com/90780162/203084302-aff316d4-f8a7-4bc6-a998-9a82bb466eea.png)

![](https://user-images.githubusercontent.com/90780162/203084297-8ba867bb-3bec-445d-8824-ea0edd385431.png)

![](https://user-images.githubusercontent.com/90780162/203084288-67d9f676-778b-41f9-b784-c261ff74ef51.png)

#### If the answer is not in the text given then it shows:
![](https://user-images.githubusercontent.com/90780162/203087941-347137e2-d022-49ac-83c9-68ba4f21be80.png)

## What is RoBERTa ?
RoBERTa is a transformer model pretrained on a large corpus of English data in a self-supervised fashion. RoBERTa builds on BERT's language masking strategy, wherein the system learns to predict intentionally hidden sections of text within otherwise unannotated language examples. BERT uses static masking i.e. the same part of the sentence is masked in each Epoch. In contrast, RoBERTa uses dynamic masking, wherein for different Epochs different part of the sentences are masked. This makes the model more robust.

## Haystack
Haystack is a python framework for developing End to End question answering systems. It provides a flexible way to use the latest NLP models to solve several QA tasks in real-world settings with huge data collections. Haystack is useful for providing solutions to diverse QA tasks such as Financial Governance, Knowledge Base Search, Competitive intelligence etc. Haystack is available as an open-source library with an extended paid enterprise version with all the bells and whistles. 


## Project Roadmap
1. Fine tuning the RoBERTa transformer model using haystack.
  * Importing FARMReader class from Haystack.
  * Downloading RoBERTa model from HUgging Face.
  * By using the SQuAD dataset training the model for 5 epochs.
  * Saving the model for our web app.
2. By using Streamlit making the web app.
3. Deploying the web app in Hugging Face Spaces.


 ## Technologies Used
 
 


