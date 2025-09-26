python的dic怎用
ChatGPT 說：

很好問題 👍！
Python 的 dict（字典） 是一種 鍵值對 (key-value pair) 的資料結構。它跟真實世界的「字典」很像：透過 key 找到對應的 value。

1. 建立字典
# 建立空字典
my_dict = {}

# 建立有內容的字典
person = {
    "name": "Sam",
    "age": 25,
    "city": "Taipei"
}

2. 取值
print(person["name"])   # Sam
print(person["age"])    # 25

# 用 get，比較安全 (避免 key 不存在時出錯)
print(person.get("city"))       # Taipei
print(person.get("country"))    # None (因為沒有這個 key)

3. 新增 / 修改
person["job"] = "Engineer"   # 新增 key-value
person["age"] = 26           # 修改 value
print(person)
# {'name': 'Sam', 'age': 26, 'city': 'Taipei', 'job': 'Engineer'}

4. 刪除
del person["city"]       # 刪掉 city
print(person)

removed = person.pop("job")   # pop 會回傳被刪掉的值
print(removed)  # Engineer

5. 遍歷 (loop)
for key in person:
    print(key, person[key])   # 逐一取出 key 與 value

for key, value in person.items():
    print(key, "=>", value)

for value in person.values():
    print(value)

6. 常用操作
print(len(person))   # 字典有多少個 key
print("name" in person)  # True，檢查是否有這個 key
print(person.keys())     # 所有 key
print(person.values())   # 所有 value
print(person.items())    # 所有 (key, value) 配對