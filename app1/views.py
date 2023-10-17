from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.mail import send_mail



@login_required(login_url='login')
def HomePage(request):
    return render (request,'h1.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

          #  my_user=User.objects.create_user(uname,email,pass1)
          #  my_user.save()
          #  return redirect('login')
   
            #my_user = CustomUser.objects.create_user(username=uname, email=email, password=pass1)
            #my_user.save()
            return redirect('login')


    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            #return HttpResponse ("Username or Password is incorrect!!!")
            return render(request,'h1.html')
            

            return redirect('login')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


#here will build complete outpass api
def mainscreen(request):
    return render(request,'h1.html')

# views.py

from .forms import OutpassForm  # Import the OutpassForm


# Your apply_outpass view
'''
def apply_outpass(request):
    if request.method == 'POST':
        form = OutpassForm(request.POST)
        if form.is_valid():
            outpass_date = form.cleaned_data['outpass_date']
            outpass_time = form.cleaned_data['outpass_time']
            outpass_reason = form.cleaned_data['outpass_reason']
            remarks = form.cleaned_data['remarks']
            return_to_company = form.cleaned_data['return_to_company']
            return_time = form.cleaned_data['return_time']
            # Save the data to your database or perform any necessary actions here

            
            # Email Notification Logic
            subject = 'Outpass Application Submitted'
            message = f'Employee_id = TKAPC1255\n' \
                      f'Employee_name = Prajwal N\n' \
                      f'An employee has submitted an outpass application.\n\n' \
                      f'Outpass date:{outpass_date}\n'\
                      f'Outpass Time: {outpass_time}\n' \
                      f'Reason: {outpass_reason}\n' \
                      f'Remarks: {remarks}\n'\
                      f'Return to Company: {return_to_company}\n' \
                      f'Return Time: {return_time}'
            from_email = 'tsaadmin@dx.tkap.co.in '  #  sender email 
            recipient_list = ['prajwal_n@tkap.co.in','arunkumar_r@tkap.co.in',]  # Add recipient emails

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return render(request, 'submission.html')
            #return HttpResponse ("Thankyou your outpass is successfully submitted!!!")
            

    else:
        form = OutpassForm()  # Create an instance of the form
    
    return render(request, 'apply_outpass.html', {'form': form, 'page_title': 'Apply for Outpass'})  # Pass the form to the template

#for dashboard template
'''
def dashboards(request):
    return render(request,'dashboard.html')




# for approval screen


#for updated code
import pandas as pd
from django.http import HttpResponse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase  
from email import encoders 
import smtplib
def get_approval(request):
    return HttpResponse("Employee Outpass is Approved successfully")

def get_reject(request):
    return HttpResponse("Employee Outpass is rejected !!!")

def apply_outpass(request):
    if request.method == 'POST':
        form = OutpassForm(request.POST)
        if form.is_valid():
            outpass_date = form.cleaned_data['outpass_date']
            outpass_time = form.cleaned_data['outpass_time']
            outpass_reason = form.cleaned_data['outpass_reason']
            remarks = form.cleaned_data['remarks']
            return_to_company = form.cleaned_data['return_to_company']
            return_time = form.cleaned_data['return_time']

            # Save the data to your database or perform any necessary actions here

            # Create a dictionary to store outpass details
            outpass_data = {
                'Employee ID': 'TKAP0001',
                'Employee Name': 'Mahesh CG',
                'Outpass Date': outpass_date,
                'Outpass Time': outpass_time,
                'Reason': outpass_reason,
                'Remarks': remarks,
                'Return to Company': return_to_company,
                'Return Time': return_time,
            }

            # Convert the data to a Pandas DataFrame
            df = pd.DataFrame([outpass_data])

            # Save the DataFrame to an Excel file
            excel_file_path = 'outpass_details.xlsx'
            df.to_excel(excel_file_path, index=False)

            # Email Notification Logic
            subject = 'Outpass Application Submitted'
            from_email = 'tsaadmin@dx.tkap.co.in'
            recipient_list = ['prajwal_n@tkap.co.in', 'arunkumar_r@tkap.co.in','mahesh_cg@tkap.co.in','vaisakh_r@tkap.co.in']

            # Create an email message
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = ', '.join(recipient_list)
            msg['Subject'] = subject

            # HTML content for the email body
            email_body = f'''
            <p>An employee has submitted an outpass application. Details are attached.</p>
            <p>Please take action:</p>
            <a href="{get_approval(request)}">Approve</a> |
            <a href="{get_reject(request)}">Reject</a>
            <br><br>
            <table border="1">
                <tr>
                    <th>Employee ID</th>
                    <th>Employee Name</th>
                    <th>Outpass Date</th>
                    <th>Outpass Time</th>
                    <th>Reason</th>
                    <th>Remarks</th>
                    <th>Return to Company</th>
                    <th>Return Time</th>
                </tr>
                <tr>
                    <td>TKAP0001</td>
                    <td>Mahesh CG</td>
                    <td>{outpass_date}</td>
                    <td>{outpass_time}</td>
                    <td>{outpass_reason}</td>
                    <td>{remarks}</td>
                    <td>{return_to_company}</td>
                    <td>{return_time}</td>
                </tr>
            </table>
            '''
            
            msg.attach(MIMEText(email_body, 'html'))

            # Attach the Excel file
            with open(excel_file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename=outpass_details.xlsx")
                msg.attach(part)

            # Send the email
            server = smtplib.SMTP('smtp.office365.com', 587)  # Replace with your SMTP server details
            server.starttls()
            server.login(from_email, 'Tov91456')  # Replace with your email and password

            text = msg.as_string()
            server.sendmail(from_email, recipient_list, text)
            server.quit()

            return render(request, 'submission.html')
    
    else:
        form = OutpassForm()
    
    return render(request, 'apply_outpass.html', {'form': form, 'page_title': 'Apply for Outpass'})

# Define your get_approval and get_reject functions as before
# to run leoni


import subprocess
from django.shortcuts import render



def run_script(request):
    # Specify the path to the Python script
    script_path = r"D:\jarvis\Jarvis-Desktop-Voice-Assistant-main\Jarvis\leoni.py"

    try:
        # Run the Python script using subprocess
        result = subprocess.run(['python', script_path], stdout=subprocess.PIPE, text=True, check=True)
        
        # Get the script's output
        script_output = result.stdout
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions that occur when running the script
        script_output = f"An error occurred: {e}"

    # Pass the script output as a context variable to the template
    context = {'script_output': script_output}

    # Render the 'leoni.html' template and pass the context
    return render(request,'leoni.html') 

