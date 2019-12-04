import csv

give_dict={0:"PER",1:"LOC",2:"ORG",3:"MISC"}

def parseLabels(content,*args):
    out=[]
    for seq in range (4):
        if args[seq]!="":
            words=[word.strip() for word in args[seq].split(";")]
            for word in words:
                single_words=word.split(" ")
                for word_seq in range(len(single_words)):
                    curr_word=single_words[word_seq]
                    if word_seq ==0:
                        out.append((content.find(curr_word),len(curr_word),"B-"+give_dict[seq]))
                    else:
                        out.append((content.find(curr_word),len(curr_word),"I-"+give_dict[seq]))
    return out

def dataparser(data):
    content,PER,LOC,ORG,MISC=data[2][1:],data[6],data[7],data[8],data[9]
    return (content,parseLabels(content,PER,LOC,ORG,MISC))


with open('NER_title_1.csv') as csvfile:
    book = csv.reader(csvfile)
    train_data=[]
    for row in book:
        train_data.append(dataparser(row)) if row[0]!="Annotator"  else None
print(train_data)




