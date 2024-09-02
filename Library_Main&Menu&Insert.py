import os
import glob
import pickle

# 도서등록 저장할 리스트 생성
bookList = []

def cls():
    os.system('cls')

def Menu():
    cls()
    print(f'{"=":=^81}')
    print("||       1. 도 서 검 색          2. 도 서 출 력        3. 도 서 등 록          ||")
    print("||       4. 도 서 반 출          5. 반 출 기 록        6. 도 서 폐 기          ||")
    print("||       7. 기록 저장하기        8. 기록 불러오기      9. 종 료                ||")
    print(f'{"=":=^81}')


def Library_Search(bookList):       # 1. 도서검색
    cls()
    return bookList

def Library_Vive(bookList):         # 2. 도서출력
    cls()
    print(bookList)
    input("")
    return bookList

def Library_Insert(bookList):       # 3. 도서등록
    # 날짜입력
    book_Date = input("등록날짜 입력(YYYY-MM-DD): ")

    # 도서book_Title입력
    book_Title = input("도서 제목 입력: ")

    # writer입력
    writer = input("글쓴이 입력: ")

    # pubilsher입력
    pubilsher = input("출판사 입력: ")

    # genre선택
    print("주의사항 : 제시된 선택지가 아닌 것을 선택할 경우 에러가 발생하여 처음부터 다시 등록하게 됩니다.")
    print("1. 문학    2. 역사    3. 시    4. 소설    5. 만화책")
    genre_Select = int(input("장르 선택: "))
    if genre_Select == 1:
        genre = "문학"
    elif genre_Select == 2:
        genre = "역사"
    elif genre_Select == 3:
        genre = "시"
    elif genre_Select == 4:
        genre = "소설"
    elif genre_Select == 5:
        genre = "만화책"
    else:
        print("1 ~ 5 이 외의 번호를 선택하여서 오류가 발생하였습니다.")
        print("도서등록을 처음부터 다시 해주세요")
        Library_Insert(bookList)
    
    # 도서상태선택
    print("주의사항 : 제시된 선택지가 아닌 것을 선택할 경우 에러가 발생하여 처음부터 다시 등록하게 됩니다.")
    print("1. 양호    2. 보통    3. 불량")
    state_Select = int(input("도서상태 선택: "))
    if state_Select == 1:
        state = "양호"
    elif state_Select == 2:
        state = "보통"
    elif state_Select == 3:
        print("불량 사유 간략히 작성(ex. 낙서존재, 찢어짐, 페이지누락, 오래됨 등...)")
        state = "불량(" + input("불량 사유: ") + ")"
    else:
        print("1 ~ 3 이 외의 번호를 선택하여서 오류가 발생하였습니다.")
        print("도서등록을 처음부터 다시 등록해주세요")
        Library_Insert(bookList)
    book_RentalCheck = "대여가능"

    # 도서등록 정보 리스트생성
    book = [book_Date, book_Title, writer, pubilsher, genre, state, book_RentalCheck]

    # 리스트에 도서 정보 리스트 추가
    bookList.append(book)

    print("정상적으로 도서가 등록되었습니다.")

    # 추가 도서 등록 여부 확인
    print("도서등록을 반복해서 실행하시겠습니까?")
    print("1. Yes 선택시 다시 도서등록 화면으로 돌아갑니다.")
    print("2. No  선택시 메뉴화면으로 돌아갑니다.")
    select_Num = int(input("번호입력: "))
    if select_Num == 1:
        print("다시 도서등록 화면으로 이동합니다.")
        Library_Insert(bookList)
    elif select_Num == 2:
        print("메뉴화면으로 이동합니다.")
        return bookList
    else:
        print("잘 못 된 번호를 입력하셨습니다.")
        print("메뉴화면으로 자동이동됩니다.")
        return bookList
    
    return bookList

def Library_Recode(bookList):       # 4. 도서반출
    return bookList

def Library_Index(bookList):        # 6. 반출기록
    return bookList

def Library_Delete(bookList):       # 6. 도서폐기
    cls()
    delete_BookTitle = input("폐기 도서 제목 입력: ")
    for i in range(len(bookList)):
        if (delete_BookTitle in bookList[i][1]) == True:
            print("주의사항: 해당 선택지 번호 이 외의 선택지를 고를 시 오류가 발생합니다")
            print("해당 도서를 정말로 폐기하시겠습니까? 1. Yes  2. No")
            delete_Select = int(input("번호입력( 1 or 2 ): "))
            if delete_Select == 1:
                del(bookList[i])
            elif delete_Select == 2:
                print("해당 도서의 폐기를 취소하였습니다.")
                print("메뉴화면으로 돌아갑니다.")
                return bookList
            else:
                print("오류로 인해 메뉴화면으로 강제이동됩니다.")
                return bookList

    return bookList

def IndexUpData(bookList):          # 7. 기록 저장하기
    return bookList

def IndexUpLoad(bookList):          # 8. 기록 불러오기
    return bookList

def Main():
    cls()
    bookList = list()
    while True:
        Menu()
        Menu_Select = int(input("메뉴선택: "))
        if Menu_Select == 1:
            bookList = Library_Search(bookList)
        elif Menu_Select == 2:
            bookList = Library_Vive(bookList)
        elif Menu_Select == 3:
            bookList = Library_Insert(bookList)
        elif Menu_Select == 4:
            bookList = Library_Recode(bookList)
        elif Menu_Select == 5:
            bookList = Library_Index(bookList)
        elif Menu_Select == 6:
            bookList = Library_Delete(bookList)
        elif Menu_Select == 7:
            bookList = IndexUpData(bookList)
        elif Menu_Select == 8:
            bookList = IndexUpLoad(bookList)
        else:
            print("도서관 관리 시스템을 종료합니다.")
            break

Main()