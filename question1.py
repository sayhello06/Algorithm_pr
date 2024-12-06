#1. 알파벳으로만 이루어진 단어를 입력 받아, 그 길이를 출력하는 프로그램을 작성하시오.

def input_count():
    word = input("영단어를 입력해주세요 : ")

    print('공백을 포함한 글자 수 : ', len(word))
    print('공백을 제외한 글자 수 : ', len(word.replace(' ', ''))) #공백을 replace
    print("\n")

if __name__ == "__main__":
    input_count()
    