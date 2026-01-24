# 📚 Library Management System

A complete **Library Management System (LMS)** developed using **Django** that allows administrators to manage books, students, book issuing, returning, and track due/late statuses efficiently.

---

## 🔹 1. SYSTEM START

- System starts
- Display **Login Page** to the user

---

## 🔹 2. LOGIN MODULE

**Inputs:**
- Username
- Password

**Process:**
```

IF username AND password are valid THEN
Open Dashboard
ELSE
Display "Invalid Username or Password"
Stay on Login Page
END IF

```

---

## 🔹 3. DASHBOARD MODULE

The dashboard provides a complete overview of the library system.

**Displayed Information:**
- Total Books
- Available Books
- Issued Books
- Total Students

**Available Actions (Buttons):**
- Add Book
- Issue Book
- Return Book
- Students
- Subjects
- Logout

---

## 🔹 4. SUBJECT MANAGEMENT

- User selects a **Subject**
- System fetches all books related to that subject
- Displays the **list of books** under the selected subject

---

## 🔹 5. ADD BOOK MODULE

**Steps:**
- User clicks **Add Book**
- Display **Add Book Form**

**Inputs:**
- Book Name
- Author Name
- Subject
- Quantity

**Process:**
- Save book data in database
- Update **Total Books Count**
- Update **Available Books Count**

**Output:**
- Display message **"Book Added Successfully"**

---

## 🔹 6. STUDENT MANAGEMENT MODULE

**Steps:**
- User clicks **Students**
- Display **Student Form**

**Inputs:**
- Student Name
- Phone Number
- Email
- Roll Number

**Process:**
- Save student data in database

**Output:**
- Display message **"Student Added Successfully"**

---

## 🔹 7. ISSUE BOOK MODULE

**Steps:**
- User clicks **Issue Book**

**Inputs:**
- Select Student
- Select Book
- Issue Date (Auto set to Current Date)
- Return Date (Issue Date + Defined Days)

**Process:**
```

IF Book Quantity > 0 THEN
Issue Book to Student
Decrease Book Quantity
Increase Issued Books Count
Display "Book Issued Successfully"
ELSE
Display "Book Not Available"
END IF

```

---

## 🔹 8. RETURN BOOK MODULE

**Steps:**
- User clicks **Return Book**
- Select Issued Book
- Select Student

**Process:**
- Update book status as **Returned**
- Increase book quantity
- Decrease issued books count

**Output:**
- Display message **"Book Returned Successfully"**

---

## 🔹 9. RETURN DATE REMINDER SYSTEM

The system automatically updates the status of issued books:

```

FOR each Issued Book Record
IF Current Date > Return Date THEN
Mark Status as "Late"
ELSE IF Current Date = Return Date THEN
Mark Status as "Due Today"
ELSE
Mark Status as "On Time"
END IF
END FOR

```

---

## 🔹 10. STUDENT ISSUE RECORD DISPLAY

Displays complete issued book records:

- Student Name
- Book Name
- Issue Date
- Return Date
- Status (On Time / Due Today / Late)

---

## 🔹 11. LOGOUT MODULE

**Steps:**
- User clicks **Logout**
- End user session
- Redirect user to **Login Page**

---

## 🔹 12. SYSTEM END

- Stop system
- User session safely closed

---

## ✅ Technologies Used

- Python
- Django Framework
- HTML / CSS
- SQLite Database

---

## 🎯 Project Status

✔ Fully Functional  
✔ All Modules Completed  
✔ Ready for Final Submission  

---

## 👨‍💻 Developed By

**Syeda Husna Zafar**  
Library Management System Project//
Date: 25-01-2026
---