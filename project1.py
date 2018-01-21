from pyt import *
import pandas as pd


#-----------------------------------------------------------
#Y-List

def make_y_list():

	sample_quiz_solution = {"Section": ['D','D','C','C','B','B','A','A']}
	df = pd.DataFrame(sample_quiz_solution)
	dummies = pd.get_dummies(df)
	answer_list = dummies.values.tolist()

	return answer_list

#----------------------------------------------------------
#X-List












