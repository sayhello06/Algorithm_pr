#3. 문자열 s가 주어졌을 때, 각 위치마다 자신보다 앞에 나왔으면서 자신과 가장 가까운 동일한 문자가 어디 있는지 구하려고 한다.
#만약, 해당 문자가 처음 등장했다면 -1로 표시한다.

s = "banana"
word_location = []

def word_find():
    print("입력된 문자 : ", s)
    word_cache = [] #문자 존재 여부를 확인하기 위한 임시 저장소

    for x in range(len(s)): #문자열 s의 길이만큼 반복
        word = s[x] #문자열 s의 x번째 글자를 리스트 word에 append
        if word not in word_cache:
            word_location.append(-1) #word_cache 리스트에 word 리스트 항목이 없다면 -1 반환
        else: #리스트에 동일한 문자가 존재할 때
            num = x - word_cache.index(word) #해당 글자와의 거리 계산
            num2 = x - (len(word_cache) - 1 - word_cache[::-1].index(word)) #위의 계산만으로는 가장 가까운 문자의 위치를 구하기 어려움 (왼쪽부터 찾아보기 때문) => 역순으로도 찾아보기
            if num > num2: #정순으로 찾을 때의 거리가 더 멀면 역순으로 찾았을 때의 거리 반환
                word_location.append(num2)
            else: #정순으로 찾을 때의 거리가 더 가까우면 정순으로 찾았을 때의 거리 반환
                word_location.append(num)
        
        word_cache.append(word) #임시 저장소에 문자 저장
    print("결과 : ", word_location)

if __name__ == "__main__":
    word_find()