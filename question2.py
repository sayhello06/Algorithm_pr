#2. 정수 리스트 num_list가 주어질 때, 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성하시오.
#단, 두 값이 같을 경우 그 값을 return함.

num_list = [1, 4, 5, 2, 3]
odd = []
even = []

def list_sort(num_list):
    for i in num_list:
        if i%2 == 0:
            even.append(i) #짝수 리스트

        elif i%2 == 1:
            odd.append(i) #홀수 리스트

    print("홀수 리스트 : ", odd)
    print("짝수 리스트 : ", even)

    odd_sum = sum(odd)
    even_sum = sum(even)

    return max(odd_sum, even_sum)

if __name__ == "__main__":
    print(list_sort(num_list))