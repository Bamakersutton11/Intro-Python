from googlesearch import search
import webbrowser

def sports_query():
    chatQuery = input("Hello, my name is Discovery AI. What can I help you with?> ")
    if chatQuery == "Games" or "Sports":
        print("Which sport should I look for?")
        chatQuery2 = input("NBA, NFL, NHL, WNBA, College, or MLB?> ")
        if chatQuery2 == "NBA" or "nba":
            input("What game would you like to review?> ")
        elif chatQuery2 == "NFL" or "nfl":
            input
#sports_query()

def webSearch():
    ip=input("What would you like to search for? ")
    for url in search(ip, stop=1):
        print(url + "/Algebra")
        webbrowser.open(ip)
webSearch()



