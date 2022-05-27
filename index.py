from flask import Flask, jsonify,request

index=Flask(__name__)
data=[
    {
        "id":1,
        "Name":"Raju",
        "Contact":"9845671832",
        "done":False
    },
    {
         "id":2,
        "Name":"Rahul",
        "Contact":"9683421908",
        "done":False
    },

]
@index.route("/")
def homePage():
    return("Home Page")

@index.route("/get-data")
def getData():
    return jsonify({
        "Contact":data
    })

@index.route("/add-data",methods=["POST"])
def addData():
    if not request.json:
        return jsonify({
            "status":"ERROR",
            "message":"Please provide the data"
        })
    contact={
        "id":data[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    },
    data.append(contact)
    return jsonify({
        "status":"SUCCESSFUL",
        "message":"Contact successfully added"
    })

if(__name__=="__main__"):
    index.run(debug=True) 