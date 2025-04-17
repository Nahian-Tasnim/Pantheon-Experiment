import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path, sep='\t')

low_latency_file_cubic = 'cubic low latency.txt'
high_latency_file_cubic = 'cubic high latency.txt'
low_latency_file_bbr = 'bbr low latency.txt'
high_latency_file_bbr = 'bbr high latency.txt'
low_latency_file_vegas = 'vegas low latency.txt'
high_latency_file_vegas = 'vegas high latency.txt'

data = {
    'Cubic Low': load_data(low_latency_file_cubic),
    'Cubic High': load_data(high_latency_file_cubic),
    'BBR Low': load_data(low_latency_file_bbr),
    'BBR High': load_data(high_latency_file_bbr),
    'Vegas Low': load_data(low_latency_file_vegas),
    'Vegas High': load_data(high_latency_file_vegas),
}

# Time-series throughput
plt.figure(figsize=(10, 6))
for label, df in data.items():
    plt.plot(df['time'], df['throughput_mbps'], label=label)
plt.xlabel('Time (s)')
plt.ylabel('Throughput (Mbps)')
plt.title('Time-series Throughput (Ramp-up Behavior)')
plt.legend()
plt.grid(True)
plt.savefig('time_series_throughput.png')
plt.close()

# Time-series loss rate
plt.figure(figsize=(10, 6))
for label, df in data.items():
    plt.plot(df['time'], df['loss_rate'], label=label)
plt.xlabel('Time (s)')
plt.ylabel('Loss Rate')
plt.title('Time-series Loss Rate')
plt.legend()
plt.grid(True)
plt.savefig('time_series_loss.png')
plt.close()

# Average RTT
bar_width = 0.2
labels = ['Low Latency', 'High Latency']
index = np.arange(len(labels))

avg_rtt_cubic = [data['Cubic Low']['rtt_ms'].mean(), data['Cubic High']['rtt_ms'].mean()]
avg_rtt_bbr = [data['BBR Low']['rtt_ms'].mean(), data['BBR High']['rtt_ms'].mean()]
avg_rtt_vegas = [data['Vegas Low']['rtt_ms'].mean(), data['Vegas High']['rtt_ms'].mean()]

plt.figure(figsize=(10, 6))
plt.bar(index - bar_width, avg_rtt_cubic, bar_width, label='Cubic')
plt.bar(index, avg_rtt_bbr, bar_width, label='BBR')
plt.bar(index + bar_width, avg_rtt_vegas, bar_width, label='Vegas')
plt.xlabel('Latency Scenario')
plt.ylabel('Average RTT (ms)')
plt.title('Average RTT Across Test Scenarios')
plt.xticks(index, labels)
plt.legend()
plt.savefig('average_rtt.png')
plt.close()

# 95th-percentile RTT
percentile_rtt_cubic = [np.percentile(data['Cubic Low']['rtt_ms'], 95), np.percentile(data['Cubic High']['rtt_ms'], 95)]
percentile_rtt_bbr = [np.percentile(data['BBR Low']['rtt_ms'], 95), np.percentile(data['BBR High']['rtt_ms'], 95)]
percentile_rtt_vegas = [np.percentile(data['Vegas Low']['rtt_ms'], 95), np.percentile(data['Vegas High']['rtt_ms'], 95)]

plt.figure(figsize=(10, 6))
plt.bar(index - bar_width, percentile_rtt_cubic, bar_width, label='Cubic')
plt.bar(index, percentile_rtt_bbr, bar_width, label='BBR')
plt.bar(index + bar_width, percentile_rtt_vegas, bar_width, label='Vegas')
plt.xlabel('Latency Scenario')
plt.ylabel('95th Percentile RTT (ms)')
plt.title('95th Percentile RTT Across Test Scenarios')
plt.xticks(index, labels)
plt.legend()
plt.savefig('percentile_rtt.png')
plt.close()

# RTT vs Throughput
plt.figure(figsize=(10, 6))

colors = {
    'Cubic Low': 'blue',
    'Cubic High': 'blue',
    'BBR Low': 'green',
    'BBR High': 'green',
    'Vegas Low': 'red',
    'Vegas High': 'red'
}

markers = {
    'Low': 'o',
    'High': 's'
}

for label, df in data.items():
    avg_rtt = df['rtt_ms'].mean()
    avg_throughput = df['throughput_mbps'].mean()
    scheme, latency = label.split()
    plt.scatter(avg_rtt, avg_throughput, label=label, color=colors[label], marker=markers[latency], s=100)

plt.xlabel('Average RTT (ms)')
plt.ylabel('Average Throughput (Mbps)')
plt.title('RTT vs Throughput (Higher RTT on Left)')
plt.gca().invert_xaxis()  # Invert x-axis so higher RTT is closer to origin
plt.grid(True)
plt.legend()
plt.savefig('rtt_vs_throughput.png')
plt.close()