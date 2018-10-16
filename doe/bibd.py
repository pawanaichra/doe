import pandas as pd
import numpy as np
import scipy.stats
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
class bibd():
	def __init__(self, file_name, alpha=0.05):
		dataset = pd.read_csv(file_name)
		missing=dataset.isna().sum(axis = 1)[0]
		data = dataset.iloc[:,1:].values
		data = data.astype(np.float)
		self.no_of_treatments = np.size(data, 1)
		self.blocks = np.size(data, 0)
		k=self.no_of_treatments-missing
		sum = np.nansum(data)
		N=self.blocks*k
		r=N/self.no_of_treatments
		lambd = r*(k-1)/(self.no_of_treatments-1)
		bias = sum*sum/(N)
		self.ss_total = np.nansum(np.square(data))-bias
		self.ss_blocks = np.nansum(np.square(np.nansum(data, axis=1)))/k-bias
		self.ss_treatments=0
		for i in range(self.no_of_treatments):
			temp=np.nansum(data, axis=0)[i]
			for j in range(self.blocks):
				if not (np.isnan(data[j][i])):
					temp-=(np.nansum(data, axis=1)[j])/k
			self.ss_treatments+=temp*temp
		self.ss_treatments=self.ss_treatments*k/(lambd*self.no_of_treatments)
		self.ss_error = self.ss_total - self.ss_blocks - self.ss_treatments
		self.df_total = N-1
		self.df_treatments = self.no_of_treatments - 1
		self.df_blocks=self.blocks-1
		self.df_error = self.df_total - self.df_treatments - self.df_blocks
		self.ms_treatments = self.ss_treatments/self.df_treatments
		self.ms_blocks = self.ss_blocks/self.df_blocks
		self.ms_error = self.ss_error/self.df_error
		self.F_treatments = self.ms_treatments/self.ms_error
		self.F_blocks = self.ms_blocks/self.ms_error
		self.p_value_treatments = 1-scipy.stats.f.cdf(self.F_treatments, dfn=self.df_treatments, dfd=self.df_error)
		self.p_value_blocks = 1-scipy.stats.f.cdf(self.F_blocks, dfn=self.df_blocks, dfd=self.df_error)
		self.x = PrettyTable()
		self.x.set_style(MSWORD_FRIENDLY)
		self.x.field_names = ["Source of Variation", "Sum of squares", "Degrees of Freedom", "Mean Square", "F", "p value"]
		self.x.float_format["Sum of squares"] = ' 10.2'
		self.x.float_format["Mean Square"] = ' 10.2'
		self.x.float_format["F"] = ' 10.2'
		self.x.float_format["p value"] = ' 10.4'
		self.x.add_row(["Treatments", self.ss_treatments, self.df_treatments, self.ms_treatments, self.F_treatments, self.p_value_treatments])
		self.x.add_row(["Blocks", self.ss_blocks, self.df_blocks, self.ms_blocks, self.F_blocks, self.p_value_blocks])
		self.x.add_row(["Error", self.ss_error, self.df_error, self.ms_error, " ", " "])
		self.x.add_row(["Total", self.ss_total, self.df_total, " ", " ", " "])
	def print(self):
		print(self.x)
	def export(self):
		with open('result.csv', 'w') as csvFile:
			csvFile.write(self.x.get_string())
