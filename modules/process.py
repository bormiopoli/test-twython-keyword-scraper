from time import strptime, mktime, time
import re


def process_tweet(tweet):
    """
    This function parses the result of the API retrieved dictionary structure in accordance with the wanted fields
    :param tweet: dictionary
    :return: tuple
    """
    messageid = extract_messageid(tweet)
    messagedata = re.sub('\s+', ' ', extract_messagedata(tweet)).replace("\n"," ")
    messagedate = extract_messagedate(tweet)
    authorid = extract_authorid(tweet)
    authordate = extract_authordate(tweet)
    authorname = extract_authorname(tweet)
    authorscreen = extract_authorscreen(tweet)
    return {"time": time(), "messageid": messageid, "messagedata": messagedata, "messagedate": messagedate, "authorid": authorid,
            "authordate": authordate, "authorname": authorname, "authorscreen": authorscreen}


def extract_messageid(data):
    """
    This function parse the ID of the messsage from the data incoming dictionary
    :param data: dict
    :return: integer
    """
    return data['id']


def extract_messagedata(data):
    """
    This function parse the text of the message from the data incoming dictionary
    :param data: dict
    :return: string
    """
    return data['text']


def extract_messagedate(data):
    """
    This function extract the date of the message from the data incoming dictionary and convert it into epoch value
    :param data: dict
    :return: float
    """
    asctime_string = data['created_at'].split(" ")[0:4] + data['created_at'].split(" ")[5:]
    struct_time = strptime(' '.join(asctime_string))
    epoch_time = mktime(struct_time)
    return epoch_time


def extract_authorid(data):
    """
    This function extract the author ID from the data incoming dictionary
    :param data: dict
    :return: integer
    """
    return data['user']['id']


def extract_authordate(data):
    """
    This function extract the data of the author creation and convert it in epoch value
    :param data: dict
    :return: float
    """
    asctime_string = data['user']['created_at'].split(" ")[0:4] + data['user']['created_at'].split(" ")[5:]
    struct_time = strptime(' '.join(asctime_string))
    epoch_time = mktime(struct_time)
    return epoch_time


def extract_authorname(data):
    """
    This function extract the name of the author from the incoming data dictionary
    :param data: dict
    :return: string
    """
    return  data['user']['name']


def extract_authorscreen(data):
    """
    This function extract the screen_name of the author from the incoming data dictionary
    :param data: dict
    :return: string
    """
    return data['user']['screen_name']