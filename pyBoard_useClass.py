import openpyxl as op

class pyBoard:

    def __init__(self):
        '''
        # basic version pyBoard, don't use openpyxl.lib
        '''

        user1 = {"아이디": "hong123", "비밀번호": "1234", "이름": "홍길동"}
        user2 = {"아이디": "sony7", "비밀번호": "7777", "이름": "손흥민"}
        user3 = {"아이디": "ryu99", "비밀번호": "9999", "이름": "류현진"}
        user4 = {'아이디': 'timandsunny', '비밀번호':'1234','이름':'dh'}

        self.user_list = [user1, user2, user3, user4]

        article1 = {"번호": 1, "제목": "소니의 축구교실", "내용": "소니의 축구 강좌", "작성자": "sony7"}
        article2 = {"번호": 2, "제목": "류뚱의 야구교실", "내용": "류뚱의 야구 강좌", "작성자": "ryu99"}
        article3 = {"번호": 3, "제목": "길동의 도술교술", "내용": "길동의 도술 강좌", "작성자": "hong123"}

        self.article_list = [article1, article2, article3]
        self.last_article_id = len(self.article_list)
        self.start_pyBoard_login()

        #self.file_path = 'C:/Users/SBS-/Desktop/dh/pyBoard/'
        #self.user_data = 'user_list.xlsx'
        #self.article_data = 'article_list.xlsx'

    def __login__(self, login_ID, login_PW):
        for user in self.user_list:
            if user['아이디'] == login_ID :
                if user['비밀번호'] == login_PW:
                    print('>>> {}님 안녕하세요! 게시판 기능을 시작합니다!'.format(user['이름']))
                    return user
                else :
                    print('>>> 비밀번호를 틀렸습니다.')
                    return False
            if user == self.user_list[-1]:
                print('>>> 잘못된 아이디입니다.')
                return False

    def __signUp__(self, new_ID, new_PW, new_Name):
        for user in self.user_list:
            if user['아이디'] == new_ID:
                print('>>> 존재하는 아이디입니다.')
                break
        self.user_list.append({'아이디':new_ID, '비밀번호':new_PW, '이름':new_Name})
        print('>>> {}님 회원가입이 완료되었습니다.'.format(new_Name))

    def read_article_title(self, article):
        print('● 번호 : {}   제목 : {}'.format(article['번호'], article['제목']))

    def read_article_all(self, article):
        print('● 게시물번호 : {} \n-- 제목 : {} \n-- 내용 : {} \n-- 작성자 : {}\n'
              .format(article['번호'], article['제목'], article['내용'], article['작성자']))

    def write_article(self, new_title, new_info, new_writer):
        self.last_article_id += 1
        self.article_list.append({'번호': self.last_article_id, '제목': new_title, '내용': new_info, '작성자':new_writer})

    def is_exist_article(self, article_no):
        for article in self.article_list :
            if article['번호'] == article_no : return article
        return False

    def is_my_article(self, article, user):
        if article['작성자'] == user['이름'] : return True
        return False

    def update_article(self, article, artc_key, artc_val):
        temp = self.article_list.index(article)
        article[artc_key] = artc_val
        self.article_list[temp] = article

    def start_pyBoard_login(self):
        print('===== Welcome to PyBoard =====')
        while True :
            print('==============================')
            print('[1] 로그인\n[2] 회원가입\n[3] 종료')
            cmd = input('▶ 명령어를 입력해주세요 : ')

            if cmd == '1':
                enter_id = input('-- 아이디를 입력해주세요 : ')
                enter_pw = input('-- 비밀번호를 입력해주세요 : ')
                rs = self.__login__(enter_id, enter_pw)
                if rs is False:
                    continue
                else:
                    self.start_pyBoard_main(rs)

            elif cmd == '2':
                print('\n▷ 회원가입 모드')
                enter_id = input('-- 희망하는 아이디를 입력해주세요 : ')
                enter_pw = input('-- 희망하는 비밀번호를 입력해주세요 : ')
                enter_name = input('-- 사용자의 이름을 입력해주세요 : ')
                self.__signUp__(enter_id, enter_pw, enter_name)

            elif cmd == '3':
                print('\n▷ 프로그램을 종료합니다')
                break

    def start_pyBoard_main(self, user):
        print('==============================')
        print('※ 접속중인 사용자 : {}'.format(user['이름']))
        while True:
            print('==============================')
            print('[1] 게시물 조회 \n[2] 게시물 작성 \n[3] 게시물 수정 \n[4] 게시물 삭제 \n[5] 로그아웃')
            cmd = input('▶ 명령어를 입력해주세요 : ')

            if cmd == '1':
                print('\n▷ 게시물조회 모드')
                mode = input('[1] 제목 조회 \n[2] 상세 조회 \n>>> 명령어를 입력해주세요 : ')
                print('========= 게시물 목록 ==========')
                if mode == '1':
                    print('\n')
                    for article in self.article_list: self.read_article_title(article)
                elif mode == '2':
                    for article in self.article_list : self.read_article_all(article)

            elif cmd == '2':
                print('\n▷ 게시물작성 모드')
                new_title = input('-- 제목을 입력해주세요 : ')
                new_info = input('-- 내용을 입력해주세요 : ')
                new_writer = user['이름']
                self.write_article(new_title, new_info, new_writer)

            elif cmd == '3':
                print('\n▷ 게시물수정 모드')
                artc_no = int(input('--- 수정할 게시물 번호를 입력해주세요 : '))
                exist_rs = self.is_exist_article(artc_no)
                if exist_rs :
                    if self.is_my_article(exist_rs, user) :
                        upd_key = input('--- 게시물 수정 항목을 입력해주세요 : ')
                        upd_val = input('--- 수정할 내용을 입력해주세요 : ')
                        if upd_key != '번호' and upd_key != '작성자' :
                            self.update_article(article, upd_key, upd_val)

            elif cmd == '4':
                print('\n▷ 게시물삭제 모드')

            elif cmd == '5':
                print('-- 로그아웃')
                break


pyBoard = pyBoard()