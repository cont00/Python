import os
import pickle

def cls():
    os.system('cls')

def insert(student):
    cls()
    name = input("학생 이름 입력: ")
    kor = int(input("국어 성적 입력: "))
    eng = int(input("영어 성적 입력: "))
    math = int(input("수학 성적 입력: "))
    result = kor + eng + math
    avg = round((result / 3), 2)
    student[name] = [kor, eng, math, avg]
    person = student[name]
    return student

def view(student):
    cls()
    print(f'{"=":=^48}')
    print(f'{"이름":<12} {"국어":>4} {"영어":>4} {"수학":>4} {"성적":>6}')
    for key in student.keys():
        print(f'{key:<12}', f'{student[key][0]:>8}', f'{student[key][1]:>6}', f'{student[key][2]:>6}', f'{student[key][3]:>8}')
    print(f'{"=":=^48}')
    return student

def search(student):
    cls()
    search_name = input("찾는 대상의 이름 입력: ")
    if (search_name in student) == True:
        print(f'{"=":=^48}')
        print(f'{"이름":<12} {"국어":>4} {"영어":>4} {"수학":>4} {"성적":>4}')
        print(f'{search_name:<12}', f'{student[search_name][0]:>8}', f'{student[search_name][1]:>6}', f'{student[search_name][2]:>6}', f'{student[search_name][3]:>8}')
        print(f'{"=":=^48}')
    else:
        print("찾는 대상이 존재하지 않습니다.")
        print("1. 재검색    2. 되돌아가기")
        search_select = int(input("번호입력: "))
        if search_select == 1:
            search(student)
        elif search_select == 2:
            main()
        else:
            print("1 혹은 2 를 입력해주세요.")
            print("그 외 다른 번호입력은 오류를 에러를 발생시킵니다.")
            print("1. 재검색    2. 되돌아가기")
            search_select = int(input("번호입력: "))
            if search_select == 1:
                search(student)
            elif search_select == 2:
                main()

    return student

def updata(student):
    cls()
    updata_name = input("수정 대상의 이름 입력: ")
    if (updata_name in student) == True:
        print("학생의 이름도 수정하시겠습니까? 1. Yes   2. No")
        num = int(input("번호입력: "))
        if num == 1:
            student.pop(updata_name)
            updata_name = input("학생 이름 입력: ")
            kor = int(input("국어 성적 입력: "))
            eng = int(input("영어 성적 입력: "))
            math = int(input("수학 성적 입력: "))
            result = kor + eng + math
            avg = round((result / 3), 2)
            student[updata_name] = [kor, eng, math, avg]
            person = student[updata_name]
        elif num == 2:
            kor = int(input("국어 성적 입력: "))
            eng = int(input("영어 성적 입력: "))
            math = int(input("수학 성적 입력: "))
            result = kor + eng + math
            avg = round((result / 3), 2)
            student[updata_name] = [kor, eng, math, avg]
            person = student[updata_name]

    else:
        print("수정 대상이 존재하지 않습니다.")
        print("1. 재검색    2. 메인으로 되돌아가기")
        updata_select = input("번호입력: ")
        if updata_select == 1 :
            updata(student)
        elif updata_select == 2:
            main()
        else:
            print("1 혹은 2 를 입력해주세요.")
            print("그 외 다른 번호입력은 오류를 에러를 발생시킵니다.")
            print("1. 재검색    2. 메인으로 되돌아가기")
            updata_select = int(input("번호입력: "))
            if updata_select == 1 :
                updata(student)
            elif updata_select == 2:
                main()
    return student

def delete(student):
    cls()
    delete_name = input("데이터를 삭제할 학생의 이름을 입력: ")
    if (delete_name in student) == True:
        print("해당 학생의 데이터를 삭제하시겠습니까? 1. Yes    2. No")
        delete_select = int(input("번호 입력: "))
        if delete_select == 1:
            student.pop(delete_name)
        elif delete_select == 2:
            print("해당 학생의 데이터 삭제를 취소하였습니다.")
            delete(student)
    return student

def alldelete(student):
    cls()
    print("입력되어있는 모든 학생의 데이터를 삭제하시겠습니까? 1. Yes   2. No")
    alldelete_select = int(input("번호입력: "))
    if alldelete_select == 1:
        student.clear()
    elif alldelete_select == 2:
        main()
    else:
        print("1 혹은 2를 입력해주세요")
        alldelete()
    return student

def fileupload(student):
    cls()
    f = open("D:\김현노\Python\ex\student.txt", 'r', encoding='UTF-8')
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        print(line)
    f.close
    with open("D:\김현노\Python\ex\student", "rb") as fr:
        student = pickle.load(fr)
    return student

def fileupdata(student):
    cls()
    with open("D:\김현노\Python\ex\student.txt", 'w', encoding='UTF-8') as f:
        f.write("================================================\n")
        f.write("이름             국어   영어   수학   성적\n")
        for key, value in student.items():
            f.write(f'{key:<12}{student[key][0]:>8}{student[key][1]:>8}{student[key][2]:>6}{student[key][3]:>8}\n')
        f.write("================================================\n")
    with open("D:\김현노\Python\ex\student","wb") as fw:
        pickle.dump(student, fw)
    return student

def main():
    cls()
    student = dict()
    while True:
        print("1. 학생정보 입력     2. 학생정보 출력    3. 학생정보 찾기   4. 학생정보 수정   5. 학생정보 삭제   6. 모든 학생정보 삭제")
        print("7. 학생정보 불러오기     8. 학생정보 저장하기    9. 학생정보 관리 종료")
        select = int(input())
        
        if select == 1:
            student = insert(student)
        elif select == 2:
            student = view(student)
        elif select == 3:
            student = search(student)
        elif select == 4:
            student = updata(student)
        elif select == 5:
            student = delete(student)
        elif select == 6:
            student = alldelete(student)
        elif select == 7:
            student = fileupload(student)
        elif select == 8:
            student = fileupdata(student)
        else:
            print("프로그램을 종료합니다.")
            break

main()