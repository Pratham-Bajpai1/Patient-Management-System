-- CREATE DATABASE / SCHEMA
CREATE DATABASE patienttracking;

-- Create Patients Table
CREATE TABLE Patients (
  PatientID INT PRIMARY KEY,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Gender VARCHAR(10) NOT NULL,
  DateOfBirth INT NOT NULL,
  Address TEXT NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  PostalCode VARCHAR(20) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  InsuranceID INT NOT NULL,
  FOREIGN KEY (InsuranceID) REFERENCES Insurance(InsuranceID)
  ON DELETE CASCADE
);

-- Create Doctors Table
CREATE TABLE Doctors (
  DoctorID INT PRIMARY KEY,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Speciality VARCHAR(255) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Email VARCHAR(255) NOT NULL
);

-- Create Appointments Table
CREATE TABLE Appointments (
  AppointmentID INT PRIMARY KEY,
  PatientID INT NOT NULL,
  DoctorID INT NOT NULL,
  AppointmentDate INT NOT NULL,
  AppointmentTime TIME NOT NULL,
  AppointmentNotes TEXT,
  FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
  FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
  ON DELETE CASCADE
);

-- Create MedicalTests Table
CREATE TABLE MedicalTests (
  MedicalTestID INT PRIMARY KEY,
  PatientID INT NOT NULL,
  DoctorID INT NOT NULL,
  TestName VARCHAR(255) NOT NULL,
  TestDate INT NOT NULL,
  TestResults TEXT,
  FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
  FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
  ON DELETE CASCADE
);

-- Create Treatments Table
CREATE TABLE Treatments (
  TreatmentID INT PRIMARY KEY,
  PatientID INT NOT NULL,
  DoctorID INT NOT NULL,
  TreatmentDate INT NOT NULL,
  TreatmentNotes TEXT,
  FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
  FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
  ON DELETE CASCADE
);

-- Create Staff Table
CREATE TABLE Staff (
  StaffID INT PRIMARY KEY,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  JobTitle VARCHAR(255) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Email VARCHAR(255) NOT NULL
);

-- Create Diagnoses Table
CREATE TABLE Diagnoses (
  DiagnosisID INT PRIMARY KEY,
  PatientID INT NOT NULL,
  DoctorID INT NOT NULL,
  DiagnosisDate INT NOT NULL,
  DiagnosisNotes TEXT,
  FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
  FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
  ON DELETE CASCADE
);

-- Create Insurance Table
CREATE TABLE Insurance (
  InsuranceID INT PRIMARY KEY,
  InsuranceName VARCHAR(255) NOT NULL,
  InsuranceAddress TEXT NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  PostalCode VARCHAR(20) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Email VARCHAR(255) NOT NULL
);

-- Sample data for Patients Table
INSERT INTO Patients (PatientID, FirstName, LastName, Gender, DateOfBirth, Address, City, State, PostalCode, Phone, Email, InsuranceID) VALUES
(1, 'Ramesh', 'Kumar', 'Male', '1992-08-10', '456 Gandhi Road', 'Delhi', 'Delhi', '110001', '9876543210', 'ramesh.kumar@example.com', 1),
(2, 'Priya', 'Patel', 'Female', '1988-03-25', '123 Nehru Street', 'Mumbai', 'Maharashtra', '400001', '9876543211', 'priya.patel@example.com', 2),
(3, 'Amit', 'Sharma', 'Male', '1990-11-15', '789 Tagore Nagar', 'Kolkata', 'West Bengal', '700001', '9876543212', 'amit.sharma@example.com', 1),
(4, 'Anjali', 'Verma', 'Female', '1995-05-02', '101 Gandhi Path', 'Jaipur', 'Rajasthan', '302001', '9876543213', 'anjali.verma@example.com', 2);

-- Sample data for Doctors Table
INSERT INTO Doctors (DoctorID, FirstName, LastName, Speciality, Phone, Email) VALUES
(1, 'Dr. Suresh', 'Gupta', 'Cardiologist', '9876543214', 'suresh.gupta@example.com'),
(2, 'Dr. Priya', 'Shah', 'Pediatrician', '9876543215', 'priya.shah@example.com'),
(3, 'Dr. Rohit', 'Patil', 'Dermatologist', '9876543216', 'rohit.patil@example.com'),
(4, 'Dr. Deepika', 'Singh', 'Orthopedic Surgeon', '9876543217', 'deepika.singh@example.com');

-- Sample data for Appointments Table
INSERT INTO Appointments (AppointmentID, PatientID, DoctorID, AppointmentDate, AppointmentTime, AppointmentNotes) VALUES
(1, 1, 1, '2024-05-15', '10:00:00', 'Regular checkup'),
(2, 2, 2, '2024-05-20', '14:30:00', 'Vaccination appointment'),
(3, 3, 3, '2024-05-18', '11:00:00', 'Skin consultation'),
(4, 4, 4, '2024-05-22', '16:00:00', 'Orthopedic examination');

-- Sample data for MedicalTests Table
INSERT INTO MedicalTests (MedicalTestID, PatientID, DoctorID, TestName, TestDate, TestResults) VALUES
(1, 1, 1, 'Blood Test', '2024-05-18', 'Normal'),
(2, 2, 2, 'X-Ray', '2024-05-22', 'No abnormalities detected'),
(3, 3, 3, 'Skin Biopsy', '2024-05-19', 'Positive for fungal infection'),
(4, 4, 4, 'MRI Scan', '2024-05-25', 'Fracture detected in right arm');

-- Sample data for Treatments Table
INSERT INTO Treatments (TreatmentID, PatientID, DoctorID, TreatmentDate, TreatmentNotes) VALUES
(1, 1, 1, '2024-05-16', 'Prescribed medication for high blood pressure'),
(2, 2, 2, '2024-05-21', 'Administered vaccine for measles'),
(3, 3, 3, '2024-05-20', 'Prescribed antifungal cream for skin infection'),
(4, 4, 4, '2024-05-26', 'Suggested arm splint for fracture');

-- Sample data for Staff Table
INSERT INTO Staff (StaffID, FirstName, LastName, JobTitle, Phone, Email) VALUES
(1, 'Sunita', 'Mishra', 'Nurse', '9876543218', 'sunita.mishra@example.com'),
(2, 'Rahul', 'Kumar', 'Receptionist', '9876543219', 'rahul.kumar@example.com'),
(3, 'Anita', 'Sharma', 'Pharmacist', '9876543220', 'anita.sharma@example.com'),
(4, 'Manoj', 'Singh', 'Lab Technician', '9876543221', 'manoj.singh@example.com');

-- Sample data for Diagnoses Table
INSERT INTO Diagnoses (DiagnosisID, PatientID, DoctorID, DiagnosisDate, DiagnosisNotes) VALUES
(1, 1, 1, '2024-05-16', 'Diagnosed with hypertension'),
(2, 2, 2, '2024-05-21', 'Diagnosed with measles'),
(3, 3, 3, '2024-05-20', 'Diagnosed with fungal infection of the skin'),
(4, 4, 4, '2024-05-26', 'Diagnosed with fracture in right arm');

-- Sample data for Insurance Table
INSERT INTO Insurance (InsuranceID, InsuranceName, InsuranceAddress, City, State, PostalCode, Phone, Email) VALUES
(1, 'HealthCare India', '567 Health Plaza', 'New Delhi', 'Delhi', '110001', '1800123456', 'info@healthcareindia.com'),
(2, 'CarePlus Insurance', '789 Insurance Tower', 'Mumbai', 'Maharashtra', '400001', '1800987654', 'info@careplusinsurance.com');
