class Pai_Lie():
    "全排列问题"
    def __init__(self):
        pass
    def helper(self,solution,array):
        if len(array) == 0:
            print(solution)
            return
        for i in range(len(array)):
            solution_ = solution[:]
            solution_.append(array[i])
            newarray = array[:i]+array[i+1:]
            self.helper(solution_,newarray)

    def solve(self,array):
        solution = []
        self.helper(solution,array)

class Zu_He():

    def solve(self,arr,n):
        solution = []
        self.helper(arr,solution,n)

    def helper(self,arr,solution,n ):
        if len(solution) == n:
            print(solution)
            return
        for i in range(len(arr)):
            solution_ = solution[:]
            solution_.append(arr[i])
            arr_ = arr[i+1:]
            self.helper(arr_,solution_,n)

if __name__ =="__main__":
    a = [1,2,3,4]
    s = Pai_Lie()
    s.solve(a)
    print("==================================")
    x = Zu_He()
    x.solve(a,2)



