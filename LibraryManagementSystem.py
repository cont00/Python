import os
import glob
import pickle

path = "C:\\temp\\"

def cls():
    os.system('cls')

def Menu():
    cls()

    # 메뉴출력
    print(f'{"=":=^83}')
    print("||     1. 도 서 검 색            2. 도 서 출 력          3. 도 서 등 록          ||")
    print("||     4. 도 서 반 출 등 록      5. 반 출 기 록 출 력    6. 도 서 폐 기          ||")
    print("||     7. 도서목록 저장하기      8. 반출기록 저장하기    9. 도서목록 불러오기    ||")
    print("||     10. 반출기록 불러오기     11. 종 료                                       ||")
    print(f'{"=":=^83}')

def Library_Search(bookList):       # 1. 도서검색
    cls()

    # 도서제목 or 글쓴이 & 출판사 & 장르 입력으로 찾고자하는 도서검색
    print("주의사항: 검색항목 외 의 항목 검색은 불가능합니다.")
    print("검색학목 제목, 글쓴이, 출판사, 장르")
    book_Search = input("도서검색: ")
    num = 0
    print()
    print("="*90)
    print("{:^10}{:^17}{:^15}{:^17}{:^14}".format("제   목", "글 쓴 이", "출 판 사", "장 르", " 대 출 확 인"))
    print("="*90)
    for i in range(len(bookList)):
        if book_Search == bookList[i][1] or book_Search == bookList[i][2] or book_Search == bookList[i][3] or book_Search == bookList[i][4]:
            print("{:^10}{:^15}{:^15}{:^15}{:^14}".format(bookList[i][1], bookList[i][2], bookList[i][3], bookList[i][4], bookList[i][6]))
            num = 1
    if num == 0:
        cls()
        print("찾고자 하는 결과가 없습니다.")
    print()
    print("다른 도서를 더 찾아보시겠습니까? 1. Yes  2. No")
    Search_Check = int(input("번호입력: "))
    if Search_Check == 1:
        Library_Search(bookList)
    else:
        print("도서검색을 종료하였습니다.")
        print("메뉴화면으로 이동합니다.")

def Library_View(bookList):         # 2. 도서출력
    cls()

    #도서목록 출력
    print("=" * 180)
    print(f"{'등록 날짜':^12} | {'도   서    제   목':^50} | {'저 자':^16} | {'출 판 사':^20} | {'장  르':^12} | {'상  태':^14} | {'대 출 확 인'}")
    print("=" * 180)
    for i in range(len(bookList)):
        print("{:^12} | {:^50} | {:^16} | {:^20} | {:^12} | {:^14} | {:^10}".format(bookList[i][0], bookList[i][1], bookList[i][2], bookList[i][3], bookList[i][4], bookList[i][5], bookList[i][6]))
    print("=" * 180)
    print()
    input("아무키나 누르시면 메뉴로 돌아갑니다.")

def Library_Insert(bookList):       # 3. 도서등록
    cls()

    # 날짜입력
    book_Date = input("등록날짜 입력(YYYY-MM-DD): ")
    print()

    # 도서book_Title입력
    book_Title = input("도서 제목 입력: ")
    print()

    # writer입력
    writer = input("글쓴이 입력: ")
    print()

    # pubilsher입력
    pubilsher = input("출판사 입력: ")
    print()

    # genre선택
    while True:
        print("1. 문학    2. 역사    3. 시    4. 소설    5. 만화책  ")
        genre_Select = int(input("장르 선택: "))
        if genre_Select == 1:
            genre = "문학"
            break
        elif genre_Select == 2:
            genre = "역사"
            break
        elif genre_Select == 3:
            genre = "시"
            break
        elif genre_Select == 4:
            genre = "소설"
            break
        elif genre_Select == 5:
            genre = "만화책"
            break
    print()

    # 도서상태선택
    while True:
        print("1. 양호    2. 보통    3. 불량")
        state_Select = int(input("도서상태 선택: "))
        if state_Select == 1:
            state = "양호"
            break
        elif state_Select == 2:
            state = "보통"
            break
        elif state_Select == 3:
            print("불량 사유 간략히 작성(ex. 낙서존재, 찢어짐, 페이지누락, 오래됨 등...)")
            state = "불량(" + input("불량 사유: ") + ")"
            break
    
    book_RentalCheck = "대여가능"

    # 도서등록 정보 리스트생성
    book = [book_Date, book_Title, writer, pubilsher, genre, state, book_RentalCheck]

    # 리스트에 도서 정보 리스트 추가
    bookList.append(book)
    print()
    print("정상적으로 도서가 등록되었습니다.")
    print()

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
        return 
    else:
        print("잘 못 된 번호를 입력하셨습니다.")
        print("메뉴화면으로 자동이동됩니다.")
        return
    return 

def Library_Record(libraryRecords, bookList):        # 4. 도서반출등록
    cls()
    # 사용자 입력 받기
    # 반출 날짜 입력
    inout_Date = input("반출날짜입력 (YYYY-MM-DD): ")
    print()

    # 반출 도서 제목 입력
    inout_BookTitle = input("반출도서 제목입력: ")
    print()

    # 회원 이름 입력
    member_Name = input("이름입력: ")
    print()

    # 회원 전화번호 입력
    member_Phone = input("전화번호입력 (010-0000-000): ")
    print()
    
    # 상태 선택
    while True:
        print("상태선택: 1. 반출중  2. 반환완료 3. 유실")
        state_Select = int(input("상태를 선택하세요 (1 ~ 3): "))
        if state_Select == 1:
            state = "반출중"
            break
        elif state_Select == 2:
            state = "반환완료"
            break
        elif state_Select == 3:
            state = "유실"
            break

    # 입력받은 정보를 리스트에 추가
    record = [inout_Date, inout_BookTitle, member_Name, member_Phone, state]

    # 리스트에 입력받은 리스트를 추가
    libraryRecords.append(record)
    
    # bookList 리스트 데이터에서 반출여부 수정 
    if state_Select == 1:
        for i in range(len(bookList)):
            if (inout_BookTitle == bookList[i][1]) == True:
                bookList[i][6] = "반출불가"
                return 
    elif state_Select == 2:
        for i in range(len(bookList)):
            if (inout_BookTitle == bookList[i][1]) == True:
                bookList[i][6] = "반출가능"
                return 
    elif state_Select == 3:
        for i in range(len(bookList)):
            if (inout_BookTitle == bookList[i][1]) == True:
                bookList[i][6] = "반출불가"
                return 
    
    # 계속 입력할지 여부 확인
    print()
    print("주의사항: 1 혹은 2 외 다른 선택은 에러가 발생할 수 있습니다.")
    print("또 다른 도서에 대한 반출기록을 하시겠습니까? 1. yes   2.No ")
    another = int(input("선택: "))
    if another == 1:
        Library_Record(libraryRecords, bookList)
    elif another == 2:
        print("메뉴화면으로 이동합니다.")
    else:
        print("1 혹은 2 외 의 선택으로 인하여 메뉴화면으로 돌아갑니다.")
        return 

def Library_Index(libraryRecords):     # 5. 반출기록출력
    cls()
    # 반출기록목록 출력
    print("=" * 140)
    print(f"{'반출 날짜':^12} | {'도   서    제   목':^50} | {'회원이름':^16} | {'전화번호':^20} | {'상  태':^14}")
    print("=" * 140)
    for i in range(len(libraryRecords)):
        print("{:^12} | {:^50} | {:^16} | {:^20} | {:^14}".format(libraryRecords[i][0], libraryRecords[i][1], libraryRecords[i][2], libraryRecords[i][3], libraryRecords[i][4]))
    print("=" * 140)
    print()
    input("아무키나 누르시면 메뉴로 돌아갑니다.")
    return 

def Library_Delete(bookList):       # 6. 도서폐기
    cls()

    # 폐기 할 도서제목 입력으로 찾아서 데이터 삭제
    delete_BookTitle = input("폐기 도서 제목 입력: ")
    for i in range(len(bookList)):
        if (delete_BookTitle in bookList[i][1]) == True:
            print("주의사항: 해당 선택지 번호 이 외의 선택지를 고를 시 오류가 발생합니다")
            print("해당 도서를 정말로 폐기하시겠습니까? 1. Yes  2. No")
            delete_Select = int(input("번호입력( 1 or 2 ): "))
            if delete_Select == 1:
                del(bookList[i])
                return 
            elif delete_Select == 2:
                print("해당 도서의 폐기를 취소하였습니다.")
                print("메뉴화면으로 돌아갑니다.")
                return 
            else:
                print("오류로 인해 메뉴화면으로 강제이동됩니다.")
                return 
    return 

def LibraryBook_IndexUpData(bookList):              # 7. 도서목록 저장하기
    cls()

    #도서목록 생성 - bookList 리스트 데이터 생성
    with open(path + '도서목록',"wb") as fw:
        pickle.dump(bookList, fw)
    print("도서목록을 저장하였습니다.")
    input("아무키나 누르시면 메뉴로 돌아갑니다.")
    return 

def LibraryRecords_IndexUpdeata(libraryRecords):    # 8. 반출기록 저장하기
    cls()

    # 반출목록 생성 - libraryRecords 리스트 데이터 생성
    with open(path + '반출목록',"wb") as fw:
        pickle.dump(libraryRecords, fw)
    print("반출기록을 저장하였습니다.")
    input("아무키나 누르시면 메뉴로 돌아갑니다.")
    return 

def BookList_IndexUpLoad(bookList):         # 9. 도서목록 불러오기

    # pickle로 도서목록 bookList 리스트 데이터 불러와서 bookList에 입력하기
    with open(path + '도서목록', "rb") as fr:
        bookList = pickle.load(fr)
    print("도서목록 불러오기를 성공했습니다.")
    input("아무키나 누르시면 메뉴로 돌아갑니다.")
    
    return bookList

def LibraryRecords_IndexUpLoad(libraryRecords):     # 10. 반출기록 불러오기

    # pickle로 반출목록 libraryRecords 리스트 데이터 불러와서 libraryRecords에 입력하기
    with open(path + '반출목록', "rb") as fr:
        libraryRecords = pickle.load(fr)
    print("반출기록 불러오기를 성공했습니다.")
    input("아무키나 누르시면 메뉴로 돌아갑니다.")
    
    return libraryRecords

def Main():
    cls()

    bookList = list()
    libraryRecords = list()

    while True:
        Menu()
        Menu_Select = int(input("메뉴선택: "))
        if Menu_Select == 1:
            Library_Search(bookList)
        elif Menu_Select == 2:
            Library_View(bookList)
        elif Menu_Select == 3:
            Library_Insert(bookList)
        elif Menu_Select == 4:
            Library_Record(libraryRecords, bookList)
        elif Menu_Select == 5:
            Library_Index(libraryRecords)
        elif Menu_Select == 6:
            Library_Delete(bookList)
        elif Menu_Select == 7:
            LibraryBook_IndexUpData(bookList)
        elif Menu_Select == 8:
            LibraryRecords_IndexUpdeata(libraryRecords)
        elif Menu_Select == 9:
            bookList = BookList_IndexUpLoad(bookList)
        elif Menu_Select == 10:
            libraryRecords = LibraryRecords_IndexUpLoad(libraryRecords)
        else:
            print("도서관 관리 시스템을 종료합니다.")
            break
        
Main()