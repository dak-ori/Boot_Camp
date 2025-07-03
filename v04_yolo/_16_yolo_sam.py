from ultralytics import SAM

# 모델 선언
model = SAM('models/sam_b.pt')

# 모델 추론
model(
    'static/small-vehicles1.jpeg',
    save = True
)

print('Done')