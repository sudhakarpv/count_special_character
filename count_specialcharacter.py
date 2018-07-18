def main():
    pass
    n=input()
    count=0
    for i in n:
        k=i.isdigit()
        o=i.isalpha()
        if (k==False and o==False):
            count+=1
    print(count)

if __name__ == '__main__':
    main()
