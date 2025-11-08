# 텍스트 전처리를 위한 내장 모듈
import re

class TextCleaner:
    # 특수문자 : ["Hello!!!", "Machine-Learning??", "Python123"]
    # 특수문자 제거 메서드 생성
    def remove_special(self, text):
        # r은 정규표현식
        # ^ 는 not 부정을 의미
        # a-zA-Z : 소문자 a-z 대문자 A-Z까지
        # \s는 문자열을 의미한다
        return re.sub(r'[^a-zA-Z\s]', "",text)
    
    # 소문자 변경 메서드 생성
    def to_lower(self, text):
        return text.lower()

    # 위의 특수문자 제거와 소문자 변경 작업을 모두 모으는 메서드 생성
    def clean_corpus(self, text):
        result = []

        for t in text:
            # 특수문자 제거 작업
            t1 = self.remove_special(t)
            # 소문자 제거 작업
            t2 = self.to_lower(t1)
            # result 리스트에 추가
            result.append(t2)
        
        return result


