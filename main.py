from modules.classes import MyStreamer
from modules.auth import openfile
import threading
import os
from sys import stdout
import time
import json


# def mytimer():
#     """
#     This function is used to time limit the thread execution involving the Twitter client.
#     This function has been created due to limitations of the request.Session(), whose timeout referred to each request
#     and not to the creation of cookies for all sessions. After the session is timeout, the client is disconnected.
#     :return: None
#     """
#     stream.disconnect()


if __name__ == '__main__':
    key, secret, acc_token, acc_secret = openfile(path=os.path.join(os.path.dirname(__file__),
                                                                    'modules', 'twitter-credentials.json'))
    stream = MyStreamer(key, secret,
                        acc_token, acc_secret, timeout=20)

    try:
        with open("message_per_second", "r") as fr:
            rate = float(fr.read().replace(" ", ""))
    except Exception as ex:
        print("May be the first execution - File for stats per second not found - Error {}".format(ex))
        rate = 0

    # my_timer = threading.Timer(30, mytimer)
    # my_timer.start()
    # start_time = time.time()
    stream.statuses.filter(track='bieber')

    # if my_timer.is_alive():
    #     elapsed_time = time.time() - start_time
    # else:
    #     elapsed_time = 30

    # my_timer.cancel()
    # FINAL PROCESSING OF RETRIEVED TWEETS
    grouped_tweets = stream.groupby_author()

    for el in stream.order_tweets(grouped_tweets):
        stdout.write(json.dumps(el) + "\n")

    with open("message_per_second", "w+") as fw:
        # if rate == 0:
        #     rate = stream.results / elapsed_time
        # else:
        #     rate = (stream.results / elapsed_time + rate) / 2
        fw.write("{}".format(rate))
        stdout.write("The message rate is {}".format(rate))
        fw.close()

