import pandas as pd


#----------------------------------------------------------#
#Appending all the items in the excel column to a python list for summer_avoid
#Output: A python list of all the ingredients to prefer in summer
summer_prefer_list = []
summer_avoid_list = []

def ingredients():

	df = pd.read_excel(r'summer2.xlsx')


	summer_prefer_column = pd.DataFrame(df, columns=['prefer_in_summer'])
	summer_prefer_list = summer_prefer_column['prefer_in_summer'].tolist()
	summer_prefer_list = [i.replace('\xa0 ','') for i in summer_prefer_list]
	summer_prefer_list_lower = []
	for i in summer_prefer_list:
		i = i.lower()
		summer_prefer_list_lower.append(i)    
	summer_prefer_list = summer_prefer_list_lower
	# FO: 
	# print("\n\nThe python list of ingredients to prefer in summer:")
	(summer_prefer_list).sort()
	# print(summer_prefer_list)



	#----------------------------------------------------------#
	#Appending all the items in the excel column to a python list for summer_avoid
	#Output: A python list of all the ingredients to avoid in summer

	summer_avoid_column = pd.DataFrame(df, columns=['avoid_in_summer'])
	summer_avoid_list = summer_avoid_column['avoid_in_summer'].tolist()
	summer_avoid_list_lower = []
	for i in summer_avoid_list:
		if not type(i) == float:
			i = i.lower()
			summer_avoid_list_lower.append(i)    
	summer_avoid_list = summer_avoid_list_lower
	summer_avoid_list.sort()
# FO: 
# print("\n\nThe python list of ingredients to avoid in summer:")
# print(summer_avoid_list)











