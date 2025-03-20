# StudyConnect

A **Django-based Study Room Collaboration Platform** implementing authentication, authorization, and CRUD operations. Users can create and join study rooms, engage in discussions, and interact with other users in real-time.

## Features
- **User Authentication & Authorization**: Sign Up, Log In, Log Out functionalities with secure user management.
- **Profile Management**: Each user has a profile with customizable avatars.
- **Study Rooms Management**: Create, update, and delete study rooms. Only room creators can modify their rooms.
- **Real-time Messaging**: Users can communicate with others within study rooms through messages.
- **Participant System**: Users can join rooms and engage in discussions as participants.
- **Responsive Design**: User-friendly interface for better user experience.
- **Database Management**: Efficiently handles data storage using Django models.

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript (with potential React integration)
- **Database**: SQLite (Can be upgraded to PostgreSQL or MySQL)
- **Authentication**: Django's built-in authentication system

## Installation
1. Clone the repository:
```bash
$ git clone https://github.com/yourusername/StudyConnect.git
```
2. Navigate to the project directory:
```bash
$ cd StudyConnect
```
3. Create and activate a virtual environment:
```bash
$ python -m venv env
$ source env/bin/activate   # On Windows use `env\Scripts\activate`
```
4. Install dependencies:
```bash
$ pip install -r requirements.txt
```
5. Make migrations and migrate the database:
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
6. Create a superuser for admin access:
```bash
$ python manage.py createsuperuser
```
7. Run the development server:
```bash
$ python manage.py runserver
```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Register or log in with your credentials.
- Create, update, and delete your own study rooms.
- Join rooms created by others and engage in conversations.
- Update your profile and upload custom avatars.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any inquiries or feedback, please reach out at [Your Email Address].


![hero](https://github.com/user-attachments/assets/25228df4-2ec4-4d9f-b919-60dbc6d7b570)
![LoginSignup page](https://github.com/user-attachments/assets/cbc9b606-5e57-46e4-ac84-d5284ca86dce)
![Creating a room](https://github.com/user-attachments/assets/8ad4f10c-6ae6-4b42-ae7a-ed6c49ecab84)
