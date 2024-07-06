import pickle


def classifydata(data):
    print(data)
    type = data[0]
    print(type)

    if 'card info' in type:
        rawcardinfo = info[1]
        print(rawcardinfo)


    else:
        print('test')









#encryption methods

















if __name__ == '__main__':
    with open('data.pickle', 'rb') as f:
        info = pickle.load(f)
        info = info
    classifydata(info)


