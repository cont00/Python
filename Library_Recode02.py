def Library_Recode(BookList):
    # 도서 반출 기록을 저장할 리스트
    borrow_records = []

    while True:
        # 반출 날짜 입력
        borrow_date = input("반출날짜 입력 (YYYY-MM-DD): ")
        
        # 도서 제목 입력
        book_title = input("제목 입력: ")
        
        # 회원 이름 입력
        member_name = input("이름 입력: ")
        
        # 회원 전화번호 입력
        member_phone = input("전화번호 입력: ")
        
        # 상태 선택
        print("상태 선택:")
        print("1. 반출중")
        print("2. 반환완료")
        print("3. 유실")
        try:
            status_select = int(input("상태를 선택하세요 (1/2/3): "))
            if status_select == 1:
                status = "반출중"
            elif status_select == 2:
                status = "반환완료"
            elif status_select == 3:
                status = "유실"
            else:
                print("1 ~ 3 이 외의 번호를 선택하여 오류가 발생하였습니다.")
                continue  # 잘못된 입력 시 다시 입력 받기
        except ValueError:
            print("유효하지 않은 입력입니다. 다시 시도하세요.")
            continue

        # 반출 기록 저장
        record = {
            "반출날짜": borrow_date,
            "도서제목": book_title,
            "회원이름": member_name,
            "회원전화번호": member_phone,
            "상태": status
        }
        borrow_records.append(record)

        print("정상적으로 도서 반출 기록이 저장되었습니다.")
        print(borrow_records)

        # 추가 반출 여부 확인
        another = input("다른 반출 기록을 추가하시겠습니까? (예/아니오): ")
        if another.lower() != '예':
            break

    return borrow_records

# 사용 예시
BookList = []  # 초기 도서 리스트
Library_Recode(BookList)
