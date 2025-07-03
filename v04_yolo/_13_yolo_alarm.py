from ultralytics import solutions
import cv2

class MySecurityAlarm(solutions.SecurityAlarm):
    def send_email(self, im0, records: int = 5) -> None:
        from email.mime.image import MIMEImage
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        img_bytes = cv2.imencode(".jpg", im0)[1].tobytes()  # Encode the image as JPEG

        # Create the email
        message = MIMEMultipart()
        message["From"] = self.from_email
        message["To"] = self.to_email
        message["Subject"] = "침입자 감지 알림"  # 원하는 제목

        # Add the text message body
        message_body = f"경고! 7번 객체가 {records}개 감지되었습니다."  # 원하는 메시지
        message.attach(MIMEText(message_body))

        # Attach the image
        image_attachment = MIMEImage(img_bytes, name="ultralytics.jpg")
        message.attach(image_attachment)

# 비디오 주소
capture = cv2.VideoCapture('static/vehicles.mp4')

# 이메일 인증
from_email = 'koreaster9480@gmail.com'
password = 'ihlx wbje epgz hhpm'
to_email = 'koreaster9480@gmail.com'

# 모델 선언
# alarm = solutions.SecurityAlarm(
#     model = 'models/yolo11n.pt',
#     show = True,
#     # message['subject'] = "침입자가 감지되었어",
#     # message_body = '확인 필요',
#     records = 1,     # 경고 이메일을 전송하기 위한 최소 감지 수
#     classes = [7]
# )

# 모델 상속 버전
alarm = MySecurityAlarm(
    model = 'models/yolo11n.pt',
    show = True,
    # message['subject'] = "침입자가 감지되었어",
    # message_body = '확인 필요',
    records = 1,     # 경고 이메일을 전송하기 위한 최소 감지 수
    classes = [7]
)

# 이메일 서버 인증
alarm.authenticate(from_email, password, to_email)

# 비디오 프레임 처리
while capture.isOpened():
    success, frame = capture.read()
    
    # 예외 처리
    if not success:
        print('비디오 확인')
        break
    
    # 모델 예측
    re_frame = cv2.resize(frame, (640, 480))
    results = alarm(re_frame)
    
    
    # 종료 버튼
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('종료합니다')
        break

capture.release()
cv2.destroyAllWindows()