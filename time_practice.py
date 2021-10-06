import time

# 1970/1/1 秒数が表示
print(time.time())

# 1633486047.6119099


print(time.time() / (60*60*24*365))

# 51.79750277815687


def fib(n):
	if n < 2:
		return n
	else:
		return fib(n-1) + fib(n-2)



before = time.time()
print(fib(30))
after = time.time()
print(f"recursive fibonacci took {after - before:.2f} sec.")

# 832040
# recursive fibonacci took 0.31 sec.


#  今のローカル時間を文字列で返す
print(time.ctime())

# Wed Oct  6 11:10:10 2021


#.localtime() 構造化データで返す
localtime = time.localtime()
print(localtime)

# time.struct_time(tm_year=2021, tm_mon=10, tm_mday=6, tm_hour=11, tm_min=10, tm_sec=49, tm_wday=2, tm_yday=279, tm_isdst=0)

print(f"今の時刻は{localtime.tm_year}年{localtime.tm_mon}月{localtime.tm_mday}日{localtime.tm_hour}時{localtime.tm_min}分です")

# 今の時刻は2021年10月6日11時12分です


# .sleep(secs) secs秒あdけプログラムが待機
# sec = 10
# print(f"{sec}秒待ってください")
# time.sleep(sec)
# print(f"{sec}秒待機しました")

# 10秒待ってください
# 10秒待機しました


def timer(func):
	def inner(*args, **kwargs):
		before = time.time()
		func(*args, **kwargs)
		after = time.time()
		print(f"{func.__name__} took {after - before:.2f} sec.")
	return inner


@timer
def lazy_func(sec):
	print(f"I'm working so hard...")
	time.sleep(sec)
	print(f"I'm finally done!")

lazy_func(4)

# I'm working so hard...
# I'm finally done!
# lazy_func took 4.00 sec.




