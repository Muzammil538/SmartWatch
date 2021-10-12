from googlesearch import search
import wikipedia
def searcher():
    def GetText():
        print("This is a wikipedia search that gives you the text")
        text_query = input("What would you like to search : \t")
        text_query_result = wikipedia.summary(text_query,2)
        # print(text_query_result)
        print(text_query_result)
    #GetText()
    def GetUrl():
        url_query = input("This is a google seach that gives you the url \nWhat would you like to search : \t ")
        url_query_result = search(url_query,num_results=5,lang="en",tld="com")
        print(url_query_result)
    # GetUrl()

    print("1 => wikipedia \n2 => Google")
    ask = input("What do you want (1/2) : \t")
    if (ask == "1"):
        GetText()
    elif(ask == "2"):
        GetUrl()
    else:
        print("non of he above")
