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
        b = set()
        c = defaultdict()
        courses1 = ['C105','C119','C121','C145','C186','C187','C197C','C197U']
        courses2 = ['C220','C230','C240','C250']
        courses3 = ['C305', 'C311', 'C320', 'C326', 'C328', 'C345', 'C348', 'C365', 'C370', 'C373' , 'C377', 'C383', 'C390N']


        prereq_for_inter = ['C187', 'M132']
        c['C311'] = ['C250'] # it should automatically include the prereq for 250 now
        c['C345'] = ['C187']
        c['C320'] = ['C']
        c['C383'] = ['C250', 'S515,C240'] # , means that we can choose either of them
        
        for i in courses1:
            self.courses[i] = set()
        for i in courses2:
            self.courses[i] = set(prereq_for_inter)

    def get_prereq(self, course):
        return self.courses[course]

    def classes_you_can_take(self, ):




# COMPSCI	105	Computer Literacy	3
# COMPSCI	119	Introduction to Programming	3
# COMPSCI	121	Introduction to Problem Solving with Computers	4
# COMPSCI	145	Representing, Storing, and Retrieving Information	3
# COMPSCI	186	Using Data Structures	4
# COMPSCI	187	Programming with Data Structures	4
# COMPSCI	197C	Special Topics - Programming in C	1
# COMPSCI	197U	Special Topics - A Hands-on Introduction to UNIX	1
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