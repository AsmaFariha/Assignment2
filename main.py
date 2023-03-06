import justpy as jp
from pymongo import MongoClient
import UserRegistration
button_classes = 'bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded m-2'
input_classes = 'border m-2 p-2'

session_data = {}

def form_test():
    wp = jp.WebPage()
    wp.display_url = '/fill_form'

    form1 = jp.Form(a=wp, classes='border m-8 p-8 w-128 l-256')

    user_label = jp.Label(text='User Name', classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=form1)
    in1 = jp.Input(placeholder='User Name', a=form1, classes='form-input')
    user_label.for_component = in1

    password_label = jp.Label(classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 mt-2', a=form1)
    jp.Div(text='Password', classes='block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2', a=password_label)
    jp.Input(placeholder='Password', a=password_label, classes='form-input', type='password')

    submit_button = jp.Input(value='Login', type='submit', a=form1, classes=button_classes)

    def submit_form(self, msg):
        print(msg)
        msg.page.redirect = '/form_submitted'
        session_data[msg.session_id] = msg.form_data

    form1.on('submit', submit_form)

    return wp

@jp.SetRoute('/form_submitted')
def form_submitted(request):
    wp = jp.WebPage()
    wp.display_url = '/verification'
    form_verification = jp.Form(a=wp, classes='border m-8 p-8 w-128 l-256')
    jp.Div(text='Thank you for submitting', a=form_verification, classes='text-xl m-2 p-2')
    for field in session_data[request.session_id]:
        if field.type in ['text']:
            username = field.value
            jp.Div(text=f'{field.placeholder}:  {field.value}', a=form_verification, classes='text-lg m-1 p-1')
        if field.type in ['password']:
            passwordvalue = field.value

    cluster = MongoClient("mongodb+srv://asmafariha:access123@cluster0.t1qqadg.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["jobhuntbuddy"]
    collection = db["UserList"]

    def button_click_Home(self, msg):
        jp.Div(text='Home', a=form_verification, classes='text-lg m-1 p-1')

    def button_click_registration(self, msg):
        jp.Div(text='Registration', a=form_verification, classes='text-lg m-1 p-1')

    results = collection.find({"_id": username})
    for result in results:
        if result["password"] == passwordvalue:
            text = "Verified"
            button_div = jp.Div(classes='flex m-4 flex-wrap', a=form_verification)
            jp.Button(text='Home Page', a=button_div, classes=button_classes, click=button_click_Home)
        else:
            jp.Div(text='Authentication Failed!!!', a=form_verification, classes='text-lg m-1 p-1')
            button_div = jp.Div(classes='flex m-4 flex-wrap', a=form_verification)
            jp.Button(text='Register', a=button_div, classes=button_classes, click=button_click_registration)
    return wp

jp.justpy(form_test)