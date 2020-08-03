# WebCrawler
Learning how to make a web crawler

**Known Bugs:**

Crawler.py
__________
- some tags clearly contain multiple words with no spaces... maybe split by more than just " " ?
- ~~in __mergeWeightedDicts, duplicates are overriden instead of added together (Ex. if a key and value exists in both dicts, it will overwrite one of the values instead of summing them)~~ FIXED

**Possible Updates:**

Crawler.py
__________

- in __splitTags, split strings by more than just space, as sometimes tags are clearly multiple words. Maybe "/", "," etc.
