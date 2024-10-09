### spacy setup
```pip install -U spacy```    
```python -m spacy download en_core_web_sm```

### interesting packages
1. In Notebook, `tqpm` can give a nice bar to track progress
```
from tqdm import tqdm
for post in tqpm(posts): 
    post['token'] = tokenize(post['body']) 
```
2. `urllib` to extract data from website

3. `tensorflow` for machine learning and deep learning in Image recognition, natural language processing, and other complex machine learning tasks.
4. `beautifulsoup` for web scraping and parsing HTML and XML documents2.
5. `matplotlib` for creating static, interactive, and animated visualizations
6. `flask` for building web applications 
    - [my simple flask project](https://github.com/ChungWasawat/simple_flask)