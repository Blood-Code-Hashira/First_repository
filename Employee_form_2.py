class employee:
    ceo = "Sundar Pichai"
    company = "Google"
    
    def __init__(self, name, salary, experience, points):
        self.__name = name
        self.__salary = salary
        self.__experience = experience
        self.__points = points
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def change_name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string.")
            return
        self.__name = new_name
        
    @property 
    def salary(self):
        return self.__salary 
    
    @salary.setter
    def change_salary(self, new_salary):
        if not (new_salary > 0):
            raise ValueError("Salary must be greater than zero.")
            return
        self.__salary = new_salary
        
    @property
    def experience(self):
        return self.__experience
    
    @experience.setter
    def change_exp(self, new_experience):
        if not (new_experience > 0 and self.__experience < 15):
            raise ValueError("Experience must be greater than 0.")
            return
        self.__experience = new_experience
        
    @property
    def points(self):
        return self.__points
    
    @points.setter
    def change_points(self, new_points):
        if not (new_points > 0):
            raise ValueError("Points must be greater than 0.")
            return
        self.__points = new_points
        
    @classmethod
    def manager(self):
        return self.ceo
    
    def change_manager(self, new_ceo):
        if not isinstance(new_ceo, str):
            raise ValueError("Name of the manager must be a string.")
            return
        self.ceo = new_ceo
        
    @classmethod 
    def comp(self):
        return self.company
    
    def __add__(self, other):
        return self.__salary + other.salary
    
    def change_company(self, new_company):
        if new_company != str:
            raise ValueError("Name of the company must be a string.")
            return
        self.company = new_company
        
    def reputation(self):
        if self.__points > 5 and self.__experience > 5 and self.__salary > 500000:
            return "Comes in the list of best and senior employees of the company."
            
        elif self.__points == 5 and self.__experience == 5 and self.__salary == 500000:
            return "Good Employee and can do more better and is also a senior employee."
            
        elif self.__points < 5 and self.__experience < 5 and self.__salary < 500000:
            return "Need some efforts and have intermediate level of experience."
            
        elif self.__points == 2 and self.__experience == 2 and self.__salary < 250000:
            return "Job is in danger and needs too efforts."
            
        elif self.__points == 1 and self.__experience == 1 and self.__salary == 100000:
            return "Worst Employee !!"
        
        else:
            return "Invalid Input."
    
    def __str__(self):
        return f"Employee Name : {self.__name}\nSalary : {self.__salary}\nExperience (in years) : {self.__experience}\nNo. of points employee have : {self.__points}\nName of the company in which the employee work : {self.company}.\nCEO of {self.ceo} : "
    
e = employee("Max Doe", 900000, 6, 10)
print(e)
print(e.reputation())
