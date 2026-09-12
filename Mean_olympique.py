nums = [3,1,5,6]

def min_2(a:float,b:float,c:float,d:float):
    return(
        (a if ((b<a)+(c<a)+(d<a)) == 1 else
         (b if ((a<b)+(c<b)+(d<b)) == 1 else
          (c if ((a<c)+(b<c)+(d<c)) == 1 else d)))

    )
def max_2(a:float,b:float,c:float,d:float):
    return(
        (a if ((b<a)+(c<a)+(d<a)) == 2 else
            (b if ((a<b)+(c<b)+ (d<b)) == 2 else
                (c if ((a<c)+(b<c)+(d<c)) == 2 else d)))
    )


def meanolympics(a:float,b:float,c:float,d:float)->float:
    return(min_2(a,b,c,d) + max_2(a,b,c,d))/2

print(meanolympics(2,3,1,7))

