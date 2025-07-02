# from flask import Flask ,render_template,jsonify,request
# from flask_cors import CORS,cross_origin
# import requests
# from bs4 import BeautifulSoup as bs # it is used to scrape the information from web pages 
# from urllib.request import urlopen as uReq
# application=Flask(__name__)
# app=application
# @app.route("/")
# def homepage():
#     return render_template("index.html")
# @app.route("/aboutme")
# def about():
#     return "<h2> this is private data</h2>"
# @app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
# @cross_origin()
# def index():
#     if request.method == 'POST':
#         try:
#             searchString = request.form['content'].replace(" ","")
#             flipkart_url = "https://www.flipkart.com/search?q=" + searchString
#             uClient = uReq(flipkart_url)
#             flipkartPage = uClient.read()
#             uClient.close()
#             flipkart_html = bs(flipkartPage, "html.parser")
#             bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
#             del bigboxes[0:3]
#             box = bigboxes[0]
#             productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
#             prodRes = requests.get(productLink)
#             prodRes.encoding='utf-8'
#             prod_html = bs(prodRes.text, "html.parser")
#             print(prod_html)
#             commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

#             filename = searchString + ".csv"
#             fw = open(filename, "w")
#             headers = "Product, Customer Name, Rating, Heading, Comment \n"
#             fw.write(headers)
#             reviews = []
#             for commentbox in commentboxes:
#                 try:
#                     #name.encode(encoding='utf-8')
#                     name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text

#                 except:
#                     name = 'No Name'

#                 try:
#                     #rating.encode(encoding='utf-8')
#                     rating = commentbox.div.div.div.div.text


#                 except:
#                     rating = 'No Rating'

#                 try:
#                     #commentHead.encode(encoding='utf-8')
#                     commentHead = commentbox.div.div.div.p.text

#                 except:
#                     commentHead = 'No Comment Heading'
#                 try:
#                     comtag = commentbox.div.div.find_all('div', {'class': ''})
#                     #custComment.encode(encoding='utf-8')
#                     custComment = comtag[0].div.text
#                 except Exception as e:
#                     print("Exception while creating dictionary: ",e)

#                 mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
#                           "Comment": custComment}
#                 reviews.append(mydict)
#             return render_template('result.html', reviews=reviews[0:(len(reviews)-1)])
#         except Exception as e:
#             print('The Exception message is: ',e)
#             return 'something is wrong'
#     # return render_template('results.html')

#     else:
#         return render_template('index.html')

# if __name__ =="__main__":
#     app.run(host="127.0.0.1", port=5000)
#--------------------------------------------------------------------------------------
# from flask import Flask, render_template, request
# from flask_cors import CORS, cross_origin
# import requests
# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen as uReq

# application = Flask(__name__)
# app = application
# CORS(app)

# @app.route("/")
# def homepage():
#     return render_template("index.html")


# @app.route("/aboutme")
# def about():
#     return "<h2>This is private data</h2>"


# @app.route('/review', methods=['POST', 'GET'])
# @cross_origin()
# def index():
#     if request.method == 'POST':
#         try:
#             # Get user input
#             searchString = request.form['content'].replace(" ", "")
#             flipkart_url = f"https://www.flipkart.com/search?q={searchString}"
#             uClient = uReq(flipkart_url)
#             flipkartPage = uClient.read()
#             uClient.close()

#             flipkart_html = bs(flipkartPage, "html.parser")
#             bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})

#             # If structure changed or no product found
#             if len(bigboxes) < 4:
#                 return render_template('result.html', reviews=[{
#                     "Product": searchString,
#                     "Name": "N/A",
#                     "Rating": "N/A",
#                     "CommentHead": "No results found",
#                     "Comment": "No product information available"
#                 }])

#             del bigboxes[0:3]
#             box = bigboxes[0]
#             productLink = "https://www.flipkart.com" + box.div.div.div.a['href']

#             prodRes = requests.get(productLink)
#             prodRes.encoding = 'utf-8'
#             prod_html = bs(prodRes.text, "html.parser")

#             commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

#             reviews = []
#             for commentbox in commentboxes:
#                 try:
#                     name = commentbox.find('p', {'class': '_2sc7ZR _2V5EHH'}).text
#                 except:
#                     name = 'No Name'

#                 try:
#                     rating = commentbox.div.div.div.div.text
#                 except:
#                     rating = 'No Rating'

#                 try:
#                     commentHead = commentbox.div.div.div.p.text
#                 except:
#                     commentHead = 'No Comment Heading'

#                 try:
#                     comtag = commentbox.find_all('div', {'class': ''})
#                     custComment = comtag[0].div.text if comtag else 'No Comment'
#                 except:
#                     custComment = 'No Comment'

#                 mydict = {
#                     "Product": searchString,
#                     "Name": name,
#                     "Rating": rating,
#                     "CommentHead": commentHead,
#                     "Comment": custComment
#                 }
#                 reviews.append(mydict)

#             return render_template('result.html', reviews=reviews)

#         except Exception as e:
#             print("Exception occurred:", e)
#             return render_template('result.html', reviews=[{
#                 "Product": "Error",
#                 "Name": "N/A",
#                 "Rating": "N/A",
#                 "CommentHead": "Error Occurred",
#                 "Comment": str(e)
#             }])
#     else:
#         return render_template('index.html')


# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)


from flask import Flask, render_template, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup as bs

application = Flask(__name__)
app = application
CORS(app)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/aboutme")
def about():
    return "<h2>This is private data</h2>"

@app.route("/review", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        try:
            searchString = request.form['content'].replace(" ", "")
            flipkart_url = f"https://www.flipkart.com/search?q={searchString}"

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }

            response = requests.get(flipkart_url, headers=headers)
            soup = bs(response.text, "html.parser")

            # Try multiple selectors (for mobile and laptop cards)
            product_tags = soup.select('a._1fQZEK, a.s1Q9rs')
            if not product_tags:
                return render_template("result.html", reviews=[{
                    "Product": searchString,
                    "Name": "N/A",
                    "Rating": "N/A",
                    "CommentHead": "No results found",
                    "Comment": "No product information available"
                }])

            product_link = "https://www.flipkart.com" + product_tags[0]['href']
            product_page = requests.get(product_link, headers=headers)
            prod_soup = bs(product_page.text, "html.parser")
            commentboxes = prod_soup.find_all('div', {'class': "_16PBlm"})

            reviews = []
            for commentbox in commentboxes:
                try:
                    name = commentbox.find('p', {'class': '_2sc7ZR _2V5EHH'}).text
                except:
                    name = 'No Name'

                try:
                    rating = commentbox.div.div.div.div.text
                except:
                    rating = 'No Rating'

                try:
                    commentHead = commentbox.div.div.div.p.text
                except:
                    commentHead = 'No Comment Heading'

                try:
                    comtag = commentbox.find_all('div', {'class': ''})
                    custComment = comtag[0].div.text if comtag else 'No Comment'
                except:
                    custComment = 'No Comment'

                mydict = {
                    "Product": searchString,
                    "Name": name,
                    "Rating": rating,
                    "CommentHead": commentHead,
                    "Comment": custComment
                }
                reviews.append(mydict)

            if not reviews:
                reviews.append({
                    "Product": searchString,
                    "Name": "N/A",
                    "Rating": "N/A",
                    "CommentHead": "No reviews found",
                    "Comment": "The product exists, but no reviews are available."
                })

            return render_template("result.html", reviews=reviews)

        except Exception as e:
            print("Exception occurred:", e)
            return render_template("result.html", reviews=[{
                "Product": searchString,
                "Name": "N/A",
                "Rating": "N/A",
                "CommentHead": "Error Occurred",
                "Comment": str(e)
            }])
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

