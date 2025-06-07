import numpy as np

temps = np.array([33.5, 36.1, 34.0, 37.8, 32.2, 38.0, 35.5])

# 2. Find max, min, and average temperature
max_temp = np.max(temps)
min_temp = np.min(temps)
avg_temp = np.mean(temps)

# 3. Check how many days were hotter than 35°C
hot_days = np.sum(temps >35)

# Output results
print(f"Maximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")
print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Number of days hotter than 35°C: {hot_days}")


