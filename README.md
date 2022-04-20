*********************************************
Sending Email With Django Using gmail
*********************************************
@Email Backend:

   Email backend value changes according to type of email service
   
   
   In this Project I am using smtp backend
   
   
   In your settings make changes like this
   
   ![Screenshot (240)_LI](https://user-images.githubusercontent.com/55806064/164217323-38b17e23-a190-4afb-83c1-6418e2d6d9df.jpg)


  EMAIL_BACKEND:  Backend using for sending email in django
  
  EMAIL_HOST:  email service provider (here i used 'smtp.gmail.com' )
  
  EMAIL_PORT:  port varies with server ( 587 for SMTP )
  
  EMAIL_HOST_USER:  from which we will send emails
  
  EMAIL_HOST_PASSWORD: email account password
  
  EMAIL_USE_TLS: specifies email uses TLS or not, true for gmail
  
  EMAIL_USE_SSL: false for gmail 
  
  **********************************************************************************************************************************************
  send_mail() method
 
 
    ->Imported from django.core.mail
    
    
    1. subject: Email subject 
    
    2. message: Email body
    
    3. from_email: sender email address (EMAIL_HOST_USER)
    
    4. recipient_list: recievers email address (this field should always be list of strings)
    
    5. fail_silently: It is True by default
                      We specified it False so when email isn't send we will get an exception
                      
  ************************************************************************************************************************************************
    Output:
    
![Screenshot (243)_LI](https://user-images.githubusercontent.com/55806064/164220709-f32574a7-d8f3-4c90-ab07-27b5e3509d71.jpg)





    
  
  
