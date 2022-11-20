def find_answer(question):
    with open('Reply.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            # 字符串的分割
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply

        return False


if __name__ == '__main__':
    question = input('Hi,您好，小蜜在此等主人很久了,有什么烦恼快和小蜜说把！')
    while True:
        if question == 'bye':
            break
        # 开始在文件中查找
        answer = find_answer(question)
        if not answer:
            question = input('小蜜不知道你在说什么,你可以问一些关于订单,物流,账户,支付等问题,退出输入bye')
        else:
            print(answer)
            question = input('小主，您可以继续问，退出请输入bye')
