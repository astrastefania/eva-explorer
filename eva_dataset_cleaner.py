""" Cleaning EVA dataset
    source: https://data.nasa.gov/Raw-Data/Extra-vehicular-Activity-EVA-US-and-Russia/9kcy-zwvn
    Extra-vehicular Activity (EVA) - US and Russia
    Activities done by an astronaut or cosmonaut outside a spacecraft beyond the Earth's appreciable atmosphere.
"""

import pandas as pd 
from duration import to_seconds as tomin
import dateparser


def to_min(hmm):
	""" Convert the time from h:mm to the total of minutes"""
	try: 
		return tomin(hmm) 
	except (ValueError, TypeError): 
		return 0


def to_date(datestr):
	""" Convert Date string in DateTime type """
	try: 
		return dateparser.parse(datestr)
	except (Exception) as e: 
		print(e, datestr)


def eva_dataset_cleaner(df):
	df['Duration'] = df['Duration'].apply(to_min)
	df['Date'] = df['Date'].apply(to_date)


if __name__ == '__main__':
	df = pd.read_csv('Extra-vehicular_Activity__EVA__-_US_and_Russia.csv')
	eva_dataset_cleaner(df)
	df.to_csv('Extra-vehicular_Activity__EVA__-_US_and_Russia_clean.csv')









