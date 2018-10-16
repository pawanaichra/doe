import pandas as pd
import numpy as np
import scipy.stats
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
class latin_square():
	def __init__(self, file_name, alpha=0.05):
		dataset = pd.read_csv(file_name)
		data = dataset.iloc[:,1:].values
		data = data.astype(np.float)
		self.no_of_treatments = np.size(data, 1)
		sum = np.sum(data)
		bias = sum*sum/(self.no_of_treatments*self.no_of_treatments)
		self.ss_total = np.sum(np.square(data))-bias
		self.ss_treatments=-bias;
		for i in range(self.no_of_treatments):
			temp=0;
			for j in range(self.no_of_treatments):
				temp+=data[(2*self.no_of_treatments-(i+j)-1)%self.no_of_treatments, j]
			self.ss_treatments+=temp*temp/self.no_of_treatments
		self.ss_columns = np.sum(np.square(np.sum(data, axis=0)))/self.no_of_treatments-bias
		self.ss_rows = np.sum(np.square(np.sum(data, axis=1)))/self.no_of_treatments-bias
		self.ss_error = self.ss_total - self.ss_treatments - self.ss_columns - self.ss_rows
		self.df_total = self.no_of_treatments*self.no_of_treatments-1
		self.df_treatments = self.no_of_treatments - 1
		self.df_rows = self.no_of_treatments - 1
		self.df_columns = self.no_of_treatments - 1
		self.df_error = self.df_total - self.df_treatments - self.df_columns - self.df_rows
		self.ms_treatments = self.ss_treatments/self.df_treatments
		self.ms_error = self.ss_error/self.df_error
		self.ms_columns = self.ss_columns/self.df_columns
		self.ms_rows = self.ss_rows/self.df_rows
		self.F_treatments = self.ms_treatments/self.ms_error
		self.F_columns = self.ms_columns/self.ms_error
		self.F_rows = self.ms_rows/self.ms_error
		self.p_value_treatments = 1-scipy.stats.f.cdf(self.F_treatments, dfn=self.df_treatments, dfd=self.df_error)
		self.p_value_columns = 1-scipy.stats.f.cdf(self.F_columns, dfn=self.df_treatments, dfd=self.df_error)
		self.p_value_rows = 1-scipy.stats.f.cdf(self.F_rows, dfn=self.df_treatments, dfd=self.df_error)
		self.x = PrettyTable()
		self.x.set_style(MSWORD_FRIENDLY)
		self.x.field_names = ["Source of Variation", "Sum of squares", "Degrees of Freedom", "Mean Square", "F", "p value"]
		self.x.float_format["Sum of squares"] = ' 10.2'
		self.x.float_format["Mean Square"] = ' 10.2'
		self.x.float_format["F"] = ' 10.2'
		self.x.float_format["p value"] = ' 10.4'
		self.x.add_row(["Treatments", self.ss_treatments, self.df_treatments, self.ms_treatments, self.F_treatments, self.p_value_treatments])
		self.x.add_row(["Rows", self.ss_rows, self.df_rows, self.ms_rows, self.F_rows, self.p_value_rows])
		self.x.add_row(["Columns", self.ss_columns, self.df_columns, self.ms_columns, self.F_columns, self.p_value_columns])
		self.x.add_row(["Error", self.ss_error, self.df_error, self.ms_error, " ", " "])
		self.x.add_row(["Total", self.ss_total, self.df_total, " ", " ", " "])
	def print(self):
		print(self.x)
	def export(self):
		with open('result.csv', 'w') as csvFile:
			csvFile.write(self.x.get_string())
