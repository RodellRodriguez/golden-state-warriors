# golden-state-warriors

**Description**

This Jupyter Notebook performs web scraping and basic data visualizations to highlight the differences in the Golden State Warriors's shooting preferences between 1996-2017. For Web Scraping I am using Python's Requests library to web scrape the [advanced shooting stats of Golden State Warriors](http://stats.nba.com/team/#!/1610612744/shooting/). In particular I am looking at the downward trend of mid range shots taken over the years and comparing it against the upward trend of 3 pointer shots. 

Originally I wanted to use Selenium to web scrape the stats data since I learned to do web automation at my job with Selenium however after researching multiple ways of web scraping I found [this](http://www.gregreda.com/2015/02/15/web-scraping-finding-the-api/) to scrape the data in a JSON format. After scraping the JSON data I create a nested dictionary where the outer dictionary keeps track of which year to access while the inner dictionary keeps track of which particular shooting stat to view for that particular year. Since JSON is a semi-structured data format, it's alot better to web scrape JSON than parsing completely unstructured data. While I can probably do that with Beautiful Soup, it's much better to use the tool that does the job most efficiently.

**Dependencies**
* Python 3.5
* Pandas
* Requests
* Matplotlib
* Jupyter Notebook