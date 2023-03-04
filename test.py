import justpy as jp
from pymongo import MongoClient

async def input_demo_model3(request):
    wp = jp.WebPage(data={'text': 'Initial text'})
    input_classes = "m-2 bg-gray-200 appearance-none border-2 border-gray-200 rounded xtw-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
    cluster = MongoClient( "mongodb+srv://asmafariha:access123@cluster0.t1qqadg.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["jobhuntbuddy"]
    collection = db["UserActivityList"]
    results= collection.find({"username":1})
    for result in results:
        jp.Div(text=result["companyname"], classes=input_classes, a=wp)
        jp.Div(text=result["companywebsite"], classes=input_classes, a=wp)
        jp.Div(text=result["jobtitle"], classes=input_classes, a=wp)
        jp.Div(text=result["date"], classes=input_classes, a=wp)
        jp.Div(text=result["coverletter"], classes=input_classes, a=wp)


    return wp

jp.justpy(input_demo_model3)