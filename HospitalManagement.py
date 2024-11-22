class Patient:
    def __init__(self, name: str, age: int , patient_id: int, illness: str, admission_date: str):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.illness = illness
        self.admission_date = admission_date

    def get_details(self):
        return f" Patient Name: {self.name}, Age: {self.age}, ID: {self.patient_id}, Illness: {self.illness}, Admission Date: {self.admission_date}"

    def get_treatment_plan(self):
        return f" The treatment plan for this patient will be provided after further assessment."


patient1= Patient('John', 34, 956983, "Flu", "23/03/2024")
patient1.get_details()
treatment_plan= patient1.get_details()
print(treatment_plan)

class DayPatient:
    def __init__(self, name: str, age: int , patient_id: int, illness: str, admission_date: str, discharge_time: str):
        super().__init__(name , age  , patient_id , illness , admission_date )# doesnt need str etc already stated in above when initialising. can cause errors. using super to state the parents
        self.discharge_time = discharge_time