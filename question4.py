#4. 단어 s의 가운데 글자를 반환하는 함수, solution을 만드시오.
#단, 단어의 길이가 짝수라면 가운데 두 글자를 반환 (1<=s<=100)
s = input("단어를 입력하세요 : ")

def find_center(s):
    leng = len(s)
    word = list(s)

    if 1<=leng<=100: 
        if leng%2 == 1:
            num = leng//2 #글자의 중앙을 찾기 위해 나누기 2
            return word[num] #중앙 글자 반환

        else:
            num = leng//2 #글자의 중앙을 찾기 위해 나누기 2
            return word[num-1], word[num] #중앙의 두 글자를 반환

    else:
        print("단어를 1글자 이상, 100글자 이하로 입력해주세요.")

if __name__ == "__main__":
    print(find_center(s))