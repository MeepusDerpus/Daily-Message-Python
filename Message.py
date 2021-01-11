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
    if (x.lower() == "yesterday"):
        MuffinFile = open("Messages.txt", "r")
        for ss in MuffinFile:
            Slines = ss.split("_")
            if(Slines[0] == yesterday):
                print(Slines[1].center(36, " "))        
        MuffinFile.close()
        y = input()
if __name__ == "__main__":
    main()
