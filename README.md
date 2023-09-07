# WEB SCRAPING USING BEAUTIFUL SOUP

`Beautiful Soup` is a library in python which can be used for web scraping. Web scraping is a technique which is used to get useful data from a target website. This is useful for statistical analysis and finding crucial data from a website. 

One needs to first create a `soup` object. Using that we can request the html content fromn the desired website using a `GET` request. The `GET` request return the `HTML` content. The `HTML` content is raw data which can be formatted further as per the need. 

I collected data from the official website of `IMDB` using the list of `URLs`. Each `URL` contains 100 movies. The data corresponds to the top 1000 highest grossing movies of all time. I have further formatted the data which is stored in a `csv` file. The contents of the `csv` file are as follows

* `Movie Name`
* `IMDB Rating`
* `Genre`
* `Runtime (in min)`
* `Year`
* `Gross Income (in $)`

One can do further analysis and use `matplotlib` for visual representation of the data collected. I have plotted a `bar graph` for `Frequency Vs Genre`.

> imdb.py :- `Python` script for web scraping

> imdb.csv :- `csv` file containing the top 1000 highest grossing movies of all time

> imdb.png :- `Bar graph` for `Frequency Vs Genre`

> data.py :- `Python` script which reads the csv file, prints the top 100 movies of all time and does data analysis as per the requirements of the user. The arguments for this script must be space separated.

## Requirements
The user needs to install `beautiful soup` package using this command

>`pip install bs4`

