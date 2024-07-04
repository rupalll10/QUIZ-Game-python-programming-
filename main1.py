#python_project_1- KBC

questions = [
  [
    "What does h stands for in html?", "hype", "hyper", "high","hi", "None",2
  ],
  [ "Which of the following is not a type of inheritance in a c++ programming language?", "multipe",
    "multilevel","single","double", "None", 3
  ],
  [
    "What is a Deque?", "delete stack", "delete linkedlist", "delete max in queue",
    "delete min in queue", "None", 3
  ],
  [
    "Which of the following is not an assymptotic notation?", "big o", "big theta", "big omega",
    "big delta", "None", 4
  ],
  [
    "All classes are ........ by default in c++", "public", "private", "protected",
    "none of the above", "None", 1
  ],
  [
    "Using friend keyword provides access to which class?",  "public", "private", "protected",
    "none of the above", "None", 2
  ],
  [
    "Which of the following component is not a standard template library component?", "container", "algorithm", "iteratot",
    "template", "None", 4
  ],
  [
    "Which of the following is self closing html tag?", "<h1>", "<b>", "<br>",
    "<Pre>", "None", 3
  ],
  [
    "By default unordered list has........ bullet points?", "round", "square", "diamond",
    "it is random", "None", 1
  ],
  [
    "Which type of heap is created in oreder to sort numbers in ascending order using heap sort?", "min heap", "max heap", 
    "both","none of the above", "None", 2
  ],
  [
    "Which of the following is non comparison sort?", "heap sort", "merge sort", "counting sort",
    "bubble sort", "None", 3
  ],
  [
    "Which approad gives an sure optimal solution for a problem?", "greedy", "brute force", "divide and conquer",
    "none of the above", "None", 2
  ],
  [
    "Worst case time complexity for binary search is?", "o(n)", "o(n2)", "o(logn)",
    "o(2logn)", "None", 3
  ],
  [
    "Which of the following is incorrect about tuple?", "it is a ordered collection ", "it can have duplicate entry",
     "it is mutable","indexing starts from 0", "None", 3
  ],
  [
    "What approach is used in quick sort?", "greedy", "brute force", "divide and conquer",
    "none of the above", "None", 3
  ],
  [
    "What of the following is not true about pointer?", "it contains value of variable", "it contains address of variable",
     "it is always a whole number","it is bound to initializer", "None", 4
  ],
  [
    "A binary tree with either 0 or 2 child nodes is calld......?", "complete binary tree", "strict binary tree",
     "almost complete binary tree","atmost complete binary tree", "None", 2
  ],
  [
    "total no of edges from root node to leaf node at last level is called.....?", "range of node", "trace of node",
     "depth of node","breadth of node", "None", 3
  ],
  [
    "Which of the following is not a tree traversal method.",
   "inorder", "outorder", "preorder","postorder", "None", 2
  ],
  [
    "Which of the following is not true about prim's algorithm?", "it is connencted ", "it is faster on dense graph", 
    "time complexity is o(v2)","it traverses one node only once", "None", 4
  ],
  [
    "If h7 is used in HTML, it will behave as a .......?", "article", "paragraph", "heading",
    "hyperlink", "None", 2
  ],
  [
    "Collision during hashing can be best resolved using ", "linear probing", "quadratic probing", "double hashing",
    "open hashing", "None", 3
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,
320000,640000,1250000,2500000,5000000,10000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"{question[0]} ")
  print(f"1. {question[1]}          2. {question[2]} ")
  print(f"3. {question[3]}          4. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    
  else:
    print("Wrong answer!")
    break 

print(f"the winning amount is {money}")