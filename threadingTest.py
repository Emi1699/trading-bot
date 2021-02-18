import time
import threading
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
	print(f"sleeping {seconds} second(s)...")
	time.sleep(seconds)
	# print("done sleeping...")

	return "done sleeping..."

def alwaysLoop():
	while True:
		print(1)
		time.sleep(1)


#return results objects in the order they finish
# with concurrent.futures.ThreadPoolExecutor() as executor:
# 	secs = [5, 4, 3, 2, 1]
# 	results = [executor.submit(do_something, sec) for sec in secs]

# 	for f in concurrent.futures.as_completed(results):
# 		print(f.result())



#returns results in the order they were called
#also waits for threads to finish execution
with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [5, 4, 3, 2, 1]
	results = executor.map(do_something, secs)

	for results in results:
		print(results)

# threads = []
# for _ in range(10):
# 	t = threading.Thread(target = do_something, args = [1.5])
# 	t.start()
# 	threads.append(t)

#wait for threads to finishe execution before going to the next instruction
# for thread in threads:
# 	thread.join()


finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
