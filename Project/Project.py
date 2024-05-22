from googlesearch import search
import webbrowser
import math
def DiscoveryAI():
    def google_search():
        query = input("Search: ")
        results = search(query,num=1,start=1,stop=1)
        for result in results:
            print(result)
        return webbrowser.open(result)
    #google_search() 

    def stat_dict():
        import urllib.request
        with urllib.request.urlopen() as response:
            html = [response.read()]
        print(html)
        nba_stats = {
        }
        print(nba_stats)  
    #stat_dict()


    def mathHelp():
        userNumber = int(input("Enter number> "))
        userEquation = input("What would you like to find?> ")
        if userEquation == "the sine of" or "sin":
            print(math.sin(userNumber))
        elif userEquation == "the cosine of" or "cos":
            print(math.cos(userNumber))
    mathHelp()
DiscoveryAI()


