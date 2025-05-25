# NEWTON - Tons of News Summarized

## Description
<p>This project has a simple and clear user interface, wherein the user is expected to give the news he or she gathered from multiple sources in a paragraph format as input. The underlying BART model summarizes the text and gives the summary.
We have also incorporated dashboards where the users are presented with scores and metrics that testifies why this summarizer app stands apart from others highlighting the versatile capabilities of BART put against BERT and T5. Users are also given the liberty to fully tune the 
  model parameters depending upon their requirements.</p>

## About BART
<ul>
  <li>BART - Bidirectional and Auto-Regressive Transformers</li>
  <li>BART is a powerful sequence-to-sequence model developed by Facebook AI, designed for natural language generation tasks like summarization, translation, and text generation.</li>
  <li>BART is pre-trained using a denoising autoencoder approach: it learns to reconstruct original text from corrupted input. 
  This makes it especially effective for tasks requiring a deep understanding of structure and semantics.</li>
</ul>

## Steps to Execute
<p>Please go through the dependencies given in the `requirements.txt` and get them installed on your PC to fully setup the environment for execution. Then follow the steps given below.</p>
<ol>
  <li>First run the `personalized_news.py` script to load the model.</li>
  <li>Then run the `summarizer_app.py` to open the app.</li>
  <li>Then run the `dashboard.py` to see the dashboards in the app.</li>
</ol>

## Alternative
Go to this link to see our news summarizer application being deployed: https://newton-news-summarized.streamlit.app/
You have a button there that redirects you to the dashboard page after clicking.
