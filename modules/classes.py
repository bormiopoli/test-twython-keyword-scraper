from modules.process import process_tweet
from twython import TwythonStreamer
import itertools
from operator import itemgetter


class MyStreamer(TwythonStreamer):
    """
    This class extends the TwythonStreamer class by adding a counter to the
    received messages and by modifying the processing of retrieved data
    """

    #MESSAGE COUNTER
    results = 0
    processed_tweets = []

    # Parse the received data and increment parsed results counter
    def on_success(self, data):
        """
        This function process the successfully retrieved tweets, introduces a counter and limit
        the number of received tweets to a specified integer limit. In case more number are parsed,
        the client is disconnected.
        :param data:
        :return: None
        """
        tweet_parsed_data = process_tweet(data)

        #CONDITION TO CHECK NUMBER OF MESSAGES DID NOT REACH 100
        if self.results < 100:

            self.append_tweets(tweet_parsed_data)
            #INCREMENT OF MESSAGE COUNTER
            self.results += 1
            return

        else:
            self.disconnect()
            return

    # Disconnect the client in case of problem with the API or in case of Timeout
    def on_error(self, status_code, data, header=None):
        """
        This function disconnect the client in case an error arises during the parsing operation
        :param status_code: integer
        :param data: dict
        :param header: None
        :return: None
        """
        print(status_code, data)
        self.disconnect()
        return

    def append_tweets(self, parsed_tweet):
        """
        This function appends to the class instance each processed tweet
        :param parsed_tweet: dict
        :return: None
        """
        self.processed_tweets.append(parsed_tweet)
        return

    def order_tweets(self, grouped_tweets):
        """
        This function orders the tweets per each user in an ascending order per time of arrival.
        The function takes as input the list of dictionaries already ordered per user and proceed
        to order each message and return a generator of ordered user dictionaries with ordered messages
        :param grouped_tweets: list
        :return: list
        """
        for el in grouped_tweets:
            new_dict = {[*el][0]: []}
            for dictionary in el.values().__iter__():
                dictionary.sort(key=itemgetter("messagedate"))
                for key, group in itertools.groupby(dictionary, lambda item: item["messagedate"]):
                    [new_dict.get([*el][0]).append(
                        {"time": item['time'], "messagedate": item['messagedate'], "messagedata": item["messagedata"],
                         "authorname": item["authorname"], "authordate": item["authordate"], "authorscreen": item["authorscreen"]})for item in group
                    ]

            yield new_dict

    def groupby_author(self):
        """
        This function group by the parsed tweets contained in the processed_tweets list of the same class instance,
        also ordering them per authordate, returning the list of grouped tweets ordered per user chronologically
        :return: list
        """
        grouped_tweets = []
        self.processed_tweets.sort(key=itemgetter("authordate"))
        for key, group in itertools.groupby(self.processed_tweets, lambda item: item["authorid"]):
            grouped_tweets.append({key: [{"time": item['time'], "messagedate": item['messagedate'], "messagedata": item["messagedata"],
                         "authorname": item["authorname"], "authordate": item["authordate"], "authorscreen": item["authorscreen"]} for item in group]})
        return grouped_tweets
