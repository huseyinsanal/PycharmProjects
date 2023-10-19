import time


print("This is the start of the program.")
start_time = time.time()

time.sleep(5)

end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

print("This is the end of the program.")