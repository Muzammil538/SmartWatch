import Time
import Wifi
import Search
class RunMain():
    def Run():
        #print("Hello world")
        print('''1 => Time \n2 => Wifi \n3 => Search''')
        comd = input("What Do you Want (1/2/3) : \t")
        if(comd == "1" or comd == "Time" or comd == "time"):
            print("\nDate and Time is : \n")
            Time.ShowTime()
        elif(comd == "2" or comd == "Wifi" or comd == "wifi"):
            print("\nWifi\n")
            Wifi.ShowWifi()
        if(comd == "3" or comd == "Search" or comd == "search"):
            print("\nSearch\n")
            Search.searcher()
    # Run()

RunMain.Run()
