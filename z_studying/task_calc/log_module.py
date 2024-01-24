import datetime

def log_time(original_function):

    def logging(*args, **kwargs):
        self, other = args
        error_code = kwargs.get('error_code')
        with open('log.txt', 'a', encoding='utf-8') as file:
            # error_code가 없다면
            if not error_code:
                result = original_function(*args, **kwargs)
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # 나눗셈이라면
                if self.oper == '/':
                    value, rest = result
                    file.write(f'{self.number} {self.oper} {other} = {value}, {rest}\tKST{now}\n')
                else:
                    file.write(f'{self.number} {self.oper} {other} = {result}\tKST{now}\n')

                #연산 결과 리턴
                return result
            else:
                #error code가 있을떄 아래형식으로 log 파일 작성
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f'{error_code}\tKST{now}\n')
        #errorcode있으면 none 리턴
        return None
    return logging