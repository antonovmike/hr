Practical assignment for unit 3

Objective
To add new functionality to the “hr_hospital” module that automates hospital operations.

Requirements

1. Create an abstract personality model. Modify the structure of the module models so that the following models are inherited from this abstract model: “Patient”, “Doctor”, “Contact person”. Add the following fields to the abstract model “Person”:
Last Name, First Name
Phone
Email
Photo
Gender

2. Add the following fields to the Patient model:
Date of Birth
Age, the field should be calculated from the current date
Passport details
Contact person
Personal Doctor

3. Add the following fields to the Doctor model:
Specialty

4. Create a new model “Diagnosis” containing the following data:
Date (diagnosis)
Doctor who made the diagnosis
Patient
Disease
Assignment for treatment

5. Add a hierarchical structure to the Diseases model. Using demo data, add 4 disease records with hierarchy.

6. Add the following fields to the Patient Visits model:
Start date and time
Doctor
Patient
Diagnosis

6.1. Prohibit changing the time/date of the doctor of a visit that has already taken place

6.2. Prohibit deleting or archiving visits with diagnoses

7. Create a new “personal doctor change history” model containing the following data:
Date and time of the doctor's appointment
Patient
Doctor

7.1. When a patient's personal doctor is set or changed, a new model should be created automatically.

8. Expand the model “ Doctor” with the fields “Intern” and “Doctor-Mentor”.

8.1. If an intern diagnoses a patient, the mentor doctor should add his/her comment to this diagnosis

8.2. Prohibit the intern from being selected over the mentor doctor.

9. Create a new model “ Doctor's Schedule” - time intervals when a doctor can make appointments for patients, containing the following data.
Doctor
Date of reception
Hour of reception

9.1 Add a check to make sure that the appointment hours do not repeat.

10. Extend the “See Patients” model with the ability to book an appointment.

10.1 Add a check to ensure that you cannot book the same appointment twice.

10.2 Add a field where it is noted or the appointment has taken place.

11. Create a wizard for mass override of personal Doctor. The wizard should be called from the “list” view of the “Patient” model.

12. Create a report of diseases for a month, which is a time model.

12.1 Add the ability to select the year and month that calculates diseases and the number of diagnoses of this disease.

12.2. The Wizard should be called from the “list” and “form” views of the “Doctor” model from the system menu item “Print”.

12.3 Add also the call of this wizard from a separate menu item of the “Hospital” module (it is desirable to add a separate general item “Reporting” and add the wizard call to it).

13. Create a wizard to transfer the appointment to the doctor. The wizard should dismiss the time and record to another time/date/doctor.

14. Create a wizard to fill in doctor appointment times per week, make it possible to fill in different schedules on even/ odd week.

