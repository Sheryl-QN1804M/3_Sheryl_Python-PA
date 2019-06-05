class CalUtils: #def CalUtils class
    def __init__(self):   #method for class to initialize objects by giving objects an initial value
        self.names = [] #list only to append later
        self.heights = []
        self.totalStudentHeight=0.0 #(start)set to 0.0 for float
        self.totalStudentCount =0 #(start)set to 0 for integer

    def CalAvgHeight(self):
        print ("Student average height is : ")
        with open("listOfStudentHeight.txt" , 'r') as f:  #locate and open file only read
            for line in f:  #each line in file
                f = line.split('\t')    #split the list by tab
                name = f[0]             #name side
                height = f[1]           #height side
                self.names.append(str(name))         #(add) name side to self.names variable in list
                self.heights.append(float(height))   #(add) height side to self.heights variable in list
                self.totalStudentCount = len(self.names) #number of self.names
                self.totalStudentHeight = sum(self.heights)
            average = print(str(round(self.totalStudentHeight / self.totalStudentCount, 2)) + " m for " + str(len(self.names)) + " students.")

        print("Is there any new student? Enter either yes or no only?")
        x = input()
        if x == "yes":
            new_names = str(input("Enter new student name:"))
            file = open("listOfStudentHeight.txt", 'a')   #append the list
            file.write('\n' + new_names)   #append the new_names to the list
            new_heights = input("Enter student height (in meters):")
            try:  #conditional statement to check the student height entered isn't numeric
                val = float(new_heights) #if variable: val is float
                print("Yes input is a numeric.")
                file = open("listOfStudentHeight.txt", 'a')
                file.write('\t') + file.write(str(round(val, 2)))  # with tab(space) and append the new_heights to the list
                self.totalStudentHeight += val # add new_heights to the total no. of self.totalStudentHeight
                self.totalStudentCount += 1

                print("Student average height is: " + str(round(self.totalStudentHeight / self.totalStudentCount, 2)) + " m for " + str(int(self.totalStudentCount)) + " students." ) #print string for statement

            except:
                print("No.. input is not a numeric")
                print("Please enter again , the student's height entered is numeric.")
                new_heights = input("Enter student height (in meters):")
                val = float(new_heights) #if val=float() then later print..
                print("Yes input is a numeric.")
                file = open("listOfStudentHeight.txt", 'a')
                file.write('\t') + file.write(str(round(val, 2)))  # with tab(space) and append the new_heights to the list
                self.totalStudentHeight += val  # add new_heights to the total no. of self.totalStudentHeight
                self.totalStudentCount += 1

                print("Student average height is: " + str(round(self.totalStudentHeight / self.totalStudentCount, 2)) + " m for " + str(int(self.totalStudentCount)) + " students.")

        else:
            print("Student average height is: " + str(round(self.totalStudentHeight / self.totalStudentCount, 2)) + " m for " + str(int(self.totalStudentCount)) + " students.")

p = CalUtils()    #instance of CalUtils,call its constructor
p.CalAvgHeight()  #CalUtils calls its method,produce the result
