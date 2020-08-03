# WebCrawler
Learning how to make a web crawler

**To Do**
__________
- update badTags.json from Search.py


**Known Bugs:**

Crawler.py
__________
- ~~in __mergeWeightedDicts, duplicates are overriden instead of added together (Ex. if a key and value exists in both dicts, it will overwrite one of the values instead of summing them)~~ FIXED


**Possible Updates:**

Crawler.py
__________

- in __splitTags, split strings by more than just space, as sometimes tags are clearly multiple words. Maybe "/", "," etc.
