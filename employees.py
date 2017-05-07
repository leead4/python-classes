# Create a class that contains information about employees of 
# a company and define methods to get/set employee name, job title, and start date.

# Copy this Company class into your module.

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date
        self.employees = list()

    def show_company_name(self):
        """Returns the name of the company"""
        print(self.name)
        return self.name
    
    def get_title(self):

    	return self.title

    def get_start_date(self):

    	return self.start_date

    def hire_employees(self, people):
        self.employees.extend(people)


    def show_employees(self):
        print(self.employees)
        return self.employees

class Employee():
    def __init__(self):
        self.name = name
        self.job_title = title
        self.company_name = company_name

cat_butt = Company("Catt Butt llc", "CatLogo", "now")
employee_list = ["kevin", "alex", "roger"]
cat_butt.hire_employees(employee_list)

cat_butt.show_employees()
cat_butt.show_company_name()


# Add the remaining methods to fill the requirements above
# Consider the concept of aggregation, and modify the Company 
# class so that you assign employees to a company.



# Create a company, and three employees, 
# and then assign the employees to the company.






