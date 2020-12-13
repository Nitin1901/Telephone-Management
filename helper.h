// A person's details datatype which holds the name, phone number and the address
struct Details {
    char phoneno[20];
    char name[20];
    char address[20];
};

// Checking if the phone number entered is valid or not 
int checkDigit(char p[20]);

// Checking for spaces in the name
int hasSpace(char n[20]);

// A function which returns the details after taking input
struct Details form();

// Adding a new customer
void addContact();

// Get the details by phone
void getPhone();

// Get the details by name
void getName();

// Get the details by address
void getAdd();
