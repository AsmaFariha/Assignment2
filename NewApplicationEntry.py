import justpy as jp
from pymongo import MongoClient

button_classes = 'bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded m-2'
input_classes = 'border m-2 p-2'


# User Registration
@jp.SetRoute('/ListApplications')
def form_application():
    wp = jp.WebPage()
    wp.display_url = '/registration'  # Input form

    form1 = jp.Form(a=wp, classes='border m-8 p-8 w-128 l-256')

    user_label1 = jp.Label(text='Company Name',
                           classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in1 = jp.Input(placeholder='Type company name here', a=form1, classes='form-input')
    user_label1.for_component = in1

    user_label3 = jp.Label(text='Address',
                           classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in3 = jp.Input(placeholder='Put Postal Code here', a=form1, classes='form-input')
    user_label3.for_component = in3

    user_label2 = jp.Label(text='Email Address',
                           classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in2 = jp.Input(placeholder='Input valid Email', a=form1, classes='form-input')
    user_label2.for_component = in2

    user_label4 = jp.Label(text='Job Title',
                           classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in4= jp.Input(placeholder='Input valid Email', a=form1, classes='form-input')
    user_label4.for_component = in4

    user_label5 = jp.Label(text='Job Description',
                           classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in5 =jp.Input(placeholder='Input the job responsibility and Requirement here', a=form1, classes='form-input')
    user_label5.for_component = in5

    user_label6 = jp.Label(text='Salary',
                           classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in6= jp.Input(placeholder='Salary Range (If posted)', a=form1, classes='form-input')
    user_label6.for_component=in6

    user_label7 = jp.Label(text='Website',
                           classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in7= jp.Input(placeholder='Company website', a=form1, classes='form-input')
    user_label7.for_component=in7


    user_label8 = jp.Label(text='Application Source',
                           classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in8= jp.Input(placeholder='Where did you find and applied for this job', a=form1, classes='form-input')
    user_label8.for_component =in8

    user_label10 = jp.Label(text='Application Date mm/DD/YYYY',
                           classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in10= jp.Input(placeholder='Date applied on', a=form1, classes='form-input')
    user_label10.for_component = in10

    user_label9 = jp.Label(text='Cover Letter',
                           classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in9=user_label9.for_component = jp.Input(placeholder='Put here if you want to store', a=form1,
                                         classes='form-input')
    user_label9.for_component = in9


    submit_button = jp.Input(value='Save', type='submit', a=form1, classes=button_classes)

    # Submit button action
    def submit_form(self, msg):
        print(msg)
        print(in1.value)
        cluster = MongoClient("mongodb+srv://asmafariha:access123@cluster0.t1qqadg.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["jobhuntbuddy"]
        collection = db["UserActivityList"]

        post_apps = {"username":1 ,"companyname":in1.value , "companywebsite": in7.value , "email":in3.value  , "jobtitle": in4.value , "address": in2.value , "date":in10.value ,
                "description":in5.value ,"salary": in6.value ,"coverletter": in9.value ,"source":in8.value }
        collection.insert_one(post_apps)
        jp.Div(text='Your Application summary Successfully saved', classes=button_classes, a=wp)

    form1.on('submit', submit_form)

    return wp


jp.justpy(form_application)