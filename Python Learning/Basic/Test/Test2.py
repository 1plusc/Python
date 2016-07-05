#-*- coding:utf-8 -*-
#列表与元组
edward=['Edward Gumby',42]
john=['John Smith',50]
database=[edward,john]
print database #[['Edward Gumby', 42], ['John Smith', 50]]
#index索引
greeting="hello"
print greeting[0]
print greeting[-1]
#print greeting[5] #IndexError: string index out of range
for temp in greeting:
    print temp;
fourth=raw_input('Year: ')[3] #获取位置是3的元素
print fourth

#根据给定的年月日，以数字形式打印出日期
months=['January','February','March','April','May','June','July','August','September','October','November','December']
#以1-31的数字作为结尾的列表
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
year=raw_input("Year: ")
month=raw_input("Month(1-12): ")
day=raw_input("Day(1-31): ")

month_number=int(month)
day_number=int(day)
#记得要将月份和天数减1，以获得正确的索引
month_name=months[month_number-1]
ordinal=day+endings[day_number-1]

print month_name+" "+ordinal+"."+year #July 2nd.2016

#分片
tag='<a href="https://github.com/1plusc" value="oneplusc">'
print tag[1:5] #提取部分的第一个元素编号，后面为剩余部分的第一个元素编号
print tag[9:30]
numbers=[1,2,3,4,5,6,7,8,9,10]
print numbers[3:6]
print numbers[-3:-1]
print numbers[-3:]#最后3个元素
print numbers[:3]#前面3个元素


