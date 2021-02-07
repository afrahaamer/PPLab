class py_solution:
    def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x
        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x
print(py_solution().pow(3, -4));
print(py_solution().pow(4, 6));
print(py_solution().pow(90, 5));