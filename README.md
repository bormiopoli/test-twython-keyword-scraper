# Python tweets by keywords using Twython #
An implementation of Twython library that retrieves tweets with specific keywords and order them per timestamp after grouping them by user ID 

## Task ##

This small program covers the functionality explained below and provide us with the source, instructions to build and run the appliocation  as well as a sample output of an execution:

+ Connect to the [Twitter Streaming API](https://dev.twitter.com/streaming/overview)
    * Use the following values:
        + Consumer Key: `RLSrphihyR4G2UxvA0XBkLAdl`
        + Consumer Secret: `FTz2KcP1y3pcLw0XXMX5Jy3GTobqUweITIFy4QefullmpPnKm4`
    * The app name will be `Python-exercise`
    * You will need to login with Twitter
+ Filter messages that track on "bieber"
+ Retrieve the incoming messages for 30 seconds or up to 100 messages, whichever comes first
+ Your application should return the messages grouped by user (users sorted chronologically, ascending)
+ The messages per user should also be sorted chronologically, ascending
+ For each message, we will need the following:
    * The message ID
    * The creation date of the message as epoch value
    * The text of the message
    * The author of the message
+ For each author, we will need the following:
    * The user ID
    * The creation date of the user as epoch value
    * The name of the user
    * The screen name of the user
+ All the above infomation is provided in either SDTOUT or a log file
+ You are free to choose the output format, provided that it makes it easy to parse and process by a machine

## How to run it ##

The file main.py requires the definition of the credentials (consumer key, consumer token, access token and access secret) inside the file "twitter_credentials.json", located inside the folder "modules".
The file that must be named "twitter_credentials.json" is not supposed to be versioned and must be updated, via the following format:

{"credentials" : {
  "CONSUMER_KEY" : "key_value",
  "CONSUMER_SECRET" : "secret_value",
  "ACCESS_TOKEN" : "access_token_value",
  "ACCESS_SECRET" : "access_secret_value"}
}

To execute the program is only needed to run the file main.py via a python 3 interpreter.
The modules necessary for its execution can be installed via "pip3 install requirements.txt" on the same folder level where the txt file is.
To keep track of the statistic of messages received per seconds, and among different run of the application, the rate of message arrival (eg. messages/second) is saved in the file "message_per_second", located at the same level of the main.py file.

## Using Docker ##
Create/update the credentials of the file "twitter_credentials.json".
Go via the terminal window to the location of where the Dockerfile is located.
Run "docker build . -t myapp". Wait the image is created and then run "docker run myapp".
PS. Note that in case the application is run via Docker, the stats per second will not be show