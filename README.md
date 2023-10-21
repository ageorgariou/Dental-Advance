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
- OpenCV
- Other dependencies listed in `requirements.txt`

### Installation:

1. Clone the repository to your local machine:
```bash
git clone https://github.com/ageorgariou/Dental-Advance.git
```
2. Navigate to the project directory:
```bash
cd Dental-Advance
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage:

### Adding a New Client:

1. Take a photo of the client.
2. Save the photo in the `Images` folder with the format `FirstName_LastName.jpg`.
3. The system will now recognize this client in subsequent visits.

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

---

Feel free to customize the README to match the exact functionality and style of your project. This structured format ensures that users have a clear understanding of how to install and use your software, and what to expect from it.
