# HW6

주시환 · [학번]

## 실행 방법

1. `.venv` 를 켜고 jupyter 로 `hw6.ipynb` 를 Restart → Run All
2. 같은 폴더에서 서버 실행

```
flask --app app run
```

3. 브라우저에서 http://127.0.0.1:5000/api/docs 접속
4. `POST /api/sales/predict` → Try it out → Execute

입력 파일은 `sales_clean.csv`, 모델 파일은 `sales_model.pkl` (linear regression + qp).

## 단계 ③ 답

linear regression 은 각 열에 계수를 곱해 더하는 것만 할 수 있어서, 수량 × 단가 라는 곱셈 자체를 스스로 만들어내지 못한다. 그래서 test R² 가 0.862 에 그쳤다. 곱한 값을 qp 열로 직접 만들어 주었더니 계수가 [0, 0, 1], 절편이 0 으로 나왔다. 「총액 = qp」 를 그대로 쓴 것이고 test R² 는 1.0 이 되었다.

## 단계 ⑤ 결정과 이유

max_depth 8 로 정했다. cross-validation 평균이 depth 8 은 0.992, depth 12 는 0.995 로 0.003 차이뿐인데 잎 수는 250 개에서 781 개로 세 배가 된다. 점수가 거의 같으면 단순한 쪽을 골랐다.

## 단계 ⑦ 답

linear regression + qp 를 올렸다. 수량 40 · 단가 200,000 을 넣으면 실제 곱은 8,000,000 인데, linear + qp 는 8,000,000 을 그대로 맞혔고 decision tree (depth 8) 는 7,362,301 로 64만 원가량 어긋났다. tree 는 test R² 가 0.994 로 높았지만, 본 적 없는 수량·단가 조합에서는 training 에서 본 값들의 평균으로 답하기 때문이다.