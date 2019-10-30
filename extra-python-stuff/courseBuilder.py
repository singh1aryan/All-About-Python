from collections import defaultdict

class Course:
    def __init__(self):
        self.name = ""
        self.number = 0
        self.credits = 0
        self.difficulty = 0
        self.time_per_week = 0
    
class Course:
    def __init__(self):
        self.prereq = set()
        self.courses = defaultdict()

    def build_dict(self):

        self.courses['M132'] = ['M131']
        self.courses['C187'] = ['C121', 'M101']
        
        self.courses['C220'] = ['C187']
        self.courses['C230'] = ['C187']
        self.courses['C240'] = ['C187', 'M132']        
        self.courses['C250'] = ['C187', 'M132']

        self.courses['C311'] = ['C187', 'C250,M455'] # it should automatically include the prereq for 250 now
        self.courses['C345'] = ['C187']
        self.courses['C320'] = ['C187']
        self.courses['C383'] = ['C250', 'S515,C240'] # , means that we can choose either of them
        self.courses['377'] = ['C250']

        self.courses
        
        # for i in courses1:
        #     self.courses[i] = []
        # for i in courses2:
        #     self.courses[i] = prereq_for_inter

    # visualize this as a tree 
    # Doing BFS to find all the prereqs
    def get_prereq(self, course):
        b = defaultdict()
        # b['o'] = ""
        a = []
        stack = []
        stack.append(course)
        # [250,220,230] - gives us this, we need prereq for all of these
        while len(stack)>0:
            c = stack.pop()
            a.append(c)
            if c in self.courses:
                # print(c)
                # print(len(self.courses[c]))
                # there is an optional subject for some, like stats 515 and cs 240
                k=0
                for i in self.courses[c]:
                    if len(i)>4:
                        # make a new list and add all of them to it
                        # add a matching letter to the end of it and then classify at the end of it 
                        # make a dictionary and store things to that
                        # if we choose 455, then prereq for that are different - that should be the option case
                        # dictionary? - how to add - various ways - w numbers, each other sounds good
                        op = i.split(',')
                        b[op[0]] = op[1]
                        stack.append(op[0])
                        stack.append(op[1])
                        continue
                    stack.append(i)
        # print(a)
        a = list(set(a))
        a = self.rearrange(a[1:])
        for i in b:
            print(i,b[i])
        final_list = []
        # there has to be a better way than this
        # for i in b:
        #     new_list = a
        #     new_list.remove(i)
        #     final_list.append(new_list)
        #     new_list.append(i)
        #     new_list.remove(b[i])
        #     final_list.append(new_list)

        # print(final_list)
        return 'Pre Req for ' + course + ' are: ' + str(a)

    def rearrange(self, a):
        m = []
        n = []
        for i in a:
            b = i[1:]
            m.append((i[0], int(b)))
        m = sorted(m, key=lambda tup: (tup[0], tup[1]))
        for i in m:
            b = i[0]+str(i[1])
            n.append(b)
        return n
        

    def classes_you_can_take(self, ):
        pass

a = Course()
a.build_dict()
print(a.get_prereq('C311'))




# COMPSCI	105	Computer Literacy	3
# COMPSCI	119	Introduction to Programming	3
# COMPSCI	121	Introduction to Problem Solving with Computers	4
# COMPSCI	145	Representing, Storing, and Retrieving Information	3
# COMPSCI	186	Using Data Structures	4
# COMPSCI	187	Programming with Data Structures	4
# COMPSCI	197C	Special Topics - Programming in C	1
# COMPSCI	197U	Special Topics - A Hands-on Introduction to UNIX	1
# COMPSCI 198J Practicum - High School Teaching Practicum

# COMPSCI	220	Programming Methodology	4
# COMPSCI	230	Computer Systems Principles	4
# COMPSCI	240	Reasoning Under Uncertainty	4
# COMPSCI	250	Introduction to Computation	4
# COMPSCI	H250	Honors Colloquium for Introduction to Computation	1

# COMPSCI	305	Social Issues in Computing	3
# COMPSCI	311	Introduction to Algorithms	4
# COMPSCI	H311	Honors Colloquium for Introduction to Algorithms	1
# COMPSCI	320	Introduction to Software Engineering	4
# COMPSCI	H320	Honors Colloquium for Software Engineering	1
# COMPSCI	326	Web Programming	4
# COMPSCI	328	Mobile Health Sensing and Analytics	3
# COMPSCI	345	Practice and Applications of Data Management	3
# COMPSCI	348	Principles of Data Science	3
# COMPSCI	365	Digital Forensics	3
# COMPSCI	373	Introduction to Computer Graphics	3
# COMPSCI	377	Operating Systems	4
# COMPSCI	383	Artificial Intelligence	3
# COMPSCI	390N	Internet of Things	3
 	 	 	 
# COMPSCI	446	Search Engines	3
# COMPSCI	H446	Honors Colloquium for Search Engines	1
# COMPSCI	453	Computer Networks	3
# COMPSCI	461	Secure Distributed Systems	3
# COMPSCI	466	Applied Cryptography	3
# COMPSCI	490S	Software Entrepreneurship	3
# COMPSCI	491G	Seminar - Computer Networking Lab	3
 	 	 	 
# COMPSCI	501	Formal Language Theory	3
# COMPSCI	514	Algorithms for Data Science	3
# COMPSCI	520	Theory and Practice of Software Engineering	3
# COMPSCI	529	Software Engineering Project Management	3
# COMPSCI	535	Computer Architecture	3
# COMPSCI	577	Operating Systems Implementation	3
# COMPSCI	589	Machine Learning	3
# COMPSCI	590A	System Defense and Test	3
# COMPSCI	590F	Advanced Digital Forensics	3
# COMPSCI	590G	Game Programming	3
# COMPSCI	590M	Introduction to Simulation	3
# COMPSCI	590U	Mobile and Ubiquitous Computing	3
# COMPSCI	590V	Data Visualization and Exploration	3
# COMPSCI	591NR	Seminar - Neural Networks and Neurodynamics	3