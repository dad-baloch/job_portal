# Flask Job Portal

A simple, yet robust job portal web application built with Python and Flask. This project allows users to browse job listings, view detailed descriptions, and submit applications. It's designed to be a showcase of a full-stack web application using modern development practices.

## Features

- **Dynamic Job Listings:** Jobs are loaded dynamically from a MySQL database.
- **View Job Details:** Click on any job to see a detailed page with responsibilities and requirements.
- **Application Submission:** A user-friendly form to apply for jobs, with data being saved to the database.
- **Contact Form:** A simple contact form for user inquiries.
- **Responsive Design:** Built with Bootstrap for a seamless experience on all devices.
- **SQLAlchemy ORM:** Utilizes SQLAlchemy for elegant and efficient database interactions.

## Technologies Used

- **Backend:** Python, Flask
- **Database:** MySQL, SQLAlchemy
- **Frontend:** HTML, CSS, Bootstrap 5
- **Environment Variables:** `python-dotenv`

## Setup and Installation

To get this project up and running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dad-baloch/Flask_with_Josh.git
    cd "GitHub Projects/job_portal"
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    *On Windows, use `.venv\Scripts\activate`*

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root of the `job_portal` directory and add your database connection string:
    ```
    DB_URL="mysql+pymysql://<user>:<password>@<host>/<dbname>"
    ```
    Replace `<user>`, `<password>`, `<host>`, and `<dbname>` with your MySQL database credentials.

5.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

## Database Schema

The application uses two main tables: `jobs` and `form` (for applications).

### `jobs` table
- `id` (Integer, Primary Key)
- `title` (String)
- `location` (String)
- `salary` (Integer)
- `currency` (String)
- `responsibility` (String)
- `requirements` (String)

### `form` table
- `id` (Integer, Primary Key)
- `full_name` (String)
- `email` (String)
- `education` (String)
- `work_experience` (String)
- `resume_url` (String)
- `job_id` (Integer, Foreign Key to `jobs.id`)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



<img width="1359" height="653" alt="navbar_about" src="https://github.com/user-attachments/assets/a058d3f0-d9f6-4dd5-ac4b-f0146f790db6" />
<img width="1359" height="653" alt="jobs" src="https://github.com/user-attachments/assets/18a3a228-1598-45e4-8a9c-27a1b5a65548" />
<img width="1359" height="653" alt="footer_contact_us" src="https://github.com/user-attachments/assets/405f7110-30d7-4f1d-85f8-5d64f29f5777" />
<img width="1359" height="653" alt="job_details" src="https://github.com/user-attachments/assets/afdadff5-7637-447d-9ad6-b40901e9a33a" />
<img width="1359" height="653" alt="application_form" src="https://github.com/user-attachments/assets/fd46d9a3-0a9a-4f1c-962a-e9421bb550ab" />
