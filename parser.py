import csv
import re

give_dict={0:"PER",1:"LOC",2:"ORG",3:"MISC"}


def parseLabels(content,*args):
    out=[]
    auxi=[]
    for seq in range (4):
        if args[seq]!="":
            words=[word.strip() for word in args[seq].split(";")]
            for word in words:
                single_words=word.split(" ")
                word_length= list(map(len,single_words))

                all_start=[m.start() for m in re.finditer(word, content) if m.start() not in auxi]

                for start in all_start:
                    temp_start=start
                    count=0
                    for length in word_length:
                        custom = "B-" if count==0 else "I-"
                        out.append((temp_start,temp_start+length,custom+give_dict[seq]))
                        auxi.append(temp_start)
                        temp_start+=length+1
                        count+=1
## mistakes find er
            for word in words:
                single_words=word.split(" ")
                
                for word_seq in range(len(single_words)):
                    curr_word=single_words[word_seq]
                    kappa=content.count(curr_word)
                    if kappa==0:
                        print(content,content.count(curr_word),words)

    return out

def dataparser(data):
    content,PER,LOC,ORG,MISC=data[2][1:],data[6],data[7],data[8],data[9]
    return (content,parseLabels(content,PER,LOC,ORG,MISC))


def selectfiles(fname):
    with open(fname) as csvfile:
        book = csv.reader(csvfile)
        train_data=[]
        for row in book:
            train_data.append(dataparser(row)) if row[0]!="Annotator"  else None
    return train_data


files=['NER_title_1.csv','NER_title_2.csv',"NER_mass_1","NER_mass_2","NER_mass_3"]
print(selectfiles(files[1]))




