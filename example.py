from datetime import datetime, timedelta

# Create two time objects
time1 = datetime.strptime("09:30:00", "%H:%M:%S")
time2 = datetime.strptime("09:15:00", "%H:%M:%S")

# Addition
result_sum = time1 + timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
#print("Sum:", result_sum.time())  # Output: Sum: 11:45:00

# Subtraction
result_diff = time1 - timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)
#print("Difference:", result_diff.time())  # Output: Difference: 07:15:00

print(time1)