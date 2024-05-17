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
    google_search() 

    def stat_dict():
        import urllib.request
        with urllib.request.urlopen() as response:
            html = [response.read()]
        print(html)
        nba_stats = {
        }
        print(nba_stats)  
    stat_dict()


    def sports_query():
        chatQuery = input("Hello, my name is Discovery AI. What can I help you with?> ")
        if chatQuery == "Games" or "Sports":
            
            chatQuery2 = input("NBA, NFL, NHL, WNBA, College, or MLB?> ")
            if chatQuery2 == "NBA" or "nba":
                input("What game would you like to review?> ")
            elif chatQuery2 == "NFL" or "nfl":
                input
    # sports_query()

    def mathHelp():
        ip=input("Enter math equation: ")
        for url in search(ip, stop=1):
            print(url)
            webbrowser.open(ip)
    # mathHelp()
DiscoveryAI()


