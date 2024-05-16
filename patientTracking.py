import mysql.connector

# connect to the database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Neeta@15",
  database="patienttracking"
)

# create a cursor object to execute SQL queries
cursor = db.cursor()

# add a patient to the system
def add_patient(PatientID, FirstName, LastName, Gender, DateOfBirth, Address, City, State, PostalCode, Phone, Email, InsuranceID):
    sql = "INSERT INTO patientS (PatientID, FirstName, LastName, Gender, DateOfBirth, Address, City, State, PostalCode, Phone, Email, InsuranceId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (PatientID, FirstName, LastName, Gender, DateOfBirth, Address, City, State, PostalCode, Phone, Email, InsuranceID)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "patient added to system")

# delete a patient from the system
def delete_patient(PatientID):
    sql = "DELETE FROM patients WHERE PatientID = %s"
    val = (PatientID,)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "patient deleted")

# display all products in the inventory
def view_patient():
    cursor.execute("SELECT * FROM patients")
    results = cursor.fetchall()
    print("\nPatientID", "FirstName", "LastName", "Gender", "DateOfBirth", "Address", "City", "State", "PostalCode", "Phone", "Email", "InsuranceID")
    for patient in results:
        print(patient)

# add a doctor to the system
def add_doctor(DoctorID, FirstName, LastName, Speciality, Phone, Email):
    sql = "INSERT INTO doctors (DoctorID, FirstName, LastName, Speciality, Phone, Email) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (DoctorID, FirstName, LastName, Speciality, Phone, Email)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "doctor added to system")

# display all doctor
def view_doctor():
    cursor.execute("SELECT * FROM doctors")
    results = cursor.fetchall()
    print("\nDoctorID", "FirstName", "LastName", "Speciality", "Phone", "Email")
    for doctor in results:
        print(doctor)

# add a appointment to the system
def add_appointment(AppointmentID, PatientID, DoctorID, AppointmentDate, AppointmentTime, AppointmentNotes):
    sql = "INSERT INTO appointments (AppointmentID, PatientID, DoctorID, AppointmentDate, AppointmentTime, AppointmentNotes) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (AppointmentID, PatientID, DoctorID, AppointmentDate, AppointmentTime, AppointmentNotes)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "appointment added to system")

# delete a appointment from the system
def delete_appointment(AppointmentID):
    sql = "DELETE FROM appointments WHERE AppointmentID = %s"
    val = (AppointmentID,)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "appointment deleted")

# display all appointments
def view_appointment():
    cursor.execute("SELECT * FROM appointments")
    results = cursor.fetchall()
    print("\nAppointmentID", "PatientID", "DoctorID", "AppointmentDate", "AppointmentTime", "AppointmentNotes")
    for appointment in results:
        print(appointment)

# add a medical test to the system
def add_medicaltest(MedicalTestID, PatientID, DoctorID, TestName, TestDate, TestResults):
    sql = "INSERT INTO medicaltests (MedicalTestID, PatientID, DoctorID, TestName, TestDate, TestResults) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (MedicalTestID, PatientID, DoctorID, TestName, TestDate, TestResults)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "medical_test added to system")

# delete a medical test from the system
def delete_medicaltest(MedicalTestID):
    sql = "DELETE FROM medicaltests WHERE medical_test_id = %s"
    val = (MedicalTestID)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "medical test deleted")

# display all medical test
def view_medicaltest():
    cursor.execute("SELECT * FROM medicaltests")
    results = cursor.fetchall()
    print("\nMedicalTestID", "PatientID", "DoctorID", "TestName", "TestDate", "TestResults")
    for medical_test in results:
        print(medical_test)

# add a treatment to the system
def add_treatment(TreatmentID, PatientID, DoctorID, TreatmentDate, TeatmentNotes):
    sql = "INSERT INTO treatments (TreatmentID, PatientID, DoctorID, TreatmentDate, TeatmentNotes) VALUES (%s, %s, %s, %s, %s)"
    val = (TreatmentID, PatientID, DoctorID, TreatmentDate, TeatmentNotes)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "treatment added to system")

# delete a treatment from the system
def delete_treatment(TreatmentID):
    sql = "DELETE FROM treatments WHERE treatment_id = %s"
    val = (TreatmentID)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "treatment deleted")

# display all treatment
def view_treatment():
    cursor.execute("SELECT * FROM treatments")
    results = cursor.fetchall()
    print("\nTreatmentID", "PatientID", "DoctorID", "TreatmentDate", "TeatmentNotes")
    for treatment in results:
        print(treatment)

# add a staff to the system
def add_staff(StaffID, FirstName, LastName, JobTitle, Phone, Email):
    sql = "INSERT INTO staff (StaffID, FirstName, LastName, JobTitle, Phone, Email) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (StaffID, FirstName, LastName, JobTitle, Phone, Email)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "staff added to system")

# display all staff
def view_staff():
    cursor.execute("SELECT * FROM staff")
    results = cursor.fetchall()
    print("\nStaffID", "FirstName", "LastName", "JobTitle", "Phone", "Email")
    for staff in results:
        print(staff)

# add a diagnosis to the system
def add_diagnosis(DiagnosisID, PatientID, DoctorID, DiagnosisDate, DiagnosisNotes):
    sql = "INSERT INTO diagnoses (DiagnosisID, PatientID, DoctorID, DiagnosisDate, DiagnosisNotes) VALUES (%s, %s, %s, %s, %s)"
    val = (DiagnosisID, PatientID, DoctorID, DiagnosisDate, DiagnosisNotes)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "diagnosis added to system")

# delete a diagnosis from the system
def delete_diagnosis(DiagnosisID):
    sql = "DELETE FROM diagnoses WHERE DiagnosisID = %s"
    val = (DiagnosisID)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "diagnosis deleted")

# display all diagnosis
def view_diagnosis():
    cursor.execute("SELECT * FROM diagnoses")
    results = cursor.fetchall()
    print("\nDiagnosisID", "PatientID", "DoctorID", "DiagnosisDate", "DiagnosisNotes")
    for diagnosis in results:
        print(diagnosis)

# add a insurance to the system
def add_insurance(InsuranceID, InsuranceName, InsuranceAddress, City, State, PostalCode, Phone, Email):
    sql = "INSERT INTO insurance (InsuranceID, InsuranceName, InsuranceAddress, City, State, PostalCode, Phone, Email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (InsuranceID, InsuranceName, InsuranceAddress, City, State, PostalCode, Phone, Email)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "insurance added to system")

# display all insurance
def view_insurance():
    cursor.execute("SELECT * FROM insurance")
    results = cursor.fetchall()
    print("\niInsuranceID", "InsuranceName", "InsuranceAddress", "City", "State", "PostalCode", "Phone", "Email")
    for insurance in results:
        print(insurance)

# interact with the user
print("--------------Welcome in Patient Tracking System---------------")
username = "pratham014"
password = "54321pb"
name = input("Enter username: ")
passw = input("Enter password: ")

while True:
    if name == username:
        if passw == password:
            print("Successfully Login\n")
            print("What would you like to do?")
            print("1. For Patient")
            print("2. For Doctor")
            print("3. For Appointment")
            print("4. For Medical Test")
            print("5. For Treatment")
            print("6. For Staff")
            print("7. For Diagnosis")
            print("8. For Insurance")
            print("9. Quit")

            choice = int(input("Enter Number: "))

            if choice == 1:
                print("1. ADD Patient")
                print("2. DELETE Patient")
                print("3. VIEW Patient")
                pat = int(input("Enter: "))

                if pat == 1:
                    id = int(input("Enter Patient ID: "))
                    fname = input("Enter Patient First Name: ")
                    lname = input("Enter Patient Last Name: ")
                    gender = input("Enter Patient Gender: ")
                    dob = int(input("Enter Patient DOB: "))
                    add = input("Enter Patient Address: ")
                    city = input("Enter Patient City: ")
                    state = input("Enter Patient State: ")
                    postalc = input("Enter Patient Postal Code: ")
                    phone = input("Enter Patient Phone No.: ")
                    email = input("Enter Patient Email: ")
                    inid = input("Enter Patient Insurance ID: ")
                    
                    add_patient(id, fname, lname, gender, dob, add, city, state, postalc, phone, email, inid)
                    print("\n")
                
                elif pat == 2:
                    id = int(input("Enter Patient ID:"))
                    delete_patient(id)
                    print("\n")

                elif pat == 3:
                    view_patient()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")

            elif choice == 2:
                print("1. ADD Doctor")
                print("2. VIEW Doctor")
                doc = int(input("Enter: "))

                if doc == 1:
                    id = int(input("Enter Doctor ID: "))
                    fname = input("Enter Doctor First Name: ")
                    lname = input("Enter Doctor Last Name: ")
                    speciality = input("Enter Doctor Speciality: ")
                    phone = input("Enter Doctor Phone Number: ")
                    email = input("Entter Doctor Email: ")
                    add_doctor(id, fname, lname, speciality, phone, email)
                    print("\n")
                    
                elif doc == 2:
                    view_doctor()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")

            elif choice == 3:
                print("1. ADD Appointment")
                print("2. DELETE Appointment")
                print("3. VIEW Appointment")
                appt = int(input("Enter: "))

                if appt == 1:
                    appid = int(input("Enter Appointment ID: "))
                    patid = int(input("Enter Patient ID: "))
                    docid = int(input("Enter Doctor ID: "))
                    date = input("Enter Appointment Date: ")
                    time = input("Enter Appointment Time: ")
                    notes = input("Enter Appointment Notes: ")
                    add_appointment(appid, patid, docid, date, time, notes)
                    print("\n")

                elif appt == 2:
                    id = int(input("Enter Appointment ID: "))
                    delete_appointment(id)
                    print("\n")

                elif appt == 3:
                    view_appointment()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")

            elif choice == 4:
                print("1. ADD Medical Test: ")
                print("1. DELETE Medical Test: ")
                print("2. VIEW Medical Test: ")
                medt = int(input("Enter: "))

                if medt == 1:
                    medtid = int(input("Enter Medical Test ID: "))
                    patid = int(input("Enter Patient ID: "))
                    docid = int(input("Enter Doctor ID: "))
                    test_name = input("Enter Medical Test Name: ")
                    test_date = input("Enter Medical Test Date: ")
                    test_result = input("Enter Medical Test Result: ")
                    add_medicaltest(medtid, patid, docid, test_name, test_date, test_result)
                    print("\n")

                elif medt == 2:
                    medtid = int(input("Enter Medical Test ID: "))
                    delete_appointment(medtid)
                    print("\n")

                elif medt == 3:
                    view_medicaltest()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")

            elif choice == 5:
                print("1. ADD Treatment")
                print("2. DELETE Treatment")
                print("2. VIEW Treatment")
                treat = int(input("Enter: "))

                if treat == 1:
                    treatid = int(input("Enter Treatment ID: "))
                    patid = int(input("Enter Patient ID: "))
                    docid = int(input("Enter Doctor ID: "))
                    dates = input("Enter Treatment Date: ")
                    notes = input("Enter Treatment Notes: ")
                    
                    add_treatment(treatid, patid, docid, dates, notes)
                    print("\n")
                
                elif treat == 2:
                    id = int(input("Enter Treatment ID: "))
                    delete_treatment(id)
                    print("\n")

                elif treat == 3:
                    view_treatment()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")

            elif choice == 6:
                print("1. ADD Staff")
                print("2. VIEW Staff")
                stf = int(input("Enter: "))

                if stf == 1:
                    id = int(input("Enter Staff ID: "))
                    fname = input("Entter Staff First Name: ")
                    lname = input("Entter Staff Last Name: ")
                    jobt = input("Enter Staff Job Title: ")
                    phone = input("Enter Staff Phone Number: ")
                    email = input("Entter Staff Email: ")
                    add_staff(id, fname, lname, jobt, phone, email)
                    print("\n")

                elif stf == 2:
                    view_staff()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")
            
            elif choice == 7:
                print("1. ADD Diagnosis")
                print("2. DELETE Diagnosis")
                print("3. VIEW Diagnosis")
                diag = int(input("Enter: "))

                if diag == 1:
                    diagid = int(input("Enter Diagnosis ID: "))
                    patid = int(input("Enter Patient ID: "))
                    docid = int(input("Enter Doctor ID: "))
                    dates = input("Enter Diagnosis Date: ")
                    notes = input("Enter Diagnosis Notes: ")
                    
                    add_treatment(diagid, patid, docid, dates, notes)
                    print("\n")
                
                elif diag == 2:
                    id = int(input("Enter Diagnosis ID: "))
                    delete_diagnosis(id)
                    print("\n")

                elif diag == 3:
                    view_diagnosis()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")

            elif choice == 8:
                print("1. ADD Insurance")
                print("2. VIEW Insurance")
                ins = int(input("Enter: "))

                if ins == 1:
                    id = int(input("Enter Insurance ID: "))
                    name = input("Enter Insurance Name: ")
                    add = input("Enter Insurance Address: ")
                    city = input("Enter Insurance City: ")
                    state = input("Enter Insurance State: ")
                    postalc = input("Enter Insurance Postal Code: ")
                    phone = input("Enter Insurance Phone No.: ")
                    email = input("Enter Insurance Email: ")
                    
                    add_insurance(id, name, add, city, state, postalc, phone, email)
                    print("\n")

                elif ins == 2:
                    view_insurance()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")


            elif choice == 9:
                print("THANK YOU !")
                break

            else:
                print("Invalid choice! Please try again.")
                print("\n")

        else:
            print("Wrong Password!")
            break

    else:
        print("Password doest not match with username!")
        break