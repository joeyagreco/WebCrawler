from Crawler import Crawler
from collections import Counter

class Weigher:

    def __init__ (self, url):

        self.__crawler = Crawler(url)
        # tags we are looking for and the weight we will give them
        self.__weightMultipliers = {"h1":3, "h2":2, "p":1}
        self.__weightedDicts = self.__getAllWeightedDicts()
        self.__weightedTags = self.__mergeWeightedDicts()


    def __getWeightsForTagType(self, tagType):
        """ This returns a dictionary of how many times a tag appears for self.__crawler at the given tag
            Tag type examples: "p", "h1", "h2"..."""

        # get the multiplier for this specific type of tag
        multiplier = self.__weightMultipliers[tagType]
        # get the list of tags from the crawler
        pTags = self.__crawler.getTagList(tagType)
        # make the list of tags a dictionary that holds the count of each tag by using Counter
        pTags = Counter(pTags)
        # apply the multiplier
        for pTag in pTags:
            pTags[pTag] *= multiplier
        return pTags

    def __getAllWeightedDicts(self):
        """ This returns a list of dictionaries containing the tags and weighted values to self.__weightedDicts
            It will create a weighted dictionary for every key in self.__weightMultipliers """

        # this will hold the all weighted dictionaries
        weightedDicts = []

        for key in self.__weightMultipliers:
            print(f"Creating a weighted dict for {key} tag...")
            weightedDicts.append(self.__getWeightsForTagType(key))

        return weightedDicts

    def __mergeWeightedDicts(self):
        """ This merges all the dictionaries in self.__weightedDicts """

        # this dictionary will be what all dictionaries will be merged into
        masterDict = {}

        # merge the dictionary into masterDict
        for weightedDict in self.__weightedDicts:
            masterDict.update(weightedDict)

        # return masterDict sorted and in descending order
        return {k: v for k, v in sorted(masterDict.items(), key=lambda item: item[1], reverse=True)}

    def getWeightedTags(self):
        return self.__weightedTags





if __name__ == "__main__":
    w = Weigher("https://stackoverflow.com/questions/37381999/iterate-through-a-dictionary-in-reverse-order-python")
    print(w.getWeightedTags())
