from trie import *

def testQuery(filename,id_prefix,last_name_prefix,true_result):
    try:
        test_result = query(filename,id_prefix,last_name_prefix)
    except:
        return ['CRASHED',[]]
    else:
        for i in range(len(test_result)):
            test_result[i] = int(test_result[i])
        test_result = sorted(test_result)
        try:
            assert len(test_result) == len(true_result)
        except AssertionError:
            return ['FAILED',[]]
        else:
            temp = []
            for i in range(len(true_result)):
                try:
                    assert test_result[i] == true_result[i]
                except AssertionError:
                    temp.append(true_result[i])
            if not temp:
                return ['PASSED',[]]
            else:
                return ['FAILED',temp]

def testReverseSubstrings(filename,true_result):
    try:
        test_result = reverseSubstrings(filename)
    except:
        return ['CRASHED',[]]
    else:
        try:
            assert len(test_result) == len(true_result)
        except AssertionError:
            return ['FAILED',[]]
        else:
            temp = []
            for i in range(len(true_result)):
                matched = False
                for j in range(len(test_result)):
                    if test_result[j] == true_result[i]:
                        matched = True
                if not matched:
                    temp.append(true_result[i])
            if not temp:
                return ['PASSED',[]]
            else:
                return ['FAILED',temp]

def trueRead(filename):
    file = open(filename)
    string = file.read().split('TEXT')
    for i in range(1,len(string)):
        string[i] = string[i].split('\n')
    return string
        
def trueReadTask1(filename):
    string = trueRead(filename)
    for i in range(len(string)):
        temp = []
        for j in range(len(string[i])):
            if string[i][j] != '':
                temp.append(int(string[i][j]))
        string[i] = sorted(temp)
    return (string[1:])

def trueReadTask2(filename):
    string = trueRead(filename)
    for i in range(len(string)):
        temp = []
        for j in range(len(string[i])):
            if string[i][j] != '':
                x = string[i][j].split(' ')
                temp.append([x[0],int(x[1])])
        string[i] = temp
    return (string[1:])

def testTask1():
    true_result = trueReadTask1('input\Task-1_text.txt')
    id_prefix = ['123','284','92','50','16801']
    last_name_prefix = ['Wil','Ne','D','Ri','Edw']

    for i in range(5):
        result = testQuery('Database.txt',id_prefix[i],last_name_prefix[i],true_result[i])
        string = ''
        if result[1]:
            string += '\nNOT FOUND INDICES : '
            for j in range(len(result[1])):
                string += str(result[1][j])+' '
        print('TEST CASE -',i+1,': id_prefix :',id_prefix[i],'last_name_prefix :',last_name_prefix[i],'\nOUTCOME :',result[0],string)

def testTask1b():
    true_result = trueReadTask1('input\Task-1b_text.txt')
    id_prefix = ['','','','019','019','019','0123456789','0123456789']
    last_name_prefix = ['','Allison','Zimmerman','','Ho','Hood','','Zimm']

    for i in range(len(id_prefix)):
        result = testQuery('DatabaseMod.txt',id_prefix[i],last_name_prefix[i],true_result[i])
        string = ''
        if result[1]:
            string += '\nNOT FOUND INDICES : '
            for j in range(len(result[1])):
                string += str(result[1][j])+' '
        print('TEST CASE -',i+6,': id_prefix :',id_prefix[i],'last_name_prefix :',last_name_prefix[i],'\nOUTCOME :',result[0],string)

def testTask2():
    true_result = trueReadTask2('input\Task-2_text.txt')

    filename = ['T2_S1.txt','T2_S2.txt','T2_S3.txt','T2_S4.txt','T2_S5.txt']
    for i in range(5):
        result = testReverseSubstrings("input\\"+filename[i],true_result[i])
        string = ''
        if result[1]:
            string += '\nNOT FOUND ITEMS : '
            for j in range(len(result[1])):
                string += str(result[1][j])+' '
        original = open("input\\"+filename[i]).read()
        print('TEST CASE -',i+1,' :',original,'\nOUTCOME :',result[0],string)

def testTask2b():
    true_result = trueReadTask2('input\Task-2_text.txt')
    true_result.append([['aa',0], ['aa',1], ['aa',2], ['aa',3], ['aaa',0], ['aaa',1], ['aaa',2], ['aaaa',0], ['aaaa',1], ['aaaaa',0]])
    true_result.append([['abba',0], ['abb',0], ['bba',1], ['bb',1], ['bab',2], ['ab',0], ['ba',2], ['ab',3], ['ba',4],['aba',3]])
    true_result.append([['cdadc',0], ['cdad',0], ['cda',0], ['dadc',1], ['dad',1], ['adc',2], ['adc',5], ['cd',0], ['da',1], ['ad',2], ['dc',3], ['ad',5], ['dc',6]])
    true_result.append([['re', 0], ['rep', 0], ['repa', 0], ['repap', 0], ['repape', 0], ['repaper', 0], ['ep', 1], ['epa', 1], ['epap', 1], ['epape', 1], ['epaper', 1], ['pa', 2], ['pap', 2], ['pape', 2], ['paper', 2], ['ap', 3], ['ape', 3], ['aper', 3], ['pe', 4], ['per', 4], ['er', 5]])
    true_result.append([['sa', 0], ['sai', 0], ['saip', 0], ['saipp', 0], ['saippu', 0], ['saippua', 0], ['saippuak', 0], ['saippuaki', 0], ['saippuakiv', 0], ['saippuakivi', 0], ['saippuakivik', 0], ['saippuakivika', 0], ['saippuakivikau', 0], ['saippuakivikaup', 0], ['saippuakivikaupp', 0], ['saippuakivikauppi', 0], ['saippuakivikauppia', 0], ['saippuakivikauppias', 0], ['ai', 1], ['aip', 1], ['aipp', 1], ['aippu', 1], ['aippua', 1], ['aippuak', 1], ['aippuaki', 1], ['aippuakiv', 1], ['aippuakivi', 1], ['aippuakivik', 1], ['aippuakivika', 1], ['aippuakivikau', 1], ['aippuakivikaup', 1], ['aippuakivikaupp', 1], ['aippuakivikauppi', 1], ['aippuakivikauppia', 1], ['aippuakivikauppias', 1], ['ip', 2], ['ipp', 2], ['ippu', 2], ['ippua', 2], ['ippuak', 2], ['ippuaki', 2], ['ippuakiv', 2], ['ippuakivi', 2], ['ippuakivik', 2], ['ippuakivika', 2], ['ippuakivikau', 2], ['ippuakivikaup', 2], ['ippuakivikaupp', 2], ['ippuakivikauppi', 2], ['ippuakivikauppia', 2], ['ippuakivikauppias', 2], ['pp', 3], ['ppu', 3], ['ppua', 3], ['ppuak', 3], ['ppuaki', 3], ['ppuakiv', 3], ['ppuakivi', 3], ['ppuakivik', 3], ['ppuakivika', 3], ['ppuakivikau', 3], ['ppuakivikaup', 3], ['ppuakivikaupp', 3], ['ppuakivikauppi', 3], ['ppuakivikauppia', 3], ['ppuakivikauppias', 3], ['pu', 4], ['pua', 4], ['puak', 4], ['puaki', 4], ['puakiv', 4], ['puakivi', 4], ['puakivik', 4], ['puakivika', 4], ['puakivikau', 4], ['puakivikaup', 4], ['puakivikaupp', 4], ['puakivikauppi', 4], ['puakivikauppia', 4], ['puakivikauppias', 4], ['ua', 5], ['uak', 5], ['uaki', 5], ['uakiv', 5], ['uakivi', 5], ['uakivik', 5], ['uakivika', 5], ['uakivikau', 5], ['uakivikaup', 5], ['uakivikaupp', 5], ['uakivikauppi', 5], ['uakivikauppia', 5], ['uakivikauppias', 5], ['ak', 6], ['aki', 6], ['akiv', 6], ['akivi', 6], ['akivik', 6], ['akivika', 6], ['akivikau', 6], ['akivikaup', 6], ['akivikaupp', 6], ['akivikauppi', 6], ['akivikauppia', 6], ['akivikauppias', 6], ['ki', 7], ['kiv', 7], ['kivi', 7], ['kivik', 7], ['kivika', 7], ['kivikau', 7], ['kivikaup', 7], ['kivikaupp', 7], ['kivikauppi', 7], ['kivikauppia', 7], ['kivikauppias', 7], ['iv', 8], ['ivi', 8], ['ivik', 8], ['ivika', 8], ['ivikau', 8], ['ivikaup', 8], ['ivikaupp', 8], ['ivikauppi', 8], ['ivikauppia', 8], ['ivikauppias', 8], ['vi', 9], ['vik', 9], ['vika', 9], ['vikau', 9], ['vikaup', 9], ['vikaupp', 9], ['vikauppi', 9], ['vikauppia', 9], ['vikauppias', 9], ['ik', 10], ['ika', 10], ['ikau', 10], ['ikaup', 10], ['ikaupp', 10], ['ikauppi', 10], ['ikauppia', 10], ['ikauppias', 10], ['ka', 11], ['kau', 11], ['kaup', 11], ['kaupp', 11], ['kauppi', 11], ['kauppia', 11], ['kauppias', 11], ['au', 12], ['aup', 12], ['aupp', 12], ['auppi', 12], ['auppia', 12], ['auppias', 12], ['up', 13], ['upp', 13], ['uppi', 13], ['uppia', 13], ['uppias', 13], ['pp', 14], ['ppi', 14], ['ppia', 14], ['ppias', 14], ['pi', 15], ['pia', 15], ['pias', 15], ['ia', 16], ['ias', 16], ['as', 17]])
    true_result.append([])

    filename = ['T2_S1.txt','T2_S2.txt','T2_S3.txt','T2_S4.txt','T2_S5.txt','T2_S6.txt','T2_S7.txt','T2_S8.txt','T2_S9.txt','T2_S10.txt','T2_S11.txt']
    for i in range(len(filename)):
        result = testReverseSubstrings("input\\"+filename[i],true_result[i])
        string = ''
        if result[1]:
            string += '\nNOT FOUND ITEMS : '
            for j in range(len(result[1])):
                string += str(result[1][j])+' '
        original = open("input\\"+filename[i]).read()
        print('TEST CASE -',i+1,' :',original,'\nOUTCOME :',result[0],string)

if __name__ == '__main__':
    testTask1()
    testTask1b()
    testTask2()
    testTask2b()
        
    
