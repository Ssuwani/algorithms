import re

def solution(new_id):
    st = new_id
    st = st.lower() # 모두 소문자로 바꿈
    st = re.sub('[^a-z0-9\-_.]', '', st) # 소문자, 숫자, -, _, . 에 해당되지 않는 문자는 제거
    st = re.sub('\.+', '.', st) # . 이 1개 이상 나오면 . 으로 대치
    st = re.sub('^[.]|[.]$', '', st) # ^x 는 시작을 의미, x$ 는 종료를 의미한다. 해당되면 제거
    st = 'a' if len(st) == 0 else st[:15] # 빈문자열이면 "a" 문자열은 15자리 까지만
    st = re.sub('[.]$', '', st) # 15자리까지만 표현을 했으므로 뒷부분에 . 을 다시 확인해줘야 한다.
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))]) # 길이가 2보다 크면 그대로 그렇지 않다면 마지막 문자를 길이가 3이 될때까지 추가.
    return st