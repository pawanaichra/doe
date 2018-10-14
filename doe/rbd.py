import pandas as pd
class rbd():
	def __init__(self, file_name):
		dataset = pd.read_csv(file_name, sep=', ', delimiter=None)