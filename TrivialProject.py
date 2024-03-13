print("welcome to my quiz")
playing = input("Do you want to play? ")
if playing != "yes":
     quit()
print("Okay! let's play ")


     

question= [
    {
        "question":" Which of the following is the correct extension of the Python file?\n(a) Python\n (b) Pl\n(c) py\n(d) p\n\n", 
        "answer":"a"
    },
    {
        "question": "what is the largest organ in the human body?\n(a) Heart\n(b) Liver\n(c) Brain\n(d) Skin\n\n ",
        "answer":"d"
        
    },
    {
        "question":"Which continent is the most populous?\n(a) Asia\n(b) Africa\n(c) Europe\n(d) North America\n\n",
        "answer":"a"
        
    },
    {
        "Which is the capital of Nigeria?\n(a) Abuja\n(b) Lagos\n(c) Kano\n(d) Ibadan\n\n",
        "answer"
        
    },
    {
        "question":"When did Nigeria become independent\n(a) 1945\n(b) 1948\n(c) 1957\n(d) 1960\n\n",
        "answer":"d"
        
    },
    {
        "question":"How many sides does a triangle have?\n(a) 4\n(b) 3\n(c) 1\n(d) 2\n\n",
        "answer":"b"
        
    },
    {
        "question":"How many bones are in the human body?\n(a) 201\n(b) 198\n(c) 206\n(d) 105\n\n",
        "answer":"c"
        
    },
    {
        "question":"Which direction does the sun rise?\n(a) west\n(b) south\n(c) north\n(d) east\n\n"
        "answer":"b"
        
    },
    {
        "question":"Which planet is closest to the sun?\n(a) earth\n(b) mercury\n(c) jupiter\n(d) mars\n\n"
        "answer":"b"
    
    },
    {
        "question":"How many continents are there?\n(a)9\n(b) 6\n(c) 7\n(d) 10\n\n"
        "answer":"b"
        
    },
    {
        "question":"When is the Nation Day in Nigeria\n(a) 7 April\n(b) 14 June\n(c) 1 October\n(d) 1 November\n\n"
        "answer":"b"
    
    },
    {
        "question":"How many bones are in the human body?\n(a) 201\n(b) 198\n(c) 206\n(d) 105\n\n",
        "answer":"c"
    
    },
    {
        "Which is the official language of Nigeria\n(a) English\n(b) Ibo\n(c) Hausa\n(d) Swahili\n\n",
        "answer":"a"
        
    },
    {
        "question":"What is the bone in your spine called?\n(a) \n(b) vertebrae\n(c) \n(d)\n\n",
        "answer":"b"
        
    },
]

score = 0
for i in question:
     print(i)
     Answer =input("enter the answer(a/b/c/d): ")
if Answer == question.Answer():
          print("correct answer,you got 1 point")
          score = score +1
else:
          print("wrong answer, you lost 1 point")
          score= score -1

          print("Final score is:",score)
