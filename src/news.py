import json
import urllib.request
import urllib.parse
from typing import Any, Dict
import math




def get_attribs_from_articles(article_list) -> Dict[str, str]:
    """
    Function used internally by NewsSource class
    """
    results = []
    for article in article_list:
        results.append({
            'title': article.get('title'),
            'author': article.get('author'),
            'source': (article['source'].get('name') if 'source' in article else None),
            'description': article.get('description') ,
            'url': article.get('url'),
            'imageurl' : article.get('urlToImage'),
            'published' : article.get('publishedAt'),
            'content' : article.get('content')
        })
        for field in results[-1]:
            if(results[-1][field] == 'null'):
                results[-1][field] = None
    return results
     
def get_attribs_from_sources(source_list) -> Dict[str, str]:
    """
    Function used internally by NewsSource class
    """
    results = []
    for article in source_list:
        results.append({
            'id': article.get('id'),
            'name': article.get('name'),
            'description': article.get('description') ,
            'url': article.get('url'),
            'category' : article.get('category'),
            'language' : article.get('language'),
            'country' : article.get('country')
        })
        for field in results[-1]:
            if(results[-1][field] == 'null'):
                results[-1][field] = None
    return results


class NewsSource:
    """Class representing a newsource"""

    def __init__(self, key : str):
        """
        :param key: NEWS API api key
        """
        self.apikey = key
        self.topHeadlineCache = []
        self.newsSourceCache = {}

    def changeKey(self, newkey : str):
        """
        :param key: NEWS API api key
        """
        self.apikey = newkey

    def getKey(self):
        """
        :return (str): NEWS API api key
        """
        return self.apikey 
    
    
    def searchByKeyWords(self, keywords):
        """
        Searches for articles with a string of comma separated list of keywords
        
        Parameters:
                keywords (str): comma separated list of keywords to search

        Returns:
                results (dict): Dictionary containing the result of the search query
                    self.topHeadlineCache['status'] (str): 'GOOD' if the search was completed successfully, 'BAD' if not

                    self.topHeadlineCache['count'] (int): number of results

                    self.topHeadlineCache['articles'] (list): list of the articles returned by the query. Each entry is a dictionary with the following keys:

                        'title' (str): Title of the article

                        'author' (str): Author(s) of the article

                        'source' (str): Source of Article (ex: 'BBC News')

                        'description' (str): Short description of the article 

                        'url' (str): Link to the article

                        'imageurl' (str): Link to the article's image

                        'published' (str): UTC time of publication (ex: 2022-05-25T14:09:59Z)
                        
                        'content' (str): First 200 characters max of the article's content 

        """



        try:
            x =  json.loads(urllib.request.urlopen("https://newsapi.org/v2/everything?q="+ urllib.parse.quote(keywords)+ "&pageSize=100&apiKey="+self.apikey).read().decode("utf-8"))
            results = []
            if x['status'] == 'ok':
                results = get_attribs_from_articles(x['articles'])
            else: #there was an error at some point
                    return {'status' : 'BAD', 'count' : 0, 'articles': []}
            return {'status': 'GOOD', 'count': len(results), 'articles': results}
        except:
            return  {'status' : 'BAD', 'count' : 0, 'articles': []}
        

    def getArticlesFromSource(self, source_id : str) -> Dict[str, Any]:

        """
        Searches for articles from a specific news source
        
        Parameters:
                source_id (str): id of the news source to search from

        Returns:
                results (dict): Dictionary containing the result of the search query
                    self.topHeadlineCache['status'] (str): 'GOOD' if the search was completed successfully, 'BAD' if not

                    self.topHeadlineCache['count'] (int): number of results

                    self.topHeadlineCache['articles'] (list): list of the articles returned by the query. Each entry is a dictionary with the following keys:

                        'title' (str): Title of the article

                        'author' (str): Author(s) of the article

                        'source' (str): Source of Article (ex: 'BBC News')

                        'description' (str): Short description of the article 

                        'url' (str): Link to the article

                        'imageurl' (str): Link to the article's image

                        'published' (str): UTC time of publication (ex: 2022-05-25T14:09:59Z)
                        
                        'content' (str): First 200 characters max of the article's content 

        """

        try:
            x =  json.loads(urllib.request.urlopen("https://newsapi.org/v2/everything?sources="+ source_id+"&pageSize=100&apiKey="+self.apikey).read().decode("utf-8"))
            results = []
            if x['status'] == 'ok':
                results = get_attribs_from_articles(x['articles'])
            else: #there was an error at some point
                    return {'status' : 'BAD', 'count' : 0, 'articles': []}
            return {'status': 'GOOD', 'count': len(results), 'articles': results}
        except:
            return {'status' : 'BAD', 'count' : 0, 'articles': []}

    
    def getNewsSources(self, category : str = "" , lang : str = "", country : str = "", clear_cache : bool = False):
        """
        Retrieves the possible news sources the NewsSource can pull from and stores them in a cache. 
        The cache is cleared if a new category, lang, or country is requested, or if 'clear_cache' is true
        
        Parameters:
                category (str): The category the news sources are. Use the empty string ("") to get all categories. Possible Values: 'business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology'
                lang (str): The language the news sources are in. Use the empty string ("") to get all languages. Possible Values: 'ar', 'de', 'en', 'es', 'fr', 'he', 'it', 'nl', 'no', 'pt', 'ru', 'sv', 'ud', 'zh'
                country (str): The country the news source is from. Use the empty string ("") to get all countries. Possible Values: 'ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za'
                clear_cache (bool): When true, the cache will be cleared

        Returns:
                results (dict): Dictionary containing the retrieved sources
                    self.topHeadlineCache['status'] (str): 'GOOD' if the operation was completed successfully, 'BAD' if not

                    self.topHeadlineCache['count'] (int): number of sources

                    self.topHeadlineCache['articles'] (list): list of sources. Each entry is a dictionary with the following keys:

                        'id' (str): ID of the news source

                        'name' (str): Name of the news source

                        'description' (str): Short description of the news source

                        'url' (str): Link to the news source

                        'category' (str): Category of the news source

                        'language' (str): Language of the news source

                        'country' (str): Country of the news source
                        
        """
        if (self.newsSourceCache.get('category') == category and 
            self.newsSourceCache.get('lang') == lang and 
            self.newsSourceCache.get('country') == country and
            clear_cache == False):
            if(self.newsSourceCache.get('sources') != None):
                return self.newsSourceCache['sources']

        

        search_param = ""
        if category != "":
            search_param += 'category='+ category + "&"
        if lang != "":
            search_param += 'language=' + lang + "&"
        if country != "":
            search_param += 'country=' + country + "&"
        try:
            x =  json.loads(urllib.request.urlopen("https://newsapi.org/v2/top-headlines/sources?"+  search_param + "apiKey="+self.apikey).read().decode("utf-8"))
            results = []
            if x['status'] == 'ok':
                results = get_attribs_from_sources(x['sources'])
                self.newsSourceCache['sources'] = results
                self.newsSourceCache['category'] = category
                self.newsSourceCache['lang'] = lang
                self.newsSourceCache['country'] = country
                return {'status': 'GOOD', 'count': len(results), 'sources': results}
            else:
                return {'status' : 'BAD', 'count' : 0, 'sources' : []}
        except:
            return {'status' : 'BAD', 'count' : 0, 'sources' : []}

    def searchByTitle(self, title) -> Dict[str, str] :
        """
        Searches for articles with a specific title
        
        Parameters:
                title (str): title to search for

        Returns:
                results (dict): Dictionary containing the result of the search query
                    self.topHeadlineCache['status'] (str): 'GOOD' if the search was completed successfully, 'BAD' if not

                    self.topHeadlineCache['count'] (int): number of results

                    self.topHeadlineCache['articles'] (list): list of the articles returned by the query. Each entry is a dictionary with the following keys:

                        'title' (str): Title of the article

                        'author' (str): Author(s) of the article

                        'source' (str): Source of Article (ex: 'BBC News')

                        'description' (str): Short description of the article 

                        'url' (str): Link to the article

                        'imageurl' (str): Link to the article's image

                        'published' (str): UTC time of publication (ex: 2022-05-25T14:09:59Z)
                        
                        'content' (str): First 200 characters max of the article's content

        """
        try:
            x =  json.loads(urllib.request.urlopen("https://newsapi.org/v2/everything?q="+ title+ "&searchIn=title&pageSize=100&apiKey="+self.apikey).read().decode("utf-8"))
            results = []
            if x['status'] == 'ok':
                results = get_attribs_from_articles(x['articles'])
            else: #there was an error at some point
                    return {'status' : 'BAD', 'count' : 0, 'articles': []}
            return {'status': 'GOOD', 'count' : len(results), 'articles': results}
        except:
            return {'status' : 'BAD', 'count' : 0, 'articles': []}

    
    def getNumberOfArticles(self, number : int, recompute_cache : bool = False) -> Dict[str , Any]:
        """
        Returns a given amount of top headlines and stores them in a cache. 
        The cache is refilled when 'number' is larger than the size of the current cache, or when 'recompute_cache' is true.
        In the case where 'status' is 'BAD', all the articles which were successfully saved in cache will be returned.


        Parameters:
                number (int): amount of articles to return
                recompute_cache (bool): when true, the cache will be emptied before the query is made

        Returns:
                self.topHeadlineCache (dict): Dictionary containing the result of the search query 
                    self.topHeadlineCache['status'] (str): 'GOOD' if the search was completed successfully, 'BAD' if not

                    self.topHeadlineCache['count'] (int): number of results

                    self.topHeadlineCache['articles'] (list): list of the articles returned by the query. Each entry is a dictionary with the following keys:

                        'title' (str): Title of the article

                        'author' (str): Author(s) of the article

                        'source' (str): Source of Article (ex: 'BBC News')

                        'description' (str): Short description of the article 

                        'url' (str): Link to the article

                        'imageurl' (str): Link to the article's image

                        'published' (str): UTC time of publication (ex: 2022-05-25T14:09:59Z)

                        'content' (str): First 200 characters max of the article's content

        """

        if recompute_cache == True:
            self.topHeadlineCache = []

        #check if enough articles are in the cache
        if number <= len(self.topHeadlineCache):
            return  {'status': 'GOOD', 'count' : number, 'articles':  self.topHeadlineCache[0 : number] }
        
        #if not, reload the entire cache with new articles
        results = []
        for i in range(1, math.ceil(number/100) + 1):
            try:
                x =  json.loads(urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=us&pageSize=100&page="+str(i) +"&apiKey="+self.apikey).read().decode("utf-8"))
                if x['status'] == 'ok':
                    results.extend(get_attribs_from_articles(x['articles']))
                else: #there was an error at some point
                    self.topHeadlineCache = results
                    return {'status' : 'BAD', 'count' : min(number, len(results)), 'articles': self.topHeadlineCache[0 : min(number, len(results))]}
            except:
                self.topHeadlineCache = results
                return {'status' : 'BAD', 'count' : min(number, len(results)), 'articles': self.topHeadlineCache[0 : min(number, len(results))]}
        
        self.topHeadlineCache = results
        return {'status': 'GOOD', 'count' : min(number ,len(self.topHeadlineCache)), 'articles': self.topHeadlineCache[0:min(number ,len(self.topHeadlineCache))]}