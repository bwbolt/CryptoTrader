from twilio.rest import Client

def sellText():
  account_sid = '###'

  auth_token = '###'

  client = Client(account_sid, auth_token)

  client.messages.create(
    to="###",
    from_="+###",
    body="SELL etherium"
    )
