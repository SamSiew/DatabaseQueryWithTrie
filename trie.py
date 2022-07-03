class NumberTrieNode:
    # Trie node class for numbers
    def __init__(self):
        self.children = [None] * 11
        self.recordIndex = None

class CharTrieNode:
    # Trie node class for character
    def __init__(self):
        self.children = [None] * 53
        self.recordIndex = None

class SuffixTrieNode:
    # Trie node class for suffix string
    def __init__(self):
        self.children = [None] * 27

class PrefixTrie:

    # Trie data structure class
    def __init__(self):
        self.lName = CharTrieNode()
        self.iD = NumberTrieNode()

    def insert(self, array, recIndex):
        """
        take in array  which consist of information about records and the index of
        records in dictionary and insert last name, identification and index
        to trie.

        Time complexity: Best: O(T)
                         Worst: O(T)

        Best Case == Worst Case, T times is needed to insert number of characters in identification numbers
        and number of characters in last names and no early termination to insert.

        Space complexity: Best: O(T)
                          Worst: O(T)

        Best Case == Worst Case, T Memory space is needed to insert
        number of characters in identification numbers and number of characters in last names and
        no way to save amount of memory space

        where T is the number of characters in identification numbers and last names

        Error handle: Nothing
        :param array: list of information for a particular records
        :return: Nothing
        Precondition: array be a list of non-empty information
        """
        #get lnamenode
        lNameNode = self.lName
        #get length of character length
        charLength = len(array[3])
        #for each level in character trie
        for level in range(charLength):
            # if character in lastname is lowercase,
            # get the index by ascii code - asciicode('a') + size of all alphabet
            if ord(array[3][level]) > 90:
                index = ord(array[3][level]) - 97 + 26
            # get the index by ascii code - asciicode('A')
            else:
                index = ord(array[3][level]) - 65
            # if current character Node is not present,
            # create a new node for character on the index
            # it was on.
            if lNameNode.children[index] == None:
                lNameNode.children[index] = CharTrieNode()
            # if list of record index is none
            # add list with record index into lNameNode.recordIndex
            if lNameNode.recordIndex == None:
                lNameNode.recordIndex = [recIndex]
            #add list with record index into lNameNode.recordIndex
            else:
                lNameNode.recordIndex.append(recIndex)
            #go to next node
            lNameNode = lNameNode.children[index]
        #mark the 52 as true at last node, for being a leaf
        if lNameNode.children[52] == None:
            lNameNode.children[52] = True
        # if list of record index is none
        # add list with record index into lNameNode.recordIndex
        if lNameNode.recordIndex == None:
            lNameNode.recordIndex = [recIndex]
        # add list with record index into lNameNode.recordIndex
        else:
            lNameNode.recordIndex.append(recIndex)
        # get id node
        iDNode = self.iD
        # get length of number string length
        numberLength = len(array[1])
        # for each level in number trie
        for level in range(numberLength):
            # get the index by ascii code - asciicode('0')
            index = ord(array[1][level]) - ord('0')
            # if current character Node is not present,
            # create a new node for character on the index
            # it was on.
            if iDNode.children[index] == None:
                iDNode.children[index] = NumberTrieNode()
            # if list of record index is none
            # add list with record index into lNameNode.recordIndex
            if iDNode.recordIndex == None:
                iDNode.recordIndex = [recIndex]
            # add list with record index into lNameNode.recordIndex
            else:
                iDNode.recordIndex.append(recIndex)
            # go to next node
            iDNode = iDNode.children[index]
        # mark the 10 as true at last node, for being a leaf
        if iDNode.children[10] == None:
            iDNode.children[10] = True
        # if list of record index is none
        # add list with record index into lNameNode.recordIndex
        if iDNode.recordIndex == None:
            iDNode.recordIndex = [recIndex]
        # add list with record index into lNameNode.recordIndex
        else:
            iDNode.recordIndex.append(recIndex)

    def query(self, intKey, charKey):
        """
        get the list index of record in dictionary where the index reference to
        records that have lastname and identification that have prefix
        lastname and prefix identification both matches

        Time complexity: Best: O(L)

                         Worst: O(k + L + i + n)

        Best Case: occurs when last name prefix do not match any prefix name of trie,
                   therefore early termination occurs on when first trie condition is not met

        Worst Case: occurs when there is any records that matches both prefix last name
                     and identification.last name prefix matches any prefix name of lastname trie which takes L time,
                     this function will then takes k times to retrieve prefix number of identification of trie
                     then (i + n) times is needed to find overlapping index of both trie.
                     Thus, it requires O(k + L + i + n) time in result

        Space complexity: Best: O(k + L)

                          Worst: O(k + L + i + n)

        Best Case: occurs when last name prefix do not match any prefix name of trie, but
                    k memory space and L memory space is needed to store parameter prefix identification
                    and prefix last name respectively. ThusL, O(k + L)

        Worst Case:   k memory space and L memory space is needed to store parameter prefix identification
                      and prefix last name respectively. Then, (i + n) space is needed to store the overlapping
                      index of prefix matching for lname and identification. In the end, O(k + L + i + n) space memory
                      is needed to get retrieve index that matches both prefix last name
                      and prefix identification

        where k is the length of id_prefix, L is the length of last_name_prefix, i is the number of records
        matching the id_prefix and n the number of records matching the last_name_prefix

        Error handle: when file does not exist, it will return empty
        :param intKey:
        :param charKey:
        :return: list of indices
        Precondition: filename must contains only one string and it must exist.
        """

        #get root of lname root
        lNameNode = self.lName
        #get length of character string
        length = len(charKey)
        #for each character of string,
        #check if the ascii code is > 90:
        #  True: retrieve index by ascii code - ascii code of 'a' + size of alphabet
        #  False: retrieve index by ascii code - ascii code of 'A'
        for level in range(length):
            # if the ascii code is > 90('a-z'):
            if ord(charKey[level]) > 90:
                index = ord(charKey[level]) - 97 + 26
            # if the ascii code is <= 90('A-Z'):
            else:
                index = ord(charKey[level]) - 65
            #  when index that just compute is not in trie, return empty list
            if lNameNode.children[index] == None:
                return []
            lNameNode = lNameNode.children[index]
        # number Length of a integer string
        numberLength = len(intKey)
        # get ID trie Node
        iDNode = self.iD
        # iterate all character in number string
        for level in range(numberLength):
            #get node by index of number's character
            index = ord(intKey[level]) - ord('0')
            # if current character is not present
            if iDNode.children[index] == None:
                #return empty
                return []
            iDNode = iDNode.children[index]

        bucket = []

        lPointer , kPointer = 0 , 0
        # while lpointer < size of lnodearray and kpointer < size of knodearray:
        # if both item on pointer in lnodearray and knodearray is same:
        #   add item from any of the nodeArray
        #   increase by 1 for pointer in lnodearray
        #   increase by 1 for pointer in knodearray
        # otherwise:
        #   if pointer in lnodearray < pointer in knodearray:
        #       increase by 1 for pointer in lnodearray
        #   else:
        #       increase by 1 for pointer in knodearray
        # increment pointer is done to go to next element
        while lPointer < len(lNameNode.recordIndex) and kPointer < len(iDNode.recordIndex):
            # both item on pointer in lnodearray and knodearray is same
            if lNameNode.recordIndex[lPointer] == iDNode.recordIndex[kPointer]:
                # add item from any of the nodeArray
                bucket.append(lNameNode.recordIndex[lPointer])
                # increase by 1 for pointer in lnodearray
                # increase by 1 for pointer in knodearray
                lPointer = lPointer + 1
                kPointer = kPointer + 1
            #if pointer in lnodearray < pointer in knodearray:
            elif lNameNode.recordIndex[lPointer] < iDNode.recordIndex[kPointer]:
                # increase by 1 for pointer in lnodearray
                lPointer = lPointer + 1
            #else
            else:
                # increase by 1 for pointer in knodearray
                kPointer = kPointer + 1

        return bucket

class SuffixTrie:

    # Trie data structure class
    def __init__(self):
        self.root = SuffixTrieNode()

    def reverseInsert(self, key):
        """
        construct suffix trie for a reverse substring for
        that string.

        Time complexity: Best: O(K^2)
                         Worst: O(K^2)

        Best case == Worst Case, no matter what, each substring in reverse which start
        from last character of input string till first character of
        words(excluding substring with one character only) will need to be inserted to trie if they
        are not in trie yet and there is no early termination.

        Space complexity: Best: O(K)
                          Worst: O(K^2)

        Best Case : occurs when input string consist of only one character regardless of its length.
        For example, input string 'aaaa'. it only require k space to fit all substring  of input string.

        Worst Case: occurs when every substring of input string needs to build new node to create memory of
        each substring. This usually happens when each substring consist of different character.

        where K is the total number of characters in the input string

        Error handle: Nothing
        :param key: input string
        :return: None
        Precondition: parameter key must be string
        """
        #for each substring in input string starting N-1....1
        for eachSub in range(len(key)-1,0,-1):
            currentNode = self.root
            #for each length of a substrings of input string,
            #if current node for current character index in trie array is none,
            #create a new node
            for level in range(eachSub,-1,-1):
                #get index of character in input string
                index = ord(key[level]) - ord('a')
                # if current character is not present
                if currentNode.children[index] == None:
                    #create suffix trie node on a item in trie array
                    currentNode.children[index] = SuffixTrieNode()
                #go to next node in trie array
                currentNode = currentNode.children[index]
            # mark last node as leaf
            currentNode.children[26] = True

    def query(self, key):
        """
        get all the substring of param key which have reverse substring which is
        also a substrings in the suffix trie.

        Time complexity: Best: O(K)
                         Worst: O(K^2 + P)

        Best Case : occurs when every substring of input string consist of different character  regardless of its length
        which causes it to terminates the inner loops in the for loops 1..N at each iteration because
        it cannot continue from first or second character of substring in input string and therefore, leading
        empty list as output due to no substring which reverse is also a substring of input string. Consider 'abcde' which
        will return empty list.

        Worst Case: occurs when every substring of input string has a reverse in the string and P times is require to
        store each substring  in list since the algorithm is output-sensitive.

        Space complexity: Best: O(K)
                          Worst: O(K + P)

        Best Case: occurs when every substring of input string consist of different character regardless of its length
        where none of substring with its reverse is a substring in input string which causes empty list as output
        due to no substring which reverse is also a substring of input string.
        Consider 'abcde' which will return empty list and it requires k space to store input string and substring of
        input string.

        Worst Case: it requires k space for input string and substring of input string, and
        p space to store total length of all substrings whose reverse appears in the string

        where K is total length of all substrings and P is the total length of all substrings whose reverse appears in the string.

        Error handle: None
        :param key: input string
        :return: list, lists of lists, where each inner list will contain two values. The rst value will be a
        substring with length > 1 whose reverse exists in the string, and the second value will be the
        index of that substring in the input text.

        Precondition: key must be a string.
        """
        #bucket will temporary store list of substring by [last index of substring,start index of substring]
        bucket = []
        #for each character in input string
        for eachSub in range(len(key)-1):
            #store the node of root for suffix trie into a variable
            currentNode = self.root
            # for each level of substring using a pointer ,
            # check if there is a node for character is in trie,
            # if true: bucket[] will only append the substring if they are length of 2.
            # if false: terminate inner loops because we knows there is no way to continue if
            # first few character is already not in trie.
            for level in range(eachSub,len(key)):
                # get index of character in input string
                index = ord(key[level]) - ord('a')
                #check if there is a node for character of substring in trie
                if currentNode.children[index] != None:
                    if level - eachSub > 0:
                        bucket.append([level,eachSub])
                # if there is no node for the character terminate inner loops
                # and continue to next substring
                else:
                    break
                #go to next node.
                currentNode = currentNode.children[index]

        # reconstruct the bucket from[last index of substring, start index of substring]
        # into [substring, start index of substring]
        for sub in range(len(bucket)):
            # get integer value of start index of substring
            startIndex = bucket[sub][1]
            # get integer value of last index of substring
            endIndex = bucket[sub][0]
            # change first value into string
            bucket[sub][0] = ""
            #copy substring into bucket
            for subIndex in range(startIndex,endIndex+1):
                bucket[sub][0] += key[subIndex]

        return bucket

def query(filename,id_prefix, last_name_prefix):
    """
    read in file, construct a prefix trie and does a query on id prefix and last name prefix
    and it will returns list of record index that matches id prefix and last name prefix on its records

    Time complexity: Best: O(NM + T + L)

                     Worst: O(NM + T + (k + L + i + n))

    Best Case:  O(NM + T) time is needed no matter what because NM time is needed to read in file and T time
                is needed to construct trie for all record consisting lastname and identification
                in database file.Best Case occurs when last name prefix do not match any prefix name of trie in query operation,
                therefore early termination occurs on when first trie condition is not met. Thus,
                resulting O(NM + T + L) time

    Worst Case:  O(NM + T) time is needed no matter what because NM time is needed to read in file and T time
                 is needed to construct trie for all record consisting lastname and identification
                 in database file. Worst Case occurs when there is any records that matches both prefix last name
                 and identification.last name prefix matches any prefix name of lastname trie which takes L time,
                 this function will then takes k times to retrieve number of prefix of identification of trie
                 then (i + n) times is needed to find overlapping index of both trie.
                 Thus, it requires O(NM + T + (k + L + i + n)) time in result

    Space complexity: Best: O(NM + T + k + L)

                      Worst: O(NM + T + (k + L + i + n))

    Best Case:  O(NM + T) space is needed no matter what because NM space is needed to read in file and T space
                is needed to construct trie for all record consisting of all lastname and identification
                in database file. Best case occurs when last name prefix do not match any prefix name of trie, but
                k memory space and L memory space is needed to store parameter prefix identification
                and prefix last name respectively. Thus, resulting O(NM + T + k + L)

    Worst Case:   O(NM + T) space is needed no matter what because NM space is needed to read in file and T space
                  is needed to construct trie for all record consisting of all lastname and identification
                  in database file.Worst Case occurs when k memory space and L memory space is needed to store
                  parameter prefix identification and prefix last name respectively. Then, (i + n) space is needed to
                  store the overlapping index of prefix matching for lname and identification.
                  In the end, O(NM + T + k + L + i + n) space memory is needed to get retrieve index that matches both prefix last name
                  zand prefix identification

    where k is the length of id_prefix, L is the length of last_name_prefix, T is the number of
    characters in all identification numbers and all last names, i is the number of records
    matching the id_prefix and n the number of records matching the last_name_prefix

    Error handle: when file does not exist, it will return empty

    :param filename: file name of a file to be read in
    :param id_prefix: prefix identification
    :param last_name_prefix: prefix last name
    :return: list of indices

    Precondition: filename must be a string, file must exist and each record should not be empty or any empty information.
    """
    # try to read in file into dictionary[] where dictionary is
    # list of records[] and records[] stores
    # [Record_index,Identification_no,First_name,Last_name, Phone_number, Email_address]
    try:
        with open(filename) as file:
            dictionary = []
            for line in file:
                record = []
                currentString = ""
                for char in line:
                    if ord(char) == 32 or ord(char) == 10:
                        if len(currentString) != 0:
                            record.append(currentString)
                        currentString = ""
                    else:
                        currentString += char
                if len(record) != 0:
                    dictionary.append(record)
            file.close()
    except:
        return []
    #create empty prefix trie.
    newTrie = PrefixTrie()

    # ensure identification be a string
    id_prefix = str(id_prefix)
    #ensure last name be a string
    last_name_prefix = str(last_name_prefix)

    # insert each records from dictionary with actual index of records in dictionary
    # into trie
    for recIndex in range(len(dictionary)):
        newTrie.insert(dictionary[recIndex], recIndex)
    # get list of indices that references to actual index of record in dictionary where
    # list of indices is a indices of records in dictionary that matches both
    # prefix of identification and last name.
    bucket = newTrie.query(id_prefix, last_name_prefix)
    #reconstruct the actual record Index based on index of records stored in dictionary.
    for eachIndex in range(len(bucket)):
        bucket[eachIndex] = int(dictionary[bucket[eachIndex]][0])
    return bucket

def reverseSubstrings(filename):
    """
    read in file, construct a suffix trie on string in file and
    perform query for each substring wheather it has a reverse that is also
    a substring in string.

    Time complexity: Best: O(K^2)
                     Worst: O(K^2 + P)

    Best Case : occurs when every substring of input string is not a palindrome regardless of its length
    which leads to empty list as output due to none of substring have its reverse which
    is also a substring of input string where P space is as close as O(1) and
    K^2 times is needed to check if substrings is in trie where no early termination can be done.
    Consider 'abcde' which will return empty list.

    Worst Case: occurs when every substring of input string is a palindrome, K^2 times is needed
    to insert all substring into trie regardless if it needs to create a new node or not and
    P times is require to store each substring into list since the algorithm is output-sensitive.

    Space complexity:  Best: O(K + P) or O(K^2)
                       Worst: O(K^2 + P)

    Best Case: occurs when every substring of input string consist of single character regardless of its length
    but it requires P space to store all substrings since every substring in that strings have its reverse in the input string.
    Thus, it does not need to create a new nodes for all substring except for its longest substring which leads K space for longest
    substring in string. For examples, ‘aaaa’ will have ‘aaaa’ inserted and rest of substring is already in trie.
    There's another scenario that none of substring with its reverse is a substring in input string which causes
    empty list as output due to none of substring which reverse is also a substring of input string but k^2 space is needed to
    store input string and store into trie. However, the two case can’t be on simultaneously event which result O(K + P) or O(K^2).

    Worst Case: occurs when every substring of input string needs to build new node to create memory of
    each substring. This usually happens when each substring is a palindrome.
    it requires k^2 space for all substring of input string to store into trie, and
    P space to store total length of all substrings whose reverse appears in the string

    where K is the total number of characters in the input string and
    P is the total length of all substrings whose reverse appears in the string.

    Error handle: when file does not exist, it will return empty

    :return: bucket, list of [substring, index of first character of substring]
    :param filename: file refers to filename to read in

    Precondition: filename must contains only one string and it must exist.
    """
    #read in file content into a variable that store the input string.
    try:
        with open(filename) as file:
            string = ""
            for line in file:
                string = line.strip()
            file.close()
    except:
        return []
    #create suffix trie
    newTrie = SuffixTrie()
    # reverse insert all substrings of input string starting from last character
    # N...1 till first character of string
    newTrie.reverseInsert(string)
    #store result of query for string when it determines all substring
    #that has a reverse also a substrings
    bucket = newTrie.query(string)

    return bucket

if __name__ == '__main__':
    print("TASK-1:")
    dictFile = "databaseMod.txt"
    id_prefix = ""
    lname_prefix = ""
    print("---------------------------------------------------------------------")
    print("Enter the file name of the query database :", dictFile)
    print("Enter the prefix of the identification number:",id_prefix)
    print("Enter the prefix of the last name :",lname_prefix)
    print("---------------------------------------------------------------------")
    recList = query(dictFile, id_prefix, lname_prefix)
    print(len(recList),"record found")
    for item in recList:
        print("Index number :",item)
    print("---------------------------------------------------------------------")
    print("TASK-2:")
    filename = "string.txt"
    print("Enter the file name for searching reverse substring:",filename)
    print("---------------------------------------------------------------------")
    recList = reverseSubstrings(filename)
    current = ""
    length = 0
    for item,index in recList:
        current += item + "("+str(index)+")"
        length += 1
        if length < len(recList):
            current += ", "
    print(current)
    print("---------------------------------------------------------------------")
    print("Program end")