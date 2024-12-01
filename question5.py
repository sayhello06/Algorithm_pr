#5. 정수로 이루어진 배열과 목표 값 target이 주어질 때, 배열에서 두 수의 합이 target이 되는 두 수를 찾아 반환하시오.
#존재하지 않으면 0을 반환 (단, 배열의 길이는 2이상 10,000이하)

nums = [1, 8, 20, 15]
nums_cache = nums #nums 배열의 복사본 (합 연산에 사용됨)
target = 28
result=[] #결과를 저장할 배열

def target_cal():
    if 2 <= len(nums) <= 10000: #배열의 크기 제한

        find = False #결과값을 찾았는지 여부 boolean => 불필요한 실행을 없애기 위함
        for x in range (len(nums)):
            num1 = nums[x] 

            for i in range (len(nums_cache)-1): #nums_cache[1]부터 시작이기 때문에 nums_cache 배열의 크기 - 1 만큼 반복
                num2 = nums_cache[i+1]

                sum = num1 + num2
                if sum == target: #타겟 값과 일치한다면
                    result.append(num1) #nums의 x번째 요소를 result 배열에 추가
                    result.append(num2) #nums_cache의 i+1번째 요소를 reult 배열에 추가
                    find = True #boolean True 반환
                    break #루프 종료
            if find:
                break #find가 True일 때. 즉, 결과값을 찾았을 때 루프 종료
            
        if not find:
            result.append(0) #find가 최종적으로 False일 때. 즉, 결과값을 찾지 못했을 때 0 반환

        print(result)

    else:
        print("배열의 크기는 2이상 10,000 이하여야 합니다.")
        exit #강제종료



if __name__ == "__main__":
    target_cal()