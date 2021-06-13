import copy
class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node("*")

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = Node(letter)
            curr_node = curr_node.children[letter]
        curr_node.is_end_of_word= True
    def search_word(self, word):
        if word == "":
            return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.is_end_of_word

trie = Trie()
trrie=Trie()

#Convert txt dictionaries to list
positive=open("positiveword.txt")
negative=open("negativeword.txt")
ptive=list()
ntive=list()
ptent=positive.read()
ntent=negative.read()
ptive=ptent.split(", ")
ntive=ntent.split(", ")
pw=list()
nw=list()

#Add words to Trie
for w in ptive:
    trie.add_word(w)
for w in ntive:
    trrie.add_word(w)
    
#courier=['CityLinkResult.txt', 'PosLajuResult.txt', 'GDEXResult.txt', 'JnTResult.txt', 'DHLResult.txt']
#courier=["citylinkresults.txt","poslajuresults.txt","gdexresults.txt","jntresults.txt","dhlresults.txt"]

def mainCountPN(couriers):
    for i in couriers:
        count=[0,0,0]
        w=list()
        for k in i:
            c=k.find("'")
            d=k.find("'",c+1)
            e=k[c+1:d]
            w.append(e)      
        #Test words in result file from list (positive)
        #print(i)
        for j in w:
            found=trie.search_word(j)
            if found is True:
                count[0]+=1
                #print("p",count[0])
            else:
                #Test words in result file from list (negative)
                found=trrie.search_word(j)
                if found is True:
                    count[1]+=1
                    #print("n",count[1])
                else:
                    count[2]+=1
                        #print("neu",count[2])
        #Add the number of Postive (count[0]), Negative (count[1]), Neutral (count[2]) as list
        pw.append(count[0])
        nw.append(count[1])
        pww = copy.deepcopy(pw)
        nww = copy.deepcopy(nw)

    print("The total of positive words in the article:",pw)
    print("The total of negative words in the article:",nw)


#Update CountPN (for Positive Word Histogram)
    with open(r'CountPN.csv','w',encoding='UTF8',newline='') as updte:
        writer = csv.writer(updte)
        header = ['Positive_word']
        data = ['1','2','3','4','5']
        writer.writerow(header)
        for x in range (len(pww)):
            while pww[x]!= 0:
                writer.writerow(data[x])
                pww[x]-=1
            x+=1

#Update CountNPN (for Negative Word Histogram)
    with open(r'CountNPN.csv','w',encoding='UTF8',newline='') as updte2:
        writer2 = csv.writer(updte2)
        header2 = ['Negative_word']
        data2 = ['1','2','3','4','5']
        writer2.writerow(header2)
        for z in range (len(nww)):
            while nww[z]!= 0:
                writer2.writerow(data2[z])
                nww[z]-=1
            z+=1



#print result to txt
txtfile=open("resultCountPN.txt","w")
txtfile.write(str(pw))
txtfile.write("\n")
txtfile.write(str(nw))
txtfile.close()
    
#Print to CSV
import csv
field=["City Link","Pos Laju","GDex","JnT","DHL"]
csvfile=open("CountPNResult","a")
write=csv.writer(csvfile)
write.writerow(field)
write.writerow(pw)
write.writerow(nw)



