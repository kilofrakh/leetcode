class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        diff_y=abs(year-1969)
        leap_y=diff_y//4
        odd_days=leap_y*2+(diff_y-leap_y)+2
        l=[31,28,31,30,31,30,31,31,30,31,30,31]
        if year%400==0 or (year%4==0 and year%100!=0) :
            l[1]=29
        for i in range(month-1):
            odd_days+=l[i]
        odd_days+=day
        return days[odd_days%7]