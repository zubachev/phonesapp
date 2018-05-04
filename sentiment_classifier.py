__author__ = 'zubachev_dmitry'
import pickle

class SentimentClassifier(object):
	def __init__(self):
		with open('./LogisticUnigramUnprocessedTextSentiment.pkl', 'rb') as f:
			self.model = pickle.load(f)
		with open('./UnigramUnprocessedVectorizer.pkl', 'rb') as f:
			self.vectorizer = pickle.load(f)
		self.classes_dict = {0: u"негативный", 1: u"позитивный", -1: u"ошибка прогноза"}

	@staticmethod
	def get_probability_words(probability):
		if probability < 0.55:
			return u"нейтральный или неточный"
		if probability < 0.71:
			return u"скорее всего"
		if probability > 0.95:
			return u"точно"
		else:
			return ""

	def predict_text(self, text):
		try:
			vectorized = self.vectorizer.transform([text])
			return self.model.predict(vectorized)[0],\
				self.model.predict_proba(vectorized)[0].max()
		except:
			print (u"ошибка прогноза")
			return -1, 0.8

	def predict_list(self, list_of_texts):
		try:
			vectorized = self.vectorizer.transform(list_of_texts)
			return self.model.predict(vectorized),\
				self.model.predict_proba(vectorized)
		except:
			print (u"ошибка прогноза")
			return None

	def get_prediction_message(self, text):
		if text == '':
			return ''
		prediction = self.predict_text(text)
		class_prediction = prediction[0]
		prediction_probability = prediction[1]
		if (prediction_probability > 0.65) and (prediction_probability < 0.71):
			class_prediction = 0
		return self.get_probability_words(prediction_probability) + " " + self.classes_dict[class_prediction]