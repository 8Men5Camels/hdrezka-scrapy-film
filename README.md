# Scraping movie data
> Python project for scraping movie data from the hdrezka site

## Installing / Getting started

Python3 must be already installed
> You’ll need to use different syntax for activating the virtual environment depending on which operating system and command shell you’re using.

#### On Windows using the Command Prompt:
```shell
git clone https://github.com/8Men5Camels/hdrezka-scrapy-film.git
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python hdrezka/spiders/film.py # run script film.py
```

We will receive a `film.csv` file with saved movie data. And we read it using pandas DataFrame. 

To get the data of another movie, you need to change the link in the `start_urls` variable
