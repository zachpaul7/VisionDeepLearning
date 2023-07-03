import numpy as np

Q = np.array([[1, 0, 0, 1],
              [0, 1, 0, 1]])

Kt = np.array([[0, 0.3, 0],
              [0.2, 0, 0.2],
              [0.3, 0, 0],
              [1, 0.5, 0.9]])

V = np.array([[1, 1, 1, 0],
             [3, 1, 1, 5],
             [0, 0, 0, 9]])

QK = Q@Kt

# Softmax 함수 적용
exp_qk = np.exp(QK)  # 각 요소에 지수 함수를 적용
sum_exp_qk = np.sum(exp_qk, axis=1, keepdims=True)  # 각 행의 요소들의 합 계산
A = exp_qk / sum_exp_qk  # Softmax 적용

C = A@V

print("주목 행렬 A = ",A)
print("문맥 행렬 C = ",C)