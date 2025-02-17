class Employee:
    def __init__ (
            self,
            designation : str = 'Developer',
            frontend : bool = False,
            backend : bool = False
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__ (self):
        return '{}'.format (self.designation, self.frontend, self.backend)
   
    ### Write the your method over here.
    def verifier (self):
        if self.frontend and self.backend:
            self.designation="Full Stack Developer"
            return 'Full Stack Developer'
       
        elif self.frontend:
            self.designation="Frontend Developer"
            return 'Frontend Developer'
       
        elif self.backend:
            self.designation="Backend Developer"
            return 'Backend Developer'
       
        else:
            self.designation="No Designation"
            return 'No designation assigned'

if __name__ == '__main__':
    firstEmployee = Employee ()
    firstEmployee.frontend="frontend"
    firstEmployee.backend="backend"
    print (firstEmployee.verifier())
