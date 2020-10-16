marks_list=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]
count_exclude = 0
count_progress = 0
count_trailer = 0
count_retriever = 0


def execute():
    print("\n~~~~~~~~~~~~~~~~~~~~Category Totals~~~~~~~~~~~~~~~~~~~~\n")
    print('Progress\t' ,"=", count_progress)
    print('Trailing\t' ,"=", count_trailer)
    print('Retriever\t',"=",count_retriever)   
    print('Exclude\t\t' ,"="  ,count_exclude)
    print("\n~~~~~~~~~~~~~~~Overall Total = 10~~~~~~~~~~~~~")
    print("\n-----------------Horizantal Histogram-----------------\n")
    print('Progress\t' , count_progress,   ' = \t' ,count_progress* '*')
    print('Trailing\t' , count_trailer,    ' = \t' ,count_trailer*  '*')
    print('Retriever\t',count_retriever,   ' = \t' ,count_retriever*'*')
    print('Exclude\t\t'  ,  count_exclude,   ' = \t' ,count_exclude*  '*')

    print("\n--------------Your program is now executed-------------")
    
    exit()

