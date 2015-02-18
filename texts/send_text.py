from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC57fa3aa8838d68ef8b34f671cf7e4d64"
auth_token  = "650326951cba2e49831c2a20eca04884"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi Toots, I sent this from a computer program I just wrote",
    to="+16103226109",    # Replace with your phone number
    from_="+14846850331") # Replace with your Twilio number
print message.sid



#+1 484-685-0331
