class Convert:    
    def __init__(self):
        self.processing()
        self.test()
        print "exiting"
        
    def LongestCommonSubstring(self, S1, S2):
        M = [[0]*(1+len(S2)) for i in xrange(1+len(S1))]
        longest, x_longest = 0, 0
        for x in xrange(1,1+len(S1)):
            for y in xrange(1,1+len(S2)):
                if S1[x-1] == S2[y-1]:
                    M[x][y] = M[x-1][y-1] + 1
                    if M[x][y]>longest:
                        longest = M[x][y]
                        x_longest  = x
                else:
                    M[x][y] = 0
        return S1[x_longest-longest: x_longest]
    
    def processing(self):
        file1 = open('C:\Users\Anjali Ashok\workspace\Stenography\src\\test.txt', 'r')
        file2 = open('C:\Users\Anjali Ashok\workspace\Stenography\src\\test1.txt', "r")
        file3 = open('C:\Users\Anjali Ashok\workspace\Stenography\src\\test2.txt', "w")
        
        list1 = file1.readlines()
        #for i in list1:
        #   thisline1 = i.strip().split(" ")
        
        ##print 'hello'   
        list2 = file2.readlines()
        for j in list2:
            thisline2 = j.strip().split(" ")
                
                    
        occured = []
        
        d = dict(x.strip().split(":") for x in list1)
        clean_d = { k.strip():v.strip() for k, v in d.iteritems()}
        
        c = self.LongestCommonSubstring('anfmfjali', 'anjali is');
        print c
        for m in list1:
            thisline1 = m.strip().split(" ")
            for x in thisline1:
                for y in thisline2:
                    if y.strip('.') in x:
                        if clean_d[y.strip('.')].strip() not in occured:
                            if(clean_d.has_key(y.strip('.'))):
                                file3.write(y.strip('.')+" : ")
                                file3.write(clean_d[y.strip('.')])
                                file3.write("\n")
                        occured.append(clean_d[y.strip('.')])
                    else:
                        continue
                    
        file1.close()
        file2.close()
        file3.close()
        
        
    def test(self):
        file1 = open('C:\Users\Anjali Ashok\workspace\Stenography\src\\test.txt', 'r')
        file2 = open('C:\Users\Anjali Ashok\workspace\Stenography\src\\test1.txt', "r")
        file3 = open('C:\Users\Anjali Ashok\workspace\Stenography\src\\test2.txt', "a")
        
        list1 = file1.readlines()
        #for i in list1:
        #   thisline1 = i.strip().split(" ")
        
        ##print 'hello'   
        list2 = file2.readlines()
        #for j in list2:
        #    thisline2 = j.strip().split(" ")
        
        '''for x in list1:
            for y in list2:
                c = self.LongestCommonSubstring(x,y);
                print c'''
               
                    
        occured = []
        
        d = dict(x.strip().split(":") for x in list1)
        clean_d = { k.strip():v.strip() for k, v in d.iteritems()}
        
        c = self.LongestCommonSubstring('anfmfjali', 'anjali is');
        print c
        
        for m in list1:
            #thisline1 = m.strip().split(" ")
            #for x in thisline1:
            for y in list2:
                common = self.LongestCommonSubstring(m,y);
                if common.strip('.') in clean_d.keys():#try exact string matching in this part
                    if clean_d[common.strip('.')].strip() not in occured:
                        if(clean_d.has_key(common.strip('.'))):
                            file3.write(common.strip('.')+" : ")
                            file3.write(clean_d[common.strip('.')])
                            file3.write("\n")
                    else:
                        continue
                    occured.append(clean_d[common.strip('.')])
                else:
                    continue
                
        file1.close()
        file2.close()
        file3.close()
c1 = Convert()
         
