import cv2

# 비디오 주소
capture = cv2.VideoCapture('http://210.99.70.120:1935/live/cctv028.stream/playlist.m3u8')

# 마우스 이벤트 처리 콜백 함수 정의
points = []
count = 0

def mouse_callback(event, x, y, flags, param):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f'{count + 1}번째 좌표 : {x, y}')
        count += 1
        
    if count == 4:
        print("4개의 좌표를 모두 선택했습니다.")
        count = 1

# 윈도우 창 설정
cv2.namedWindow("GET_X_Y", cv2.WINDOW_NORMAL)

# 콜백 함수 등록
cv2.setMouseCallback("GET_X_Y", mouse_callback)

# 비디오 프레임 처리
while capture.isOpened():
    success, frame = capture.read()
    
    # 예외 처리
    if not success:
        print('비디오 확인')
        break
    
    re_frame = cv2.resize(frame, (720, 600))
    cv2.imshow("GET_X_Y", re_frame)
    
    # 종료 버튼
    if cv2.waitKey(10) & 0xFF == ord('q'):
        print('종료합니다')
        break
    
capture.release()
cv2.destroyAllWindows()