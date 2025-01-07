#finalproject.py


import math
def clean_text(txt):
    """ This function takes a string of text txt as a parameter and returns a 
        list containing the words in txt after all punctuation has been removed
    """
    txt=txt.lower()
    for i in txt:
        if i in """.,?"'!;:""":
            txt=txt.replace(i,'')
    x=txt.split()
    return x

def stem(s):
    """ This function accepts a string as a parameter and then returns the 
        stem of s
    """
    if s[-2:]=='es' and len(s)>4:
        s = s[:-2]
    elif s[-2:]=='ed' and len(s)>4:
        s = s[:-2]
    elif s[-1]=='s' and len(s)>3:
        s = s[:-1]
    elif s[-3:]=='ing' and len(s)>5:
        if s[-4]==s[-5]:
            s=s[:-4]
        else:
            s=s[:-3]
    elif s[-2:]=='er' or s[-2:]=='ly' and len(s)>5:
            s=s[:-3]
    elif s[-1]=='y':
        s=s[:-1]+'i'
    elif s[-3:]=='ful' and len(s)>5:
        s=s[:-3]
    if s[:2]=='un' and len(s)>4:
        s=s[2:]
    if s[:2]=='en' and len(s)>4:
        s=s[2:]
    if s[:3]=='dis' and len(s)>5:
        s=s[3:]
    return s

def compare_dictionaries(d1,d2):
    """ This function takes two feature dictionaries d1 and d2 as inputs and 
        computes and returns their log similarity score
    """
    if d1=={}:
        return -50
    score=0
    total=0
    for i in d1:
        total+=d1[i]
    for j in d2:
        if j in d1:
            score+= math.log(d1[j]/total)*d2[j]
        else:
            score+=math.log(0.5/total)*d2[j]
    return score

class TextModel():
    """ This class will serve as a blueprint for objects that model a body of 
        text 
    """
    def __init__(self, model_name):
        """ This function constructs a new TextModel object 
        """
        self.name=model_name
        self.words={}
        self.word_lengths={}
        self.stems={}
        self.sentence_lengths={}
        self.punctuations={}
        
    def __repr__(self):
        """ This function returns a string that includes the name of the model 
            as well as the sizes of the dictionaries for each feature of the 
            text.
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuations: ' + str(len(self.punctuations)) + '\n'
        return s
    
    def add_string(self, s):
        """ Analyzes the string txt and adds its pieces
            to all of the dictionaries in this text model.
        """
        word_list = clean_text(s)
        for w in word_list:
            if w not in self.words:
                self.words[w]=1
            else:
                self.words[w]+=1
        for word in word_list:
            l=len(word)
            if l not in self.word_lengths:
                self.word_lengths[l]=1
            else:

                self.word_lengths[l]+=1
        for word in word_list:
            stemmed_word=stem(word)
            if stemmed_word not in self.stems:
                self.stems[stemmed_word]=1
            else:
                self.stems[stemmed_word]+=1
        x=s.split()
        length=0
        for i in x:
            if i[-1] not in '.?!':
                length+=1
            else:
                length+=1
                if length in self.sentence_lengths:
                    self.sentence_lengths[length]+=1
                    length=0
                else:
                    self.sentence_lengths[length]=1
                    length=0
        for j in x:
            if j[-1] in """.,?"'!;:""":
                if j[-1] not in self.punctuations:
                    self.punctuations[j[-1]]=1
                else:
                    self.punctuations[j[-1]]+=1
                    
    def add_file(self, filename):
        """ This function adds all of the text in the file identified by 
            filename to the model.
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        x=f.read()
        f.close()
        self.add_string(x)
        
    
    def save_model(self):
        """ This function saves the TextModel object self by writing its 
            various feature dictionaries to files. 
        """
        f1=open(str(self.name) + '_' + 'words' + '.txt','w')
        f1.write(str(self.words))
        f1.close()
        f2=open(str(self.name) + '_' + "word_lengths" + '.txt','w')
        f2.write(str(self.word_lengths))
        f2.close()
        f3=open(str(self.name) + '_' + "stems" + '.txt','w')
        f3.write(str(self.stems))
        f3.close()
        f4=open(str(self.name) + '_' + "sentence_lengths" + '.txt','w')
        f4.write(str(self.sentence_lengths))
        f4.close()
        f5=open(str(self.name) + '_' + "punctuations" + '.txt','w')
        f5.write(str(self.punctuations))
        f5.close()
        
    def read_model(self):
        """ This function reads the stored dictionaries for the called 
            TextModel object from their files and assigns them to the 
            attributes of the called TextModel.
        """
        f1=open(str(self.name) + '_' + 'words' + '.txt','r')
        d1=f1.read()
        d1_dict=dict(eval(d1))
        self.words=d1_dict
        f1.close()
        f2=open(str(self.name) + '_' + "word_lengths" + '.txt','r')
        d2=f2.read()
        d2_dict=dict(eval(d2))
        self.word_lengths=d2_dict
        f2.close()
        f3=open(str(self.name) + '_' + "stems" + '.txt','r')
        d3=f3.read()
        d3_dict=dict(eval(d3))
        self.stems=d3_dict
        f3.close()
        f4=open(str(self.name) + '_' + "sentence_lengths" + '.txt','r')
        d4=f4.read()
        d4_dict=dict(eval(d4))
        self.sentence_lengths=d4_dict
        f5=open(str(self.name) + '_' + "punctuations" + '.txt','r')
        d5=f5.read()
        d5_dict=dict(eval(d5))
        self.punctuations=d5_dict
        
    def similarity_scores(self, other):
        """ This function computes and returns a list of log similarity 
            scores measuring the similarity of self and other
        """
        word_score=compare_dictionaries(other.words,self.words)
        word_lengths_score=compare_dictionaries(other.word_lengths,self.word_lengths)
        stems_score=compare_dictionaries(other.stems,self.stems)
        sentence_lengths_score=compare_dictionaries(other.sentence_lengths,self.sentence_lengths)
        punctuations_score=compare_dictionaries(other.punctuations,self.punctuations)
        scores=[word_score,word_lengths_score,stems_score,sentence_lengths_score,punctuations_score]
        return scores
        
    def classify(self, source1, source2):
        """ This function compares the called TextModel object (self) to 
            two other “source” TextModel objects (source1 and source2) and 
            determines which of these other TextModels is the more likely 
            source of the called TextModel.
        """
        scores1=self.similarity_scores(source1)
        scores2=self.similarity_scores(source2)
        print("scores for",source1.name,':', scores1)
        print("scores for",source2.name, ':', scores2)
        weighted_sum1=10*scores1[0] + 5*scores1[1] + 7*scores1[2] + 10*scores1[3] + 7*scores1[4]
        weighted_sum2=10*scores2[0] + 5*scores2[1] + 7*scores2[2] + 10*scores2[3] + 7*scores2[4]
        if weighted_sum1>weighted_sum2:
            print(self.name,"is more likely to come from", source1.name)
        else:
            print(self.name,"is more likely to come from", source2.name)
            
            
def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)           


def run_tests():
    """ This function tests our project"""
    source1 = TextModel('rowling')
    source1.add_file('rowling_source_text.txt')

    source2 = TextModel('shakespeare')
    source2.add_file('shakespeare_source_text.txt')
    
    new1 = TextModel('rowling(excerpt)')
    new1.add_file('rowling_comparison_source_text.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('shakespeare(excerpt)')
    new2.add_file('shakespeare_comparison_source_text.txt')
    new2.classify(source1, source2)

    new3 = TextModel('wr112')
    new3.add_file('wr112_source_text.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('Tolkien')
    new4.add_file('tolkien_source_text.txt')
    new4.classify(source1, source2)
    
    
