#include <vector> //배열과 비슷한 느낌, 스택과 큐 구현 가능하게 함
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr)
{
    vector<int> answer;
    answer.push_back(arr[0]); //arr의 맨 앞 원소를 answer배열의 맨 뒤에 삽입
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] != arr[i - 1])//i가 1부터 이므로 뒤 앞이 아닌 앞 뒤로 비교
            answer.push_back(arr[i]);//[혼동주의] push_back()을 하면 배열의 맨 뒤로 삽입됨, 즉 큐 삽입과 매우 유사함

    }
    return answer;
}
