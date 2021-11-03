from twilio.rest import Client

def buyText():
  account_sid = '###'

  auth_token = '###'

  client = Client(account_sid, auth_token)

  client.messages.create(
    to="###",
    from_="+###",
    body="BUY etherium"
    )
