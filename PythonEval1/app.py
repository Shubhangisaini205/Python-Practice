from flask import Flask, request
app = Flask(__name__)

postData = {
    "Shubhangi":{
        "username":"Shubhangi Saini",
        "caption":"I am learning Python from Generatiev AI"
        },
   
  
}
@app.route("/allPost")
def GetAllPost():
    return postData

@app.route("/createPost/<string:username>", methods =["POST"])
def CreatePost(username):
    data = request.get_json()
    postData[username] = data
    return {"msg":"Post added Successfully"}

@app.route("/update/<string:username>", methods =["PATCH"])
def updatePost(username):
    data = request.get_json()
    postData[username] = data
    print(postData)
    return {"msg":"Post updated Successfully"}


@app.route("/delete/<string:username>", methods =["DELETE"])
def DeletePost(username):
    del postData[username] 
    print(postData)
    return {"msg":"Post deleted Successfully"}
   

if __name__ == '__main__':
    app.run(debug=True)