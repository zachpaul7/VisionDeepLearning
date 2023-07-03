from transformers import DetrFeatureExtractor, DetrForObjectDetection #DETR(전처리,모델구성)을 사용
from PIL import Image
import numpy as np
import cv2 as cv

# 테스트에 쓸 영상을 읽음
img = Image.open('BSDS_361010.jpg')

# 모델을 읽어오고 테스트 영상에 대해 추론하는 과정
# 모델 파일을 읽어와 전처리에 해당하는 부분을 feature_extractor에 저장
feature_extractor = DetrFeatureExtractor.from_pretrained('facebook/detr-resnet-50')
model = DetrForObjectDetection.from_pretrained('facebook/detr-resnet-50')

inputs = feature_extractor(img, return_tensors='pt')
res = model(**inputs)


im = cv.cvtColor(np.array(img), cv.COLOR_BGR2RGB)

image_width, image_height = img.size

for i in range(res.logits.shape[1]):
    predicted_label = res.logits[0, i].argmax(-1).item()

    if predicted_label != 91:
        name = model.config.id2label[predicted_label]
        prob = '{:.2f}'.format(float(res.logits[0, i].softmax(dim=0)[predicted_label]))

        cx, cy = int(image_width * res.pred_boxes[0, i, 0]), int(image_height * res.pred_boxes[0, i, 1])
        w, h = int(image_width * res.pred_boxes[0, i, 2]), int(image_height * res.pred_boxes[0, i, 3])

        # 좌표 조정
        cx = max(0, cx)
        cy = max(0, cy)
        w = min(w, image_width - cx)
        h = min(h, image_height - cy)

        cv.rectangle(im, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), (255, 0, 0), 2)
        cv.putText(im, name + str(prob), (cx - w // 2, cy - h // 2 - 5), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)

cv.imshow('DETR', im)
cv.waitKey()
cv.destroyAllWindows()