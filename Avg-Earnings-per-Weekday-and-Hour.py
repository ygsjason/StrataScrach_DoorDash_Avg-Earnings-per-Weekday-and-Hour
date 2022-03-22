# Import your libraries
import pandas as pd

# Start writing code
df = doordash_delivery

df['day_of_week'] = df['customer_placed_order_datetime'].dt.weekday+1

df['hours'] = df['customer_placed_order_datetime'].dt.hour

#df.groupby('day_of_week')['hours','order_total'].apply(lambda x: x.order_total.sum()/x.hours.sum()).reset_index(name = 'rate')

df.groupby(by = ['day_of_week', 'hours'], as_index = False).agg({'order_total': 'mean'})
