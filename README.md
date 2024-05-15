# Trek Recommendation
![Image](https://raw.githubusercontent.com/Samarth745/Portfolio-Website/master/assets/imgs/folio-2.png)
## Introduction:

The Trek Recommendation project aims to provide trek suggestions based on user preferences and available dates. It utilizes web scraping techniques, Pandas for data analysis, and Natural Language Processing (NLP) to filter and recommend suitable trekking options.


## Goals:
The goal of the project is to create an end to end AI Based System to help Select Treks
- To develop a system that can recommend trekking options based on user preferences and available dates and price using Pandas data Filtering
- Suggest Treks based on Description provided using Natural Langauge Processing

## Skills Used:

- Web Scraping (Using Requests and Beautiful Soup)
- Natural Language Processing (NLP) - NLP Techniques to generate a clean feature list from data 
- Machine Learning - Creating a suggestion model using cosine similarity
- Deployment - Git, HTML and CSS for creating frontend for this project


## Libraries Used:

- Requests
- BeautifulSoup
- Pandas
- nltk
  
### Data 
The dataset is extracted from trekking websites using Web scraping techniques

### Key Features:

- **Filter Trek Recommendations:** Filter trek recommendations based on user preferences for season, number of days, and difficulty level.
- **Date Range Analysis:** Analyze the number of days between given dates to determine the available trekking duration. Suggest suitable trekking options based on the available duration, considering both single trek options and combinations of shorter treks.
- **NLP-based Trek Suggestions:** Apply Natural Language Processing techniques to analyze textual descriptions of treks. Provide best trek suggestions based on the analysis of trek descriptions, highlighting top recommendations based on user preferences and trek characteristics. 

### Deployment:

The project is deployed and live on [Render](https://trek-reccomendation.onrender.com/).

### Additional Features:

- **TF-IDF and Detailed Analysis for Domain Stop Words:** Utilized TF-IDF to understand domain-specific stop words and refine the feature list.
- **Price-based Filtering:** Implemented price-based filtering logic in Pandas to further refine trek recommendations based on budget constraints.
- **Cosine Similarity Based ML Suggestions:** Incorporated cosine similarity-based machine learning suggestions to enhance trek recommendations by considering textual descriptions and similarities between treks.

## Project Flow:

The project follows the below flow:

1. **Scraping and Initial Data Cleaning:** Handle scraping errors and perform initial data cleaning. We have used requests model to Scrape Trek Data from Trekkking websites. further used Beatiful Soup to prse the html and create a tabular data set out of it
2. **Data Preprocessing with Pandas:** Use Pandas to preprocess and clean the dataset, including feature engineering and TF-IDF for stop words.
3. **Trek Recommendation Filtering:** Filter trek recommendations based on user preferences and price constraints using Pandas.
4. **Date Range Analysis and Trek Suggestions:** Analyze available trekking duration between given dates and suggest suitable trekking options using Pandas and NLP.
5. **NLP-based Best Trek Suggestions:** Utilize NLP techniques to analyze textual descriptions of treks and provide enhanced trek suggestions using cosine similarity-based ML.

### Conclusion:

The Trek Recommendation project leverages web scraping, Pandas, NLP, and machine learning techniques to assist users in finding optimal trekking experiences tailored to their preferences and available time.


## Contributing:
Contributions to this project are welcome! 
If you have any ideas for improvements or feature enhancements, feel free to open an issue or submit a pull request.


## Contact Information:
For any inquiries or feedback regarding this project, please email me [Samarth Prabhu](prabhusamarth001@gmail.com)
