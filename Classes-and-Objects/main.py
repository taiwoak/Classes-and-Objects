class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(Bob, new_name):
        Bob.change_name = new_name
       

    def change_age(Bob, new_age):
        Bob.change_age = new_age
        
    def add_track(Bob, new_track):
        Bob.add_track = new_track
        

    def get_score(Bob, score):
        Bob.get_score = score
        

Bob = Student(name="Bob", age=26, tracks=["FE","BE","PD"], score=20.90)
print("The Student name is", Bob.name)
print("The Student age is", Bob.age)
print("The Student tracks are", Bob.tracks)
print("The Student score is", Bob.score)

Bob.change_name = str(input("Enter your name: "))
Bob.change_age= int(input("Enter your age: "))
Bob.add_track = list(input("Enter your track: "))
Bob.get_score = Bob.score

print("The new Student name is", Bob.change_name)
print("The new Student age is", Bob.change_age)
print("The new Student tracks is", Bob.add_track + Bob.tracks)
print("The new Student score is", Bob.get_score)



# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
