# golden-state-warriors

**Description**

This Jupyter Notebook web scrapes stats from [NBA.com's](https://stats.nba.com/) API and then creates basic data visualizations to show the change in the Golden State Warriors's shooting preferences between the years 1996-2017. In particular I am looking at the decreasung trend of mid range shots taken over the years and comparing it against the upward trend of 3 pointer shots. As an avid basketball fan, I'm very intrigued in basketball trends and I think using data to validate patterns and tell a story is very reassuring and interesting.

For Web Scraping I am using Python's Requests library to web scrape the [advanced shooting stats of Golden State Warriors](http://stats.nba.com/team/#!/1610612744/shooting/). 

I found [this very helpful article](http://www.gregreda.com/2015/02/15/web-scraping-finding-the-api/) to find the endpoints of NBA.com's stats API to scrape the data in a JSON format. After scraping the JSON data I created a nested dictionary where the outer dictionary keeps track of which year to access while the inner dictionary keeps track of which particular shooting stat to view for that particular year. Since JSON is a structured data format, it's alot better to web scrape JSON than parsing completely unstructured data. While I can probably do that with Beautiful Soup, it's much better to use the tool that does the job most efficiently.

**Dependencies**
* Python 3.5
* Pandas
* Requests
* Matplotlib
* Jupyter Notebook