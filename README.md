# Dental-Advance: Client Face Recognition System

Dental-Advance is a robust client face recognition system tailored for dental practices. Upon recognizing a client's face as they arrive, the system promptly sends an email notification containing key information about their last appointment, outstanding balances, and the agenda for their current appointment.

## Features:
- Face recognition for client identification.
- Automatic email notifications upon client arrival.
- Easy client data management through a simple UI.

## Getting Started:

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites:
- Python 3.x

### Installation:

1. Clone the repository to your local machine:
```bash
git clone https://github.com/ageorgariou/Dental-Advance.git
```
2. Navigate to the project directory:
```bash
cd Dental-Advance
```
3. Run the script to install the required dependencies:
    - On Windows:
    ```bash
    install_dependencies.bat
    ```

### Email Configuration:

1. Update the `EMAIL_PASSWORD`, `email_sender`, and `email_recipient` variables in your script.
2. To generate an app-specific password for `EMAIL_PASSWORD`, follow this [tutorial](https://www.youtube.com/watch?v=hXiPshHn9Pw).

## Usage:

### Setting Up Client Images:

1. Create a folder named `Images` in the project directory.
2. Add client photos to the `Images` folder, naming each photo with the format `FirstName LastName.jpg`.

### Updating Client Information:

1. Run the `client_data_entry.py` script:
```bash
python client_data_entry.py
```
2. Follow the prompts to add or update the client's information in the database.

### Running the Face Recognition System:

1. Execute the main script:
```bash
python main.py
```
2. The system will now monitor for client arrivals and send email notifications accordingly.

## Contributing:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License:

[MIT](https://choosealicense.com/licenses/mit/)
