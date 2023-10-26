# URL Classification with ML
Research project (WIP) - evaluating the most effective metrics for predicting malicious URLs using ML.
### What dataset is used?
We randomly sampled 60,000 benign and 40,000 malicious urls from [this kaggle dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset/).

### What metrics will be used?
**Classification bins:**
- Benign of malicious
  
**Lexical features:**
- URL Length
- URL file extension (.html, .php, .pdf for example)
- Hostname
- Top-Level Domain
- Does the URL use a commmon shortener (bit.ly, ow.ly, etc.)?
- Domain features:
  * Domain token count
  * Domain token average length
  * Domain token max length
  * Domain token length standard deviation
- Path features:
  * Path token count
  * Path token average length
  * Path token max length
  * Path token length standard deviation

**Content features**
WIP!
