# coding=UTF-8
import re
def get_year():
    year = input("请输入年：")
    if re.search('^WWWW$|^(\d{4}\,)*?\d{4}$', year):
        month = input("请输入月：")
    else:
        print("输入的年份不正确，请重新输入")
        return get_year()
    if re.search('^WWWW$|^(\d{4}\,)*?\d{1,2}$|^1[0-2]$', month):
        day = input("请输入天：")
    else:
        print("输入的月不正确，请重新输入")
        return get_year()
    if re.search('^WWWW$|^(\d{4}\,)*?\d{1,2}$', day):
        # return 0
        if year%4 == 0:
            res=[]
            print('s%' % '是闰年')
            if month == 1:
              day=31-day
              print('s%' % '是第d%天')
            elif month==2:
                day=31+day
                print('s%' % '是第d%天')
            else:
                for month in range(3, 5, 7, 8, 10, 12):
                    mon = mon + month * 31
                    res.append(mon)
                for month in range(4,6,9,11):
                    mon1=mon+month*30
                    res.append(mon1)
                    print(res)
    else:
        print("输入的天不正确，请重新输入")
        return get_year()
get_year()
# def jisuan():
#     if year %4==0:
#         print('s%'%'是闰年')
#     else:
#         print('s%' % '不是闰年')


