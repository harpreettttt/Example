# test_HospitalManagement.py

import unittest
from HospitalManagement import Patient, DayPatient


class TestPatient(unittest.TestCase):
    def setUp(self):
        """
        Set up a Patient object for testing.
        This method is called before each test.
        """
        self.patient = Patient(
            name="Jane Doe",
            age=30,
            patient_id=5001,
            illness="Flu",
            admission_date="2024-04-01"
        )

    def test_patient_initialization(self):
        """
        Test that the Patient object is initialized correctly.
        """
        self.assertEqual(self.patient.name, "Jane Doe")
        self.assertEqual(self.patient.age, 30)
        self.assertEqual(self.patient.patient_id, 5001)
        self.assertEqual(self.patient.illness, "Flu")
        self.assertEqual(self.patient.admission_date, "2024-04-01")

    def test_patient_get_details(self):
        """
        Test the get_details method of Patient.
        """
        expected_details = ("Patient Name: Jane Doe, Age: 30, ID: 5001, "
                            "Illness: Flu, Admission Date: 2024-04-01")
        self.assertEqual(self.patient.get_details(), expected_details)

    def test_patient_get_treatment_plan(self):
        """
        Test the get_treatment_plan method of Patient.
        """
        expected_plan = "The treatment plan for this patient will be provided after further assessment."
        self.assertEqual(self.patient.get_treatment_plan(), expected_plan)


class TestDayPatient(unittest.TestCase):
    def setUp(self):
        """
        Set up a DayPatient object for testing.
        This method is called before each test.
        """
        self.day_patient = DayPatient(
            name="John Smith",
            age=45,
            patient_id=6002,
            illness="Arthritis",
            admission_date="2024-05-15",
            discharge_time="17:00"
        )

    def test_day_patient_initialization(self):
        """
        Test that the DayPatient object is initialized correctly, including inherited attributes.
        """
        self.assertEqual(self.day_patient.name, "John Smith")
        self.assertEqual(self.day_patient.age, 45)
        self.assertEqual(self.day_patient.patient_id, 6002)
        self.assertEqual(self.day_patient.illness, "Arthritis")
        self.assertEqual(self.day_patient.admission_date, "2024-05-15")
        self.assertEqual(self.day_patient.discharge_time, "17:00")

    def test_day_patient_get_details(self):
        """
        Test the overridden get_details method of DayPatient.
        """
        expected_details = ("Day Patient Name: John Smith, Age: 45, ID: 6002, "
                            "Illness: Arthritis, Admission Date: 2024-05-15, "
                            "Discharge Time: 17:00")
        self.assertEqual(self.day_patient.get_details(), expected_details)

    def test_day_patient_get_treatment_plan(self):
        """
        Test the overridden get_treatment_plan method of DayPatient.
        """
        expected_plan = ("The treatment plan includes day procedures and the patient will be discharged by 17:00.")
        self.assertEqual(self.day_patient.get_treatment_plan(), expected_plan)

    def test_day_patient_inheritance(self):
        """
        Test that DayPatient is indeed a subclass of Patient.
        """
        self.assertTrue(issubclass(DayPatient, Patient))
        self.assertIsInstance(self.day_patient, Patient)

    def test_day_patient_method_override(self):
        """
        Ensure that the DayPatient methods override the Patient methods.
        """
        # Ensure that get_details returns DayPatient's version
        self.assertNotEqual(self.day_patient.get_details(),
                            self.day_patient.__class__.__bases__[0].get_details(self.day_patient))

        # Ensure that get_treatment_plan returns DayPatient's version
        self.assertNotEqual(self.day_patient.get_treatment_plan(),
                            self.day_patient.__class__.__bases__[0].get_treatment_plan(self.day_patient))


if __name__ == '__main__':
    unittest.main()
