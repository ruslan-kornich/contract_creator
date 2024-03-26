# Contract creator

The web application creates a standard contract between the supplier of goods and the buyer.
It is enough to enter the code (EDPNOU) and the IBAN bank account number of the company with which you want to conclude an agreement.
At the output, we get a file with a contract in the dox format with filled in data about the company
The script automatically substitutes all the necessary data for the contract
## Example  Contract Creator Page 

![Example Short URL page](./screenshots/example.png)


## Getting Started


To run the project locally first you need to clone the repository:

```bash
https://github.com/ruslan-kornich/contract_creator.git
```

Create a virtualenv and activate:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

Install the development requirements:
```bash
pip install -r requirements.txt
```

Run the local server:
```bash
python manage.py runserver
```
