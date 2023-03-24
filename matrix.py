class matrix:

    data=[]

    matrix=[]



    def get_data(self,path_file):
        file=open(path_file, "r")
        for line in file:
            self.data.append(line[:-1])

    def print_data(self):
        print(self.data)

    def do_matrix(self):
        tmp=[]

        for firs_gen in range(len(self.data)):
            for second_gen in range(len(self.data)):
                licznik=0
                for i in range(1,10):
                    #print(self.data[firs_gen][i:],"bla", self.data[second_gen][:-i], "   ", self.data[firs_gen], self.data[second_gen])
                    if self.data[firs_gen][i:]==self.data[second_gen][:-i]:
                        tmp.append(9-i)
                        licznik=1
                        break
                if licznik==0:
                    tmp.append(0)
            self.matrix.append(tmp)
            tmp=[]

    def show_matrix(self):
        print(self.matrix)