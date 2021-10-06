import re

# Regular Expression (正規表現)

email = 'email@gmail.com'

print("@" in email)

# True

matched = re.search('@\w+\.', email)
print(matched)

# <re.Match object; span=(5, 12), match='@gmail.'>



noChecked= re.search('@\w+\.', "myemail@wwwcom")
print(noChecked)

# None


#[]
# abcを含む場合一致する
print(re.search('[abc]','a'))

# 数字を含む場合に一致する
print(re.search('[0-9]','2'))

# 最初の文字が数字かどうかを判定
print(re.search('^[0-9]','test2'))

# {}
# {n}回リピート
print(re.search('^[0-9]{4}','2021/02/12'))

# {n, m} 最低n回、最高m回リピート
print(re.search(' ^[0-9]{2, 4','21.fs.132'))

# $
# 最後の文字
print(re.search('[0-9]{2}$','2021/07/21'))

# *
# 左のパターンを０回以上繰り返す
print(re.search('a*b','aaaaab'))

# +
# 左のパターンを1回以上繰り返す
print(re.search('a+b','a'))

# ?
# 左のパターンを０回か１回繰り返す
print(re.search('abc','abbbc'))

# | 
# or
print(re.search('abc|012','012'))

# ()
# グループ
print(re.search('te(s|x)t','test'))

# .
# 任意の１文字
print(re.search('h.t','hat'))

# \
# エスケープ
print(re.search('h\.t','h.t'))

# \w
# [a-zA-Zo-9_] 全てのアルファベット、数字及びアンダースコア
print(re.search('h\wt','h0t'))



# 入力された生年月日が正しいフォーマットを判定
pattern_dob = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[0-1])$"

while True:
	dob = input("生年月日を入力してください(yyyy/mm/dd)")
	result = re.search(pattern_dob, dob)
	if result:
		print(f"{dob}は正しいフォーマットです")
		break
	else:
		print(f"{dob}は正しくないフォーマットです　")




# 入力されたemailが正しいフォーマットを判定
pattern_email = "^(\w|\.|-)+@(\w|\.|-)+\.[a-zA-Z]{2,3}$"

while True:
	email = input("Emailを入力してください")
	result = re.search(pattern_email, email)
	if result:
		print(f"{email}は正しいフォーマットです")
		break
	else:
		print(f"{email}は正しくないフォーマットです　")