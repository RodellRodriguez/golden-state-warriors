# golden-state-warriors

Playing with Web Scraping and Data Visualization functionality for self-learning and transition into Data Science. For Web Scraping I am using the Requests library to web scrape Shooting stats of Golden State Warriors team during the 2016-2017 season from http://stats.nba.com/ specifcally http://stats.nba.com/team/#!/1610612744/shooting/ .

Originally I wanted to use Selenium to web scrape the stats data since I learned to do web automation at my job with Selenium however after researching multiple ways of web scraping I found this http://www.gregreda.com/2015/02/15/web-scraping-finding-the-api/ to scrape the data in a JSON format and saved the data in a csv format. Since JSON is a semi-structured data format, it's alot better to web scrape JSON than from completely unstructured data.

From the 2'nd URL you can see that there are multiple tables for different shooting stats. The web scraping script exports each table to its own CSV file as shown in the "Stats" folder. 

Now that I have data I am now playing with the data by getting accustomed to data visualization via pandas, matplotlib, seaborn, and numpy libraries.
