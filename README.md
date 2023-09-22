# NewsAPI

A simple news api wrapper for the [News API](https://newsapi.org/) in python

/src: the python file for the api

/app: an example project showing how to use the api in a python project



# Get Started 
Start by creating a NewsSource object with an official  [News API](https://newsapi.org/) api key
```python
source = news.NewsSource('[API KEY]')
```

Search for a specified number of top headlines
```python
articles = source.getNumberOfArticles(3)
```

Search for a specific title
```python
articles = source.searchByTitle('Garmin Forerunner 265 review: runner’s best friend gets screen upgrade')
```

Search for articles with keywords
```python
articles = source.searchByKeyWords('ai, technology, apple')
```

Example of possible value of **articles** variable:
```python
{
    'status' : 'GOOD',
    'count' : 1,
    'articles' : 
        [
            {
                'title' : "Android can automatically archive apps you aren't using",
                'author' : "Jon Fingas",
                'source' : "Engadget",
                'description' : "After a teaser last year, Google is ready to help you save space on your phone by shelving unused apps. The company is rolling out an auto-archive feature that removes key parts of apps without erasing personal data. So long as an app is still available on th…",
                'url' : "https://www.engadget.com/android-can-automatically-archive-apps-you-arent-using-150337942.html",
                'imageurl' : "https://s.yimg.com/uu/api/res/1.2/nlm0UwtgoZYdf1SX1lZv0g--~B/Zmk9ZmlsbDtoPTYzMDtweW9mZj0wO3c9MTIwMDthcHBpZD15dGFjaHlvbg--/https://media-mbst-pub-ue1.s3.amazonaws.com/creatr-uploaded-images/2023-04/a1c6dff0-d872-11ed-bcf1-41f73c825e11.cf.jpg",
                'published' : "2023-04-11T15:03:37Z",
                'content' : "After a teaser last year, Google is ready to help you save space on your phone by shelving unused apps. The company is rolling out an auto-archive feature that removes key parts of apps without erasi… [+1251 chars]"
            }
        ]
}
```
More documentation is provided in [/docs](/docs/)
Open the index.html file for html documentation page



# Run Instructions
This repository contains an example project that demonstrates how to use the api. It requires [pip](https://pip.pypa.io/en/stable/cli/pip_install/) be installed.

**Important: a [News API](https://newsapi.org/) API key is required to run the application!**

After obtaining the api key, create \app\key.txt file and place only the key in the file

## Windows


Go to app\ directory
```cmd
cd app
```

Create a virtual environment 
```cmd
py -3 -m venv venv
```

Activate the virtual environment 
```cmd
venv\Scripts\activate
```

Install Flask in the virtual environment
```cmd
pip install Flask
```

Install Flask-CORS extension 
```cmd
pip install -U flask-cors
```

Run Application
```cmd
flask --app app run
```

This should output the following:
![](res/flask_out.png?raw=true)


Open http://localhost:5000/search in web browser or run **start.bat**



## Linux (Ubuntu)

Go to app\ directory
```bash
cd app
```

Create a virtual environment 
```bash
python3 -m venv venv
```

Activate the virtual environment 
```bash
source venv/bin/activate
```

Install Flask in the virtual environment
```bash
pip install Flask
```

Install Flask-CORS extension 
```bash
pip install -U flask-cors
```

Run Application
```bash
flask run
```
This should output the following:
![](res/flask_out_linux.png?raw=true)

Open http://localhost:5000/search in web browser or run **start**
