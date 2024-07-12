class Patient:
    def _init_(self, patient_id, name, date_of_birth, gender, contact_info):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_info = contact_info

    def _str_(self):
        return f"Patient[ID={self.patient_id}, Name={self.name}, DOB={self.date_of_birth}, Gender={self.gender}, Contact={self.contact_info}]"
    # class patient is for getting patients info


class PatientManagement:
    def _init_(self):
        self.patients = {}

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def update_patient(self, patient_id, **kwargs):
        if patient_id in self.patients:
            for key, value in kwargs.items():
                setattr(self.patients[patient_id], key, value)

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]

    def get_patient(self, patient_id):
        return self.patients.get(patient_id, "Patient not found")


class Doctor:
    def _init_(self, doctor_id, name, specialty, contact_info, available_dates):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.contact_info = contact_info
        self.available_dates = available_dates

    def _str_(self):
        return f"Doctor[ID={self.doctor_id}, Name={self.name}, Specialty={self.specialty}, Contact={self.contact_info}, Available Dates={self.available_dates}]"


class DoctorManagement:
    def _init_(self):
        self.doctors = {}

    def add_doctor(self, doctor):
        self.doctors[doctor.doctor_id] = doctor

    def update_doctor(self, doctor_id, **kwargs):
        if doctor_id in self.doctors:
            for key, value in kwargs.items():
                setattr(self.doctors[doctor_id], key, value)

    def delete_doctor(self, doctor_id):
        if doctor_id in self.doctors:
            del self.doctors[doctor_id]

    def get_doctor(self, doctor_id):
        return self.doctors.get(doctor_id, "Doctor not found")


class Appointment:
    def _init_(self, appointment_id, patient_id, doctor_id, appointment_date, reason):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.reason = reason

    def _str_(self):
        return f"Appointment[ID={self.appointment_id}, Patient ID={self.patient_id}, Doctor ID={self.doctor_id}, Date={self.appointment_date}, Reason={self.reason}]"


class AppointmentManagement:
    def _init_(self):
        self.appointments = {}

    def schedule_appointment(self, appointment):
        self.appointments[appointment.appointment_id] = appointment

    def update_appointment(self, appointment_id, **kwargs):
        if appointment_id in self.appointments:
            for key, value in kwargs.items():
                setattr(self.appointments[appointment_id], key, value)

    def cancel_appointment(self, appointment_id):
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]

    def get_appointment(self, appointment_id):
        return self.appointments.get(appointment_id, "Appointment not found")
