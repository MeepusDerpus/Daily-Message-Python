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
import sys

def main():
    today = date.today()
    day = timedelta(days=1)
    todayStr = today.strftime("%d/%m/%Y")
    yesterday = today - day
    yesterdayStr = yesterday.strftime("%d/%m/%Y")
       
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print("♥     GOOD MORNING FRIEND          ♥")
    print("♥   THIS IS YOUR DAILY MESSAGE     ♥")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    OutputStr = "Today Is "+today.strftime("%d")+" of "+today.strftime("%B")+" "+today.strftime("%Y")
    print("♥",OutputStr.center(34," "),"♥",sep="")

    print("♥Your Lucky Message Of The Day Is: ♥")
    MessagesFile = open("Messages.txt", "r")
    for s in MessagesFile:
        lines = s.split("_")
        if(lines[0] == todayStr):
            print(lines[1].center(36, " "))        
    MessagesFile.close()
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print("♥            GOODBYE               ♥")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")

    InputStr = input()
    while(InputStr != ""):
        if (InputStr.lower() == "yesterday"):
            MessagesFile = open("Messages.txt", "r")
            for s in MessagesFile:
                Slines = s.split("_")
                if(Slines[0] == yesterdayStr):
                    print(Slines[1].center(36, " "))
            MessagesFile.close()    
        else:
               SearchDate = datetime.strptime(InputStr ,"%d/%m/%Y")
               SearchDelta = today - datetime.date(SearchDate) + timedelta(days=1)
               SearchDateStr = SearchDate.strftime("%d/%m/%Y")
               if(SearchDelta.days > 0):                   
                   MessagesFile = open("Messages.txt", "r")
                   for s in MessagesFile:
                       Slines = s.split("_")
                       if(Slines[0] == SearchDateStr):
                           print(Slines[1].center(36, " "))
                   MessagesFile.close()
               else:
                   print("Please Pick a Date Before Today")
            

        InputStr = input()
        if (InputStr == ""):
            sys.exit(0)
    sys.exit(0)      
        
    
        
        
if __name__ == "__main__":
    main()
