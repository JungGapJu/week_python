# 각 파일별 클래스 호출
from ml_prep.scaler import DataScaler
from ml_prep.cleaner import TextCleaner
# stats파일은 파일자체를 호출하여 함수들을 실행
from ml_prep import stats 

data =  [[10, 20, 30], [20, 30, 40], [30, 40, 50]]

# 클래스 객체화
scaler = DataScaler()

normalized = scaler.fit_transform(data)

print("===normalized Data===")
print(normalized)

Summary = stats.summary(data)
print("=== Data Summary ===")
print(Summary)

text = ["Hello!!!", "Machine-Learning??", "Python123"]
cleaner = TextCleaner()
cleaned = cleaner.clean_corpus(text)

print("=== Cleaned Texts ===")

print(cleaned)
