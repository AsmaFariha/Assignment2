import justpy as jp
from pymongo import MongoClient
import smtplib , ssl



button_classes = 'bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded m-2'
input_classes = 'border m-2 p-2'

#User Registration
def form_registration():
    wp = jp.WebPage()
    wp.display_url = '/registration'  #Input form

    form1 = jp.Form(a=wp, classes='border m-8 p-8 w-128 l-256')

    user_label1 = jp.Label(text='User Name', classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in1 = jp.Input(placeholder='User Name', a=form1, classes='form-input')
    user_label1.for_component = in1

    user_label2 = jp.Label(text='Email Address', classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in2 = jp.Input(placeholder='Input valid Email', a=form1, classes='form-input')
    user_label2.for_component = in2


    password_label = jp.Label(classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 mt-2', a=form1)
    jp.Div(text='Password', classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=password_label)
    passw=jp.Input(placeholder='Password', a=password_label, classes='form-input', type='password')

    submit_button = jp.Input(value='Register', type='submit', a=form1, classes=button_classes)


#Submit button action
    def submit_form(self, msg):
        print(msg)
        print(in1.value)
        cluster = MongoClient("mongodb+srv://asmafariha:access123@cluster0.t1qqadg.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["jobhuntbuddy"]
        collection_auth = db["UserList"]
        collection_prof= db["UserProfile"]

        if collection_auth.count_documents({"_id" : in1.value}) >= 1:
            jp.Div(text='UserName already in use. Try Another', classes=button_classes, a=wp)  #Check existing user
        else:
            post_user= {"_id": in1.value, "password":passw.value}  #Add new user in authentication and user profile tables
            post_profile = {"_id": in1.value, "email": in2.value}
            collection_auth.insert_one(post_user)
            collection_prof.insert_one(post_profile)
            jp.Div(text='Registration Successful', classes=button_classes, a=wp)
            #sending email
            sender = 'postmaster@sandboxc6cbdf39d9614ad6a792f43b19b7d6d6.mailgun.org'
            receivers = [in2.value]
            message = """From: From <JobHuntBuddy>
            
            Subject: Successful Registration
            
            Welcome to JobHuntBuddy portal! Wish you success!!!
            """
            smtpObj = smtplib.SMTP('smtp.mailgun.org',587)
            smtpObj.starttls(context=ssl.create_default_context())
            smtpObj.login(sender,'653940aa7dddc84922ea87e7df43be32-15b35dee-a761ee1d')
            smtpObj.sendmail(sender, receivers, message)

    form1.on('submit', submit_form)
    return wp


jp.justpy(form_registration)