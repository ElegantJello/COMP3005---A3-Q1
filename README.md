Name: Jasmine Jamali
ID: 101156769
Demonstration link: https://www.youtube.com/watch?v=nGzXfKnT2Lk

Database Setup Instructions:

- Create a database in pgAdmin
- Right click database and create a db named "StudentDB"
- Click "Query Tool"
- Copy and paste this query:

-- Create Students Table
CREATE TABLE students (
	student_id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	enrollment_date DATE
);

-- Fill Students Table With Data
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

- Execute query

Application Instructions:

- Install psycopg2 if you don't already have it, by entering 'pip install psycopg2' into the terminal.
- In 'DBScript.py', configure the database connection credentials and enter your own to connect to your db.
- To run the program, type 'python .\DBScript.py' into the terminal.
