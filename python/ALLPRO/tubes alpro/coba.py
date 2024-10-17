import streamlit as st
import sqlite3
from datetime import datetime

# Create a connection to the database
conn = sqlite3.connect('clinic_appointments.db')
c = conn.cursor()

# Create the appointment table
c.execute('''CREATE TABLE IF NOT EXISTS appointments
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              patient_name TEXT NOT NULL,
              doctor_name TEXT NOT NULL,
              appointment_date TEXT NOT NULL,
              appointment_time TEXT NOT NULL,
              notes TEXT)''')

conn.commit()

# Function to create a connection to the database
def create_connection():
    conn = sqlite3.connect('clinic_appointments.db')
    return conn

# Function to add an appointment
def add_appointment(patient_name, doctor_name, appointment_date, appointment_time, notes):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO appointments (patient_name, doctor_name, appointment_date, appointment_time, notes) VALUES (?, ?, ?, ?, ?)",
              (patient_name, doctor_name, appointment_date, appointment_time.strftime('%H:%M:%S'), notes))
    conn.commit()
    conn.close()

# Function to view all appointments
def view_appointments():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM appointments")
    rows = c.fetchall()
    conn.close()
    return rows

# Function to delete an appointment
def delete_appointment(appointment_id):
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
    conn.commit()
    conn.close()

# Function to update an appointment
def update_appointment(appointment_id, patient_name, doctor_name, appointment_date, appointment_time, notes):
    conn = create_connection()
    c = conn.cursor()
    c.execute("UPDATE appointments SET patient_name = ?, doctor_name = ?, appointment_date = ?, appointment_time = ?, notes = ? WHERE id = ?",
              (patient_name, doctor_name, appointment_date, appointment_time.strftime('%H:%M:%S'), notes, appointment_id))
    conn.commit()
    conn.close()

# Streamlit interface
st.title("Clinic Appointment Management System")

menu = ["Add Appointment", "View Appointments", "Update Appointment", "Delete Appointment"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Appointment":
    st.subheader("Add New Appointment")
    patient_name = st.text_input("Patient Name")
    doctor_name = st.text_input("Doctor Name")
    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")
    notes = st.text_area("Notes")
    
    if st.button("Add Appointment"):
        add_appointment(patient_name, doctor_name, appointment_date.isoformat(), appointment_time, notes)
        st.success(f"Appointment for {patient_name} with Dr. {doctor_name} on {appointment_date} at {appointment_time} added successfully!")

elif choice == "View Appointments":
    st.subheader("View Appointments")
    appointments = view_appointments()
    for appointment in appointments:
        st.write(f"ID: {appointment[0]}")
        st.write(f"Patient Name: {appointment[1]}")
        st.write(f"Doctor Name: {appointment[2]}")
        st.write(f"Appointment Date: {appointment[3]}")
        st.write(f"Appointment Time: {appointment[4]}")
        st.write(f"Notes: {appointment[5]}")
        st.write("---")

elif choice == "Update Appointment":
    st.subheader("Update Appointment")
    appointment_id = st.number_input("Enter Appointment ID to Update", min_value=1, step=1)
    patient_name = st.text_input("New Patient Name")
    doctor_name = st.text_input("New Doctor Name")
    appointment_date = st.date_input("New Appointment Date")
    appointment_time = st.time_input("New Appointment Time")
    notes = st.text_area("New Notes")
    
    if st.button("Update Appointment"):
        update_appointment(appointment_id, patient_name, doctor_name, appointment_date.isoformat(), appointment_time, notes)
        st.success(f"Appointment ID {appointment_id} updated successfully!")

elif choice == "Delete Appointment":
    st.subheader("Delete Appointment")
    appointment_id = st.number_input("Enter Appointment ID to Delete", min_value=1, step=1)
    
    if st.button("Delete Appointment"):
        delete_appointment(appointment_id)
        st.success(f"Appointment ID {appointment_id} deleted successfully!")
