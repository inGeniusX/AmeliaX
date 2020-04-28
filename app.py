import requests
import sys
from bs4 import BeautifulSoup
import wikipedia
from googlesearch import search
from flask import Flask, request, render_template

Amelia_response = ""
def chat(query_test):
    print()
    links = []
    do_wiki = False
    for j in search(query_test, start=0, stop=10, pause=0):
        links.append(j)
        if 'wikipedia.org' in j:
            do_wiki = True
    #print(links[0])
    if do_wiki:
        a = '\n''%s ' % query_test + "site:en.wikipedia.org/wiki/" '\n'
        url = ''
        for k in search("%s" % a, num=1, start=0, stop=1):
            url = k
        #if 'wikipedia.org' in url:
         #   print(wikipedia.summary(wikipedia.search(query_test)[0]))
        if True:
            page = BeautifulSoup(requests.get(url).text, 'html.parser').find_all('p')
            x = 0
            block = page[x].getText()
            while len(block) < 5:
                x = x + 1
                block = page[x].getText()
            final_resp = block[:block.find('.')]
            # print(final_resp + '.')
            Amelia_response = final_resp +  ' Learn more here: ' + str(links[0])
        print()
    else:
        final_resp = "I'm not so sure, but you can find more information about it here: " + links[0]
        Amelia_response = final_resp

        # print("I'm not so sure, but you can find more information about it here:" + links[0])


    links = links[len(links)//2:]
    # for i in links:
    #      print(i)

    return Amelia_response

# while True:
#     print()
#     print("Hello, welcome to chat. Type anything to chat, Type quit to quit")
#     x = input("input: ")
#     if x == 'quit':
#         break
#     chat(x)
#     try:
#       chat(x)
#     except IndexError:
#       print("Sorry, I didn't quite get that, please try again.")
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    try:
        final_response = chat(userText)
    except IndexError:
        final_response = "Sorry, I didn't quite get that, could you say that again?"
    return str(final_response)


if __name__ == "__main__":
    app.run()
    #from elsa import cli
    #cli(app, base_url='https://ingeniusx.github.io/AmeliaX/')