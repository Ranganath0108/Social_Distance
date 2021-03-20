import cv2
import time
import config
import smtplib
cap=cv2.VideoCapture(0)

face_model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    status,photo=cap.read()
    
    face_cor=face_model.detectMultiScale(photo)
    if len(face_cor)==0:
        pass
    elif len(face_cor)==1:
        x1=face_cor[0][0]
        y1=face_cor[0][1]
        x2=x1+face_cor[0][2]
        y2=y1+face_cor[0][3]
        photo=cv2.rectangle(photo,(x1,y1),(x2,y2),[0,255,0],2)
        
        cv2.imshow('test',photo)
        if cv2.waitKey(10)==13:
            break
        
    else:
        x1=face_cor[0][0]
        y1=face_cor[0][1]
        x2=x1+face_cor[0][2]
        y2=y1+face_cor[0][3]
        a1=face_cor[1][0]
        b1=face_cor[1][1]
        a2=a1+face_cor[1][2]
        b2=b1+face_cor[1][3]
        i=(x1+x2)/2
        j=(y1+y2)/2
        k=(a1+a2)/2
        l=(b1+b2)/2
        photo=cv2.rectangle(photo,(a1,b1),(a2,b2),[0,255,0],2)
        photo=cv2.rectangle(photo,(x1,y1),(x2,y2),[0,255,0],2)
        dist=((i-j)*(i-j)+(k-l)*(k-l))**0.5
        if dist<=182.88:
            def send_mail(object,msg):
                try:
                    server=smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login(config.Email_ADDRESS,config.PASSWORD)
                    message=f'Subject : {subject}\n\n{msg}'
                    server.sendmail(config.EMAIL_ADDRESS,'ranganathswamy.ys@gmail.com',message)
                    server.quit()
                    print("Success: Email Sent")
                except:
                    print("Email failed to send")
            subject="CORONA UPDATE"
            msg="Two persons are not maintaining distance."
            send_mail(subject,msg)
            time.sleep(3)

        else:
            cv2.putText(photo,"Maintained Distanced Correctly ",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,[255,0,0],2,cv2.LINE_AA)
            
        cv2.imshow('test',photo)
        if cv2.waitKey(10)==13:
            break
        
cv2.destroyAllWindows()
cap.release()
