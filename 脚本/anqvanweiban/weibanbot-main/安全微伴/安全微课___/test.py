from multiprocessing import Pool
def fun(x,y):
    print(x,y+'')
if __name__ == '__main__':
    aa=[['2106200248','2106200248'],['2106200247','2106200247']]
    pool= Pool(5)
    pool.starmap(fun,aa)
