#2. 정수 리스트 num_list가 주어질 때, 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성하시오.
#단, 두 값이 같을 경우 그 값을 return함.

num_list = [1, 4, 5, 2, 3]
list1 = []
list2 = []

def list_sort():
    for i in num_list:
        if i%2 == 0:
            list2.append(i) #짝수 리스트

        elif i%2 == 1:
            list1.append(i) #홀수 리스트

    print("홀수 리스트 : ", list1)
    print("짝수 리스트 : ", list2)

    sum1 = sum(list1)
    sum2 = sum(list2)

    if(sum1 < sum2):
        print("짝수의 합이 큽니다 : ", sum2)

    elif(sum1 > sum2):
        print("홀수의 합이 큽니다. : ", sum1)

    else:
        print("두 합이 같습니다. : ", sum1)

if __name__ == "__main__":
    list_sort()