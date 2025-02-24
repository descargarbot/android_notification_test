# pip install firebase-admin

import firebase_admin
from firebase_admin import credentials, messaging

def initialize_firebase():
    # firebase credenciales JSON
    cred = credentials.Certificate("notificationtest.json")
    firebase_admin.initialize_app(cred)

def send_notification(registration_token):
    message = messaging.Message(
        notification=messaging.Notification(
            title='hola soy un text title',
            body= 'hola soy un text body'
        ),
        token=registration_token,
    )

    #todo: check firebase response
    response = messaging.send(message)
    print(response)


if __name__ == "__main__":
    initialize_firebase()

    # firebase device token
    registration_token = 'eEcbbDUgRJKkqs4-Of3Mmh:APA91bHMLo1X99dGck3KlYROLnHYUR34XsBvWKB2ZL28Se3_eCjwjfbWCgyha1Eds66cguzLQ3hR8wWIFj7MPzq2fbE88WsLR6gM2m1eFEkw714pjTLJjps'
    send_notification(registration_token)
