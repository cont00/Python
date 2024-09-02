import os

#Library_view
#===================================================
#   등록날짜    제목    저자    출판사  장르    상태
#===================================================
#
#===================================================

class Library_view:
    def __init__(self):
        self.books = []

    def add_book(self, date, title, writer, publisher, genre, status):
        book_info = {
            "Date": date,
            "Title": title,
            "Writer": writer,
            "Publisher": publisher,
            "Genre": genre,
            "Status": status
        }
        self.books.append(book_info)

    def display_books(self):
        print("=" * 140)
        print(f"{'등록 날짜':<18} {'제목':<20} {'저자':<20} {'출판사':<22} {'장르':<15} {'상태':<10}")
        print("=" * 140)
        for book in self.books:
            print(f"{book['Date']:<18} {book['Title']:<20} {book['Writer']:<20} {book['Publisher']:<22} {book['Genre']:<15} {book['Status']:<10}")
        print("=" * 140)

# 도서 객체 생성
library = Library_view()

# 도서 추가
library.add_book("2024-02-20", "가시고기", "조창인", "산지", "장편소설", "양호")
library.add_book("2024-02-28", "불변의법칙", "서삼독", "모건하우철", "경제학", "불량")
library.add_book("2024-07-23", "당신이 누군가를 죽였다", "히가시노 게이고", "북다", "추리소설", "불량")
library.add_book("2024-08-21", "빛이 이끄는 곳으로", "백희성", "북로망스", "추리소설", "불량")
library.add_book("2024-08-22", "인공지능", "이명수", "햇빛기획", "스릴러", "불량")
library.add_book("2024-08-27", "이중 하나는 거짓말", "김애란", "문학동네", "소설", "양호")

# 도서 목록 출력
library.display_books()
