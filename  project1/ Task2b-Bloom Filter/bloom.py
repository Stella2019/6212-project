from pybloom import BloomFilter
import time
start_time=time.time()
bf = BloomFilter(9000000, 0.01)
end_time=time.time()
used_time=end_time-start_time
print(used_time)
with open("/usr/share/dict/words") as f:
    for word in f:
        bf.add(word.rstrip())

print ('apple') in bf