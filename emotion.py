from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, SentimentOptions, EmotionOptions
import json
from PyLyrics import *
import matplotlib.pyplot as plt
import numpy as np
import warnings

class Emotion:
	
	def get_emotion(self, song, artist):
		warnings.filterwarnings('ignore')
		natural_language_understanding = NaturalLanguageUnderstandingV1(version = '2017-02-27', username = "***REMOVED***", password = "***REMOVED***")
		response = natural_language_understanding.analyze(text=PyLyrics.getLyrics(artist, song), features=Features(emotion=EmotionOptions(), sentiment = SentimentOptions()))
		return response.get('emotion').get('document').get('emotion')
	
	def get_sentiment(self, song, artist):
		warnings.filterwarnings('ignore')
		natural_language_understanding = NaturalLanguageUnderstandingV1(version = '2017-02-27', username = "***REMOVED***", password = "***REMOVED***")
		response = natural_language_understanding.analyze(text=PyLyrics.getLyrics(artist, song), features=Features(emotion=EmotionOptions(), sentiment = SentimentOptions()))
		return response.get('sentiment').get('document').get('score')