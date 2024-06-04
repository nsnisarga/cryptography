from twilio.rest import Client
account_sid = 'ACe70192416fe987699dd300c3d9e8addc'
auth_token = 'c9bbea314cccc480c80f6c10d8706d3c'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='+15014625062',
    body='Alert ',
    to='+917619144990'
    )

    print(message.sid)
