smith = int(input())
jhon = int(input())
henry = int(input())

if smith == jhon and jhon == henry:
    print("smith, jhon and henry are of same age")

else:
    if smith <= jhon and smith <= henry:
             youngest = smith
             print("smith is younger")
    elif jhon <= smith and jhon <= henry:
        youngest = jhon
        print("jhon is youngest")
    else:
        youngest = henry
        print("henry is youngest")



