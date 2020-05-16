from twilio.rest import Client

account_sid = 'ACd7998b9686f908a2d971ec617802d767'
auth_token = '42bf9420ddfccbb257b1e55c912daabb'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12073863803',
    body=' newb ',
    to='+16475246691'
)

print(message.sid)