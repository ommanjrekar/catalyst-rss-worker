# Project title
catalyst-rss-worker

# Description : 
Goal of the worker will be to check the following RSS sources for new content periodically (every 15 mins) 

https://www.indiatoday.in/rss/1206514 
https://www.indiatoday.in/rss/1206614 
https://www.indiatoday.in/rss/1206584 
https://www.indiatoday.in/rss/1206513 
https://www.indiatoday.in/rss/1206577 
https://feeds.feedburner.com/ndtvnews-top-stories 
https://feeds.feedburner.com/ndtvnews-latest 
https://feeds.feedburner.com/ndtvnews-india-news 
https://feeds.feedburner.com/ndtvnews-world-news 
https://feeds.feedburner.com/ndtvprofit-latest 

# To start celery 
celery -A catalyst_rss_worker worker -l info -B

# To start Redis
redis-server

# To start Flower
celery flower --broker=redis://localhost:6379

