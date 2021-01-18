#    Copyright (C) 2021  Mansoor Rahman, MeepusDepus on Github
#
#    This file is part of Daily-Message-Python on Github.

#    Daily-Message-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Daily-Message-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Graphics-Website. If not, see <https://www.gnu.org/licenses/>.

__author__ = "Mansoor Rahman"
__copyright__ = "Copyright (C) 2021  Mansoor Rahman"
__license__ = "GNU GPL v3"

from datetime import date, timedelta, datetime

def main():
    today = date.today()
    day = timedelta(days=1)
    d1 = today.strftime("%d/%m/%Y")
    yesterday = today - day
    yesterday = yesterday.strftime("%d/%m/%Y")
    d2 = today.strftime("%B %d, %Y")
       
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print("♥     GOOD MORNING FRIEND          ♥")
    print("♥   THIS IS YOUR DAILY MESSAGE     ♥")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    TodayStr = "Today Is "+today.strftime("%d")+" of "+today.strftime("%B")+" "+today.strftime("%Y")
    print("♥",TodayStr.center(34," "),"♥",sep="")

    print("♥Your Lucky Message Of The Day Is: ♥")
    MuffinFile = open("Messages.txt", "r")
    for s in MuffinFile:
        lines = s.split("_")
        if(lines[0] == d1):
            print(lines[1].center(36, " "))        
    MuffinFile.close()
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print("♥            GOODBYE               ♥")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    x = input()
    if (x.lower() == "help"):
        print("Enter date in DD/MM/YYYY format. Type yesterday for previous day's message")
        x = input()
    if (x.lower() == "yesterday"):
        MuffinFile = open("Messages.txt", "r")
        for ss in MuffinFile:
            Slines = ss.split("_")
            if(Slines[0] == yesterday):
                print(Slines[1].center(36, " "))        
        MuffinFile.close()
        y = input()
    elif (x.lower() == "help"):
        print("Enter date in DD/MM/YYYY format. Type yesterday for previous day's message")
        
if __name__ == "__main__":
    main()
