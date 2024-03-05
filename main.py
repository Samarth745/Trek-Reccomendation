import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import nltk
import openpyxl
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import ast
from ast import literal_eval

stop_words = (stopwords.words('english'))

# pd.DataFrame.head = partialmethod(pd.DataFrame.head, n=2)
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', None)


#@title GetData - TransformData
treks = pd.read_excel("Bikat_alltreks.xlsx").drop(columns="Unnamed: 0")
trek_lookup = treks.reset_index()[["index", "name"]]
short_to_full = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}
treks['Season'] = treks['Season'].apply(ast.literal_eval)
treks["Season"] = treks["Season"].apply(lambda x: ', '.join([short_to_full[month] for month in x]))
treks["difficulty"] = treks["difficulty"].apply(lambda x:"easy" if x<4 else "difficult")
treks.dropna(inplace=True)
treks["description"] = treks["description"]+" "+treks["difficulty"]+" "+treks["Season"]


app = Flask(__name__, template_folder='template', static_folder='static')
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/Recommended', methods=['POST'])
def Recommend():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
    description=to_predict_list['trek_description']
    global treks
    description = description.lower()
    description = word_tokenize(description)
    stop_words = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    filtered = {word for word in description if word not in stop_words}
    filtered_set = set()
    for fs in filtered:
      filtered_set.add(lemmatizer.lemmatize(fs))
    filtered_set
    list1 = []; list2 = []; cos = [];
    treks = treks.set_index(np.arange(treks.shape[0]))

    for i in range(treks.shape[0]):
        temp_token = word_tokenize(treks["description"][i])
        temp_set = [word for word in temp_token if word not in stop_words]
        temp2_set = set()
        for s in temp_set:
            temp2_set.add(lemmatizer.lemmatize(s))
        vector = temp2_set.intersection(filtered_set)
        cos.append(len(vector))
    treks['similarity'] = cos
    treks = treks.sort_values(by='similarity', ascending=False)
    try:
        treks.reset_index(inplace=True)
    except:
        pass
    suggestions = treks.iloc[0:3]
    suggestions_name = suggestions["name"].values
    suggestions_link  = suggestions["link"]
    suggestions_poster = []
    suggestions_prices = []
    suggestions_seasons = suggestions["Season"].values
    for link in suggestions_link:
      html = requests.get(link).content
      soup = BeautifulSoup(html, 'html.parser')
      poster_image = "https://www.bikatadventures.com//%s"%(soup.find('div', class_="blog col-6").select('div img'))[0]['src']
      price = soup.find("div", class_='price-tag').text.replace("\n+ 5% GST\n", "").replace("\n", "").replace("₹","").replace(" ","")
      suggestions_poster.append(poster_image)
      suggestions_prices.append(price)
    all_list = zip(suggestions_name, suggestions_link, suggestions_poster, suggestions_prices, suggestions_seasons)
    return render_template('recommendations.html', search=description, all_list=all_list)

@app.route('/Notebook')
def view_notebook():
    return render_template('Notebook.html')

@app.route('/info')
def view_info():
    return render_template('idea.html')
if __name__ == "__main__":
    app.run(debug=True)
