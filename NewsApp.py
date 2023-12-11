import requests
print(("Would like to read some news? press(y/n)"))
user_choice=input()

while (user_choice=="y"):
    print("What types of news you'd like to stay updated on?" )
    query=input()
    url = f"https://newsapi.org/v2/everything?q={query}&from=2023-11-28&to=2023-11-28&sortBy=popularity&apiKey=61c121edc4ab45d5876d72a898e4baf4"
    response = requests.get(url).json()
    i=1
    for article in response["articles"]:
        print(str(i)+")"+"News title:",article['title'])
        print("Source Name:",article["source"]['name'])
        print("Description:",article['description'])
        print("You can check the entire news at:",article['url'])
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        i=i+1
    print("Would like to see news? press(y/n)")
    user_choice=input()
    

    
    
    
   



