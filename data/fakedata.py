import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# define number of records and start time
number_records = 1440
start_time = datetime(2024,1,1,0,0,0)

# make timestamps
timestamps = [start_time + timedelta(minutes=i) for i in range(number_records)]

# make fake data for columns
latency = np.random.normal(loc=50, scale=10, size=number_records)
throughput = np.random.normal(loc=100, scale=20, size=number_records)
packet_loss_rate = np.random.uniform(low=0, high=0.1, size=number_records)

# dataframe
df = pd.DataFrame({
    'timestamp': timestamps,
    'latency_ms': latency,
    'throughput_mbps': throughput,
    'packet_loss_rate': packet_loss_rate
})

# save as csv
df.to_csv('network_performance_metrics.csv', index=False)