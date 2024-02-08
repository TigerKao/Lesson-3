
data = []
with open("food.txt", "r") as f:  # r 是 read 的意思，as 當作，f # with 是 open 一個檔案，並且在結尾的時候自動 close
    for line in f: # 調用到 f
        data.append(line.strip()) #strip 針對字串將 /n、多餘的空格 去除掉
        
print(data)