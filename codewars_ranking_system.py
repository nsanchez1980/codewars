class User:

    
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.possible_ranks = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]

    def rank(self):
        return self.ranking
    
    def progress(self):
        return self.progress
    
    def inc_progress(self, n):
        sum = sorted([self.possible_ranks.index(self.rank), self.possible_ranks.index(n)])
        rank_diff=sum[1]-sum[0]
        print("difference",rank_diff)
        if self.possible_ranks.index(self.rank)>=self.possible_ranks.index(n): #si mi ranking es mayor o igual al de la tarea
            if rank_diff==1:
                self.progress = self.progress + 1
            elif rank_diff==0:
                self.progress = self.progress + 3
        else:   #la tarea es de mayor ranking que yo.    
            self.progress= self.progress + (10*rank_diff*rank_diff)
        
        while self.progress>=100:
            self.progress = self.progress - 100
            if self.rank==-1:
                self.rank = 1
            elif self.rank==0:
                self.rank = self.rank + 1
            elif self.rank!=8:
                self.rank = self.rank + 1
        if self.rank==8:
            self.progress=0

pappo = User()
print("Rank",pappo.rank)
print("Progress",pappo.progress)
pappo.inc_progress(-7)
print("Rank",pappo.rank)
print("Progress",pappo.progress)
pappo.inc_progress(-1)
print("Rank",pappo.rank)
print("Progress",pappo.progress)
pappo.inc_progress(2)
print("Rank",pappo.rank)
print("Progress",pappo.progress)
pappo.inc_progress(1)
print("Rank",pappo.rank)
print("Progress",pappo.progress)
