import os
import pickle

def cls():
    os.system('cls')

def Insert(student):
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

def View(student):
    cls()
    print(f'{"=":=^48}')
    print(f'{"이름":<12} {"국어":>4} {"영어":>4} {"수학":>4} {"성적":>6}')
    for key in student.keys():
        print(f'{key:<12}', f'{student[key][0]:>8}', f'{student[key][1]:>6}', f'{student[key][2]:>6}', f'{student[key][3]:>8}')
    print(f'{"=":=^48}')
    return student

def Search(student):
    cls()
    search_Name = input("찾는 대상의 이름 입력: ")
    if (search_Name in student) == True:
        print(f'{"=":=^48}')
        print(f'{"이름":<12} {"국어":>4} {"영어":>4} {"수학":>4} {"성적":>4}')
        print(f'{search_Name:<12}', f'{student[search_Name][0]:>8}', f'{student[search_Name][1]:>6}', f'{student[search_Name][2]:>6}', f'{student[search_Name][3]:>8}')
        print(f'{"=":=^48}')
    else:
        print("찾는 대상이 존재하지 않습니다.")
        print("1. 재검색    2. 되돌아가기")
        search_Select = int(input("번호입력: "))
        if search_Select == 1:
            Search(student)
        elif search_Select == 2:
            Main()
        else:
            print("1 혹은 2 를 입력해주세요.")
            print("그 외 다른 번호입력은 오류를 에러를 발생시킵니다.")
            print("1. 재검색    2. 되돌아가기")
            search_Select = int(input("번호입력: "))
            if search_Select == 1:
                Search(student)
            elif search_Select == 2:
                Main()

    return student

def UpData(student):
    cls()
    updata_Name = input("수정 대상의 이름 입력: ")
    if (updata_Name in student) == True:
        print("학생의 이름도 수정하시겠습니까? 1. Yes   2. No")
        num = int(input("번호입력: "))
        if num == 1:
            student.pop(updata_Name)
            updata_Name = input("학생 이름 입력: ")
            kor = int(input("국어 성적 입력: "))
            eng = int(input("영어 성적 입력: "))
            math = int(input("수학 성적 입력: "))
            result = kor + eng + math
            avg = round((result / 3), 2)
            student[updata_Name] = [kor, eng, math, avg]
            person = student[updata_Name]
        elif num == 2:
            kor = int(input("국어 성적 입력: "))
            eng = int(input("영어 성적 입력: "))
            math = int(input("수학 성적 입력: "))
            result = kor + eng + math
            avg = round((result / 3), 2)
            student[updata_Name] = [kor, eng, math, avg]
            person = student[updata_Name]

    else:
        print("수정 대상이 존재하지 않습니다.")
        print("1. 재검색    2. 메인으로 되돌아가기")
        updata_Select = input("번호입력: ")
        if updata_Select == 1 :
            UpData(student)
        elif updata_Select == 2:
            Main()
        else:
            print("1 혹은 2 를 입력해주세요.")
            print("그 외 다른 번호입력은 오류를 에러를 발생시킵니다.")
            print("1. 재검색    2. 메인으로 되돌아가기")
            updata_Select = int(input("번호입력: "))
            if updata_Select == 1 :
                UpData(student)
            elif updata_Select == 2:
                Main()
    return student

def Delete(student):
    cls()
    delete_Name = input("데이터를 삭제할 학생의 이름을 입력: ")
    if (delete_Name in student) == True:
        print("해당 학생의 데이터를 삭제하시겠습니까? 1. Yes    2. No")
        delete_Select = int(input("번호 입력: "))
        if delete_Select == 1:
            student.pop(delete_Name)
        elif delete_Select == 2:
            print("해당 학생의 데이터 삭제를 취소하였습니다.")
            Delete(student)
    return student

def AllDelete(student):
    cls()
    print("입력되어있는 모든 학생의 데이터를 삭제하시겠습니까? 1. Yes   2. No")
    alldelete_Select = int(input("번호입력: "))
    if alldelete_Select == 1:
        student.clear()
    elif alldelete_Select == 2:
        Main()
    else:
        print("1 혹은 2를 입력해주세요")
        AllDelete()
    return student

def FileUpLoad(student):
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

def FileUpData(student):
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

def Main():
    cls()
    student = dict()
    while True:
        print("1. 학생정보 입력     2. 학생정보 출력    3. 학생정보 찾기   4. 학생정보 수정   5. 학생정보 삭제   6. 모든 학생정보 삭제")
        print("7. 학생정보 불러오기     8. 학생정보 저장하기    9. 학생정보 관리 종료")
        select = int(input())
        
        if select == 1:
            student = Insert(student)
        elif select == 2:
            student = View(student)
        elif select == 3:
            student = Search(student)
        elif select == 4:
            student = UpData(student)
        elif select == 5:
            student = Delete(student)
        elif select == 6:
            student = AllDelete(student)
        elif select == 7:
            student = FileUpLoad(student)
        elif select == 8:
            student = FileUpData(student)
        else:
            print("프로그램을 종료합니다.")
            break

Main()
