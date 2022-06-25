# Trek-Reccomendation
**Goal** - The Goal of this project is to provide treks suggestion on given dates with required information <br />
**Skills used** - Web Scraping, Pandas <br>
**Libraries used** - Selinium, BeatifulSoup, Pandas

## Web Scraping
The data for the project is recieved by scraping the website of Bikat Adventures (Bikatadventures.com) <br />
The data is scraped using Selenium web automation tool. The scraper first generates url for all treks b scraping monthwise trekking Data <br>
The generated url is stored in a list which now contains all treks from the website <br>
This list is further iterated to get features like Difficulty, Source, Destination, Cost, Months, Description, Addons. <br>
The scraped data is received byy crawling the elements in the page and is stored in the form of tupple. <br>
This stored data is further converted to a data frame <br>

## Model
Scrapping errors are further handled in Excel. <br />
Use Pandas to create required features and Analyze Dataset <br />
Use Pandas to filter out trek recemondations based on season, no of days and Difficulty <br />
Analyze the no of days between given dates and suggest all the possible treks in combination between those days <br>
For Example - If the date range include 10 days then suggest a 10 day trek as well as combination of 4 day trek and 6 day trek depending on the season. 


