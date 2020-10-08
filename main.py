from twilio.rest import Client

account_sid = "your-account-sid"

auth_token  = "your-auth-token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17205509130", 
    from_="+12056977227",
    body="whats up")
