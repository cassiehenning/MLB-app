import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
MY_EMAIL = os.getenv("MY_EMAIL_ADDRESS")

def send_email(subject="[Market Daily] This is a test", html="<p>Hello World</p>"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)
    message = Mail(from_email=MY_EMAIL, to_emails=MY_EMAIL, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", type(e), e.message)
        return None

if __name__ == "__main__":
    example_subject = " YOUR MLB UPDATES " #This tests to make sure the email capabilities are working correctly

    example_html = f""" 
    <h2>Good Evening, here are your MLB updates!</h3>
    <h4>Today's Date</h4>
    <p>Tuesday, May 5, 2020</p>
    <h2>Have a good night!</h2>
    """

    send_email(example_subject, example_html)