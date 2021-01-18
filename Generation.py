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

from datetime import datetime, timedelta

def main():
    #startDate = input("Enter Start Date in DD/MM/YYYY format \n")
    DateMsgDict = {}
    startDate = "01/01/2021"
    startDate = datetime.strptime(startDate, '%d/%m/%Y')
    
    #print(startDate," ",msg)
    noDays = int(input("Enter number of Days to generate messages for:\n"))
    

    for i in range(0, noDays):
        currentDate = startDate + timedelta(days=i)
        msg = input(currentDate.strftime("%d/%m/%Y: "))    
        DateMsgDict[currentDate.strftime("%d/%m/%Y")] = msg 
    print(DateMsgDict)
    
    filename = input("Enter fileneame with extension:\n")
    file = open(filename,"a+")

    for key in DateMsgDict:
        file.write(key +"_"+DateMsgDict[key]+"\n")
    file.close()
if __name__ == "__main__":
    main()
