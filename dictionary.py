student = {
             "name" : "vijay" ,
             "placement" : "palle telechnologies" ,
             "year" : 2023
          }
lap = {
       "name" : "lenovo",
        "model" : 2008
      }
car = {
        "name" : "sail" ,
        "model" : 2018 ,
        "branch" : "Erode"
     }
get = {
        "student" : student,
        "lap" : lap,
        "car" : car
         }
print(get)
print(
    '''
    1 = student
    2 = lap
    3 = car
    '''
     )
choice = int(input("Enter a choice: "))
if choice == 1:
    print(student)
    print(
        '''
        4 = name,
        5 = placement,
        6 = year
        '''
         )
    x = int(input("Enter a choice: "))
    if x == 4:
       student["name"] = input("Enter a name: ")
       print(student)
    elif x == 5:
        student["placement"] = input("Enter a placement: ")
        print(student)
    elif x == 6:
        student["year"] = int(input("Enter a year: "))
        print(student)

if choice == 2:
        print(lap)
        print(
            '''
            7 = name
            8 = model

           '''
        )
        x = int(input("Enter a choice: "))
        if x == 7:
            lap["name"] = str(input("Enter a name: "))
            print(lap)
        elif x == 8:
            lap["model"] = str(input("Enter a model: "))
            print(lap)

if choice == 3:
            print(car)
            print(
                '''
               9 = name
               10 = model
               11 = branch
               '''
            )
            x = int(input("Enter a choice: "))
            if x == 9:
                car["name"] = str(input("Enter a name: "))
                print(car)
            elif x == 10:
                car["model"] = int(input("Enter a model: "))
                print(car)
            elif x == 11:
                car["branch"] = int(input("Enter a branch: "))
                print(car)