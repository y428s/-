math = float(input(" MT score:"))
sc = float(input("SC score:"))
geo = float(input("GEO score:"))
ch = float(input("CH score:"))
bm = float(input("BM score:"))
eng = float(input("ENG score:"))
his = float(input("HIS score:"))
art = float(input("art score:"))
compu = float(input("电脑 score:"))
conse = float(input("辅导 score:"))
Pe = float(input("PE score:"))
CO = float(input("联课 score:"))

al = ch * 7 + bm * 7 +eng * 7 + math * 7 + his * 3 + geo * 3 + art * 1 + compu * 2 + conse * 1 + Pe * 2 + CO * 2 + sc * 6
total = al / 48

print('你需要计算下半年的总平均吗？(写数字就好)')
print('1)需要')
print('2)不需要')

answer = int(input("答案:"))

if answer == 1:
    totalup = float(input("上半年的成绩: "))
    allcombine = (total + totalup) / 2
    print('你的最终总平均:'+ str(allcombine))

elif answer == 2:
    print(total)

else:
    print("错误数字")



