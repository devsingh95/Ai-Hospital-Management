import datetime
import random

# --------- Data Storage ---------
patients = []
doctors = [
    {"id": 1, "name": "Dr. Sharma", "specialization": "Cardiologist"},
    {"id": 2, "name": "Dr. Mehta", "specialization": "Neurologist"},
    {"id": 3, "name": "Dr. Gupta", "specialization": "General Physician"}
]

appointments = []

# --------- AI-like Health Suggestion ---------
def ai_health_suggestion(symptoms):
    suggestions = {
        "fever": "Possible flu or infection. Suggested doctor: General Physician",
        "chest pain": "Possible heart issue. Suggested doctor: Cardiologist",
        "headache": "Possible stress or migraine. Suggested doctor: Neurologist",
        "cough": "Possible cold or lung infection. Suggested doctor: General Physician"
    }
    for key in suggestions:
        if key in symptoms.lower():
            return suggestions[key]
    return "No clear suggestion. Please consult General Physician."

# --------- Core Functions ---------
def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    symptoms = input("Enter symptoms: ")
    patient = {
        "id": len(patients) + 1,
        "name": name,
        "age": age,
        "symptoms": symptoms
    }
    patients.append(patient)
    print(f"✅ Patient {name} added successfully.")
    print("🤖 AI Suggestion:", ai_health_suggestion(symptoms))

def book_appointment():
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    date = input("Enter appointment date (YYYY-MM-DD): ")
    appointment = {
        "id": len(appointments) + 1,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date
    }
    appointments.append(appointment)
    print("📅 Appointment booked successfully!")

def show_patients():
    print("\n--- Patient List ---")
    for p in patients:
        print(f"ID: {p['id']} | Name: {p['name']} | Age: {p['age']} | Symptoms: {p['symptoms']}")

def show_doctors():
    print("\n--- Doctor List ---")
    for d in doctors:
        print(f"ID: {d['id']} | Name: {d['name']} | Specialization: {d['specialization']}")

def show_appointments():
    print("\n--- Appointment List ---")
    for a in appointments:
        p = next((p for p in patients if p["id"] == a["patient_id"]), None)
        d = next((d for d in doctors if d["id"] == a["doctor_id"]), None)
        print(f"ID: {a['id']} | Patient: {p['name']} | Doctor: {d['name']} | Date: {a['date']}")

# --------- Menu ---------
def main():
    while True:
        print("\n🏥 AI Hospital Management System")
        print("1. Add Patient")
        print("2. Book Appointment")
        print("3. Show Patients")
        print("4. Show Doctors")
        print("5. Show Appointments")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_patient()
        elif choice == "2":
            book_appointment()
        elif choice == "3":
            show_patients()
        elif choice == "4":
            show_doctors()
        elif choice == "5":
            show_appointments()
        elif choice == "6":
            print("Exiting... ✅")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
