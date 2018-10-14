import pandas as pd
import numpy as np
import scipy.stats
from prettytable import PrettyTable
class crd():
	def __init__(self, file_name, alpha=0.05):
		dataset = pd.read_csv(file_name)
		data = dataset.iloc[:,:].values
		data = data.astype(np.float)
		self.no_of_treatments = np.size(data, 1)
		self.repications = np.size(data, 0)
		sum = np.sum(data)
		bias = sum*sum/(self.no_of_treatments*self.repications)
		self.ss_total = np.sum(np.square(data))-bias
		self.ss_treatments = np.sum(np.square(np.sum(data, axis=0)))/self.repications-bias
		self.ss_error = self.ss_total - self.ss_treatments
		self.df_total = self.no_of_treatments*self.repications-1
		self.df_treatments = self.no_of_treatments - 1
		self.df_error = self.no_of_treatments*self.repications - self.no_of_treatments
		self.ms_treatments = self.ss_treatments/self.df_treatments
		self.ms_error = self.ss_error/self.df_error
		self.F = self.ms_treatments/self.ms_error
		self.p_value = 1-scipy.stats.f.cdf(self.F, dfn=self.df_treatments, dfd=self.df_error)
	def print(self):
		x = PrettyTable()
		x.field_names = ["Source of Variation", "Sum of squares", "Degrees of Freedom", "Mean Square", "F", "p value"]
		x.add_row(["Treatments", self.ss_treatments, self.df_treatments, self.ms_treatments, self.F, self.p_value])
		x.add_row(["Error", self.ss_error, self.df_error, self.ms_error, " ", " "])
		x.add_row(["Total", self.ss_total, self.df_total, " ", " ", " "])
		print(x)
