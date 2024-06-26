import pandas as pd
import utils
utils.start(__file__)



orders = pd.read_csv('../input/orders.csv.gz', usecols=['order_hour_of_day'])

orders.sort_values('order_hour_of_day', inplace=True)
orders.drop_duplicates(inplace=True)
orders.reset_index(drop=True, inplace=True)

def timezone(s):
    if s < 6:
        return 'midnight'
    elif s < 12:
        return 'morning'
    elif s < 18:
        return 'noon'
    else:
        return 'night'


orders['timezone'] = orders.order_hour_of_day.map(timezone)

orders.to_pickle('../input/mk/timezone.p')




utils.end(__file__)
