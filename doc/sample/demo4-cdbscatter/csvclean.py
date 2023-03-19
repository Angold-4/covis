import csv
import sys

# Generate JS code to clean the csv file
# Part of this script are generate by Github Compilot

# deal with all the data in the csv file
# !!! must be in the standard format !!!

# specify the two addresses of the csv file or default to the current directory
# first one should be CDB1, second one should be CDB2, third one should be CDB3
# TODO: (current only have CDB1, CDB3)

CDB1 = "CDB1.csv" # Industry
CDB3 = "CDB3.csv" # Stock

if len(sys.argv) == 2:
    CDB1 = str(sys.argv[1])
    CDB3 = str(sys.argv[2])
# hard coded each column name
# choose col0 or col1
col0 = "個股代號／公司名字" # for CDB1
col1 = "行業"               # for CDB3

col2 = "時富雷達 (CR)"
col3 = "基本分析比重"
col4 = "技術分析比重"
col5 = "基本分析分數"
col6 = "技術分析分數"
col7 = "相對強弱指數 RSI（9天）"
col8 = "波幅指數 Volatility（10天）"
col9 = "平均線 SMA（10天）"
col10 = "銷售額增長标准分数"
col11 = "債務股本比例标准分数"
col12 = "淨收入改善标准分数"
col13 = "資本回報标准分数"
col14 = "保留盈餘增長标准分数"
col15 = "TA4"
col16 = "TA5"
col17 = "移動平均線标准分数"
col18 = "相對強弱指數标准分数"
col19 = "布林线指标标准分数"


# quoted column name
col0_ = "'個股代號／公司名字'" # for CDB1
col1_ = "'行業'"               # for CDB3

col2_ = "'時富雷達 (CR)'"
col3_ = "'基本分析比重'"
col4_ = "'技術分析比重'"
col5_ = "'基本分析分數'"
col6_ = "'技術分析分數'"
col7_ = "'相對強弱指數 RSI（9天）'"
col8_ = "'波幅指數 Volatility（10天）'"
col9_ = "'平均線 SMA（10天）'"
col10_ = "'銷售額增長标准分数'"
col11_ = "'債務股本比例标准分数'"
col12_ = "'淨收入改善标准分数'"
col13_ = "'資本回報标准分数'"
col14_ = "'保留盈餘增長标准分数'"
col15_ = "'TA4'"
col16_ = "'TA5'"
col17_ = "'移動平均線标准分数'"
col18_ = "'相對強弱指數标准分数'"
col19_ = "'布林线指标标准分数'"

def roundne(x):
    if x == "#VALUE!" or x == "#DIV/0!" or x == '':
        return ''
    return round(float(x), 5) 

def p2f(x):
    # convert percentage to float
    if x == "#VALUE!" or x == "#DIV/0!" or x == '':
        return ''
    return float(x.strip('%'))/100

def quoted(x):
    # add quotes to the string
    return "'" + x + "'"

"""
Basic logic: Keep the data of each col into memory
and then write them into a JS Float32Array (each col) one time
Even though this code is crap, and very slow,
but it works and it is easy to manage/understand
"""

headers_1 = [col0_, col1_, col2_, col3_, col4_, col5_, col6_, col7_, col8_,
    col9_, col10_, col11_, col12_, col13_, col14_, col15_, col16_, col17_, col18_, col19_]
headers_3 = [col0_, col1_, col2_, col3_, col4_, col5_, col6_, col7_, col8_,
    col9_, col10_, col11_, col12_, col13_, col14_, col15_, col16_, col17_, col18_, col19_]

# CDB1 data
col1_data_1 = []
col2_data_1 = []
col3_data_1 = []
col4_data_1 = []
col5_data_1 = []
col6_data_1 = []
col7_data_1 = []
col8_data_1 = []
col9_data_1 = []
col10_data_1 = []
col11_data_1 = []
col12_data_1 = []
col13_data_1 = []
col14_data_1 = []
col15_data_1 = []
col16_data_1 = []
col17_data_1 = []
col18_data_1 = []
col19_data_1 = []

# CDB3 data
col1_data_3 = []
col2_data_3 = []
col3_data_3 = []
col4_data_3 = []
col5_data_3 = []
col6_data_3 = []
col7_data_3 = []
col8_data_3 = []
col9_data_3 = []
col10_data_3 = []
col11_data_3 = []
col12_data_3 = []
col13_data_3 = []
col14_data_3 = []
col15_data_3 = []
col16_data_3 = []
col17_data_3 = []
col18_data_3 = []
col19_data_3 = []


# CDB1 Industry
with open(CDB1, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        col1_data_1.append(quoted(row[col1]))

        col2_data_1.append(roundne(row[col2]))
        col3_data_1.append(p2f(row[col3]))
        col4_data_1.append(p2f(row[col4]))
        col5_data_1.append(roundne(row[col5]))
        col6_data_1.append(roundne(row[col6]))
        col7_data_1.append(roundne(row[col7]))
        col8_data_1.append(roundne(row[col8]))
        col9_data_1.append(roundne(row[col9]))
        col10_data_1.append(roundne(row[col10]))
        col11_data_1.append(roundne(row[col11]))
        col12_data_1.append(roundne(row[col12]))
        col13_data_1.append(roundne(row[col13]))
        col14_data_1.append(roundne(row[col14]))
        col15_data_1.append(roundne(row[col15]))
        col16_data_1.append(roundne(row[col16]))
        col17_data_1.append(roundne(row[col17]))
        col18_data_1.append(roundne(row[col18]))
        col19_data_1.append(roundne(row[col19]))


# CDB3
with open(CDB3, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        col1_data_3.append(quoted(row[col0]))

        col2_data_3.append(roundne(row[col2]))
        col3_data_3.append(p2f(row[col3]))
        col4_data_3.append(p2f(row[col4]))
        col5_data_3.append(roundne(row[col5]))
        col6_data_3.append(roundne(row[col6]))
        col7_data_3.append(roundne(row[col7]))
        col8_data_3.append(roundne(row[col8]))
        col9_data_3.append(roundne(row[col9]))
        col10_data_3.append(roundne(row[col10]))
        col11_data_3.append(roundne(row[col11]))
        col12_data_3.append(roundne(row[col12]))
        col13_data_3.append(roundne(row[col13]))
        col14_data_3.append(roundne(row[col14]))
        col15_data_3.append(roundne(row[col15]))
        col16_data_3.append(roundne(row[col16]))
        col17_data_3.append(roundne(row[col17]))
        col18_data_3.append(roundne(row[col18]))
        col19_data_3.append(roundne(row[col19]))

# write to JS file

# CDB1
print("var CDB1_data = {};")
print("CDB1_data['headers'] = new Array([", sep='', end='')
print(*headers_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col1_, "] = new Array([", sep='', end='')
print(*col1_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col2_, "] = new Float32Array([", sep='', end='')
print(*col2_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col3_, "] = new Float32Array([", sep='', end='')
print(*col3_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col4_, "] = new Float32Array([", sep='', end='')
print(*col4_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col5_, "] = new Float32Array([", sep='', end='')
print(*col5_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col6_, "] = new Float32Array([", sep='', end='')
print(*col6_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col7_, "] = new Float32Array([", sep='', end='')
print(*col7_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col8_, "] = new Float32Array([", sep='', end='')
print(*col8_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col9_, "] = new Float32Array([", sep='', end='')
print(*col9_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col10_, "] = new Float32Array([", sep='', end='')
print(*col10_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col11_, "] = new Float32Array([", sep='', end='')
print(*col11_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col12_, "] = new Float32Array([", sep='', end='')
print(*col12_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col13_, "] = new Float32Array([", sep='', end='')
print(*col13_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col14_, "] = new Float32Array([", sep='', end='')
print(*col14_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col15_, "] = new Float32Array([", sep='', end='')
print(*col15_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col16_, "] = new Float32Array([", sep='', end='')
print(*col16_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col17_, "] = new Float32Array([", sep='', end='')
print(*col17_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col18_, "] = new Float32Array([", sep='', end='')
print(*col18_data_1, sep=', ', end='')
print("]);")

print("CDB1_data[", col19_, "] = new Float32Array([", sep='', end='')
print(*col19_data_1, sep=', ', end='')
print("]);")


# CDB3
print("var CDB3_data = {};")
print("CDB3_data['headers'] = new Array([", sep='', end='')
print(*headers_3, sep=', ', end='')
print("]);")
    
print("CDB3_data[", col0_, "] = new Array([", sep='', end='')
print(*col1_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col2_, "] = new Float32Array([", sep='', end='')
print(*col2_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col3_, "] = new Float32Array([", sep='', end='')
print(*col3_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col4_, "] = new Float32Array([", sep='', end='')
print(*col4_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col5_, "] = new Float32Array([", sep='', end='')
print(*col5_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col6_, "] = new Float32Array([", sep='', end='')
print(*col6_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col7_, "] = new Float32Array([", sep='', end='')
print(*col7_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col8_, "] = new Float32Array([", sep='', end='')
print(*col8_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col9_, "] = new Float32Array([", sep='', end='')
print(*col9_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col10_, "] = new Float32Array([", sep='', end='')
print(*col10_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col11_, "] = new Float32Array([", sep='', end='')
print(*col11_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col12_, "] = new Float32Array([", sep='', end='')
print(*col12_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col13_, "] = new Float32Array([", sep='', end='')
print(*col13_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col14_, "] = new Float32Array([", sep='', end='')   
print(*col14_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col15_, "] = new Float32Array([", sep='', end='')
print(*col15_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col16_, "] = new Float32Array([", sep='', end='')
print(*col16_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col17_, "] = new Float32Array([", sep='', end='')
print(*col17_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col18_, "] = new Float32Array([", sep='', end='')
print(*col18_data_3, sep=', ', end='')
print("]);")

print("CDB3_data[", col19_, "] = new Float32Array([", sep='', end='')
print(*col19_data_3, sep=', ', end='')
print("]);")