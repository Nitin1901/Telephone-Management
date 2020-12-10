// Including necessary libraries
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

// A person's details datatype which holds the name, phone number and the address
struct Details {
    char phoneno[20];
    char name[20];
    char address[20];
};

// Checking if the phone number entered is valid or not 
int checkDigit(char p[20]) {
    for(int i=0; i<strlen(p); i++) {
        // Invalid if it is not a digit
        if(isdigit(p[i]) == 0) {
            return 0;
        }
    }
    return 1;
}

// Chechking for spaces in the name
int hasSpace(char n[20]) {
    for(int i=0; i<strlen(n); i++) {
        // If there is a space, returns true
        if(n[i]==' ') {
            return 1;
        }
    }
    return 0;
}

// A function which returns the details after taking input
struct Details form() {

    struct Details d;

    // For phone number
    printf("\t\tEnter the phone number: ");
    scanf("%s", d.phoneno);
    // Prompting the user to re-enter if the conditions are not statisfied
    while(strlen(d.phoneno) != 10 || !checkDigit(d.phoneno)) {
        printf("\t\tPhone number should contain 10-digits\n");
        printf("\t\tEnter the phone number: ");
        scanf("%s", d.phoneno);
    }

    // For the name
    printf("\t\tEnter the name without spaces: ");
    scanf("%s", d.name);
    while(strlen(d.name) > 10 || hasSpace(d.name)) {
        printf("\t\tName can't exceed 10 characters\n");
        printf("\t\tEnter the name without spaces: ");
        scanf("%s", d.name);
    }

    // For the city
    printf("\t\tEnter the city: ");
    scanf("%s", d.address);
    while(strlen(d.address) > 20) {
        printf("\t\tCity name can't exceed 20 characters\n");
        printf("\t\tEnter the city: ");
        scanf("%s", d.address);
    }

    // Returning the struct
    return d;

}

// Adding a new customer
void addContact() {

    // Opening the file to write
    FILE *ptr;
    ptr = fopen("telephone_data.txt", "a");
    if(ptr == NULL) {
        printf("\t\tERROR WRITING TO FILE!");
        return;
    }

    // Get the input details from the form
    struct Details formd = form();

    // Writing to the file
    fprintf(ptr, "%s\t", formd.phoneno);
    fprintf(ptr, "%s\t", formd.name);
    fprintf(ptr, "%s\n", formd.address);
    printf("\tDATA ADDED SUCCESSFULLY\n\n");
    fclose(ptr);

    return;

}

// Get the details by address
void getPhone() {
    FILE *ptr;
    ptr = fopen("telephone_data.txt", "r");
    if(ptr == NULL) {
        printf("\t\t\t\tERROR READING FILE!");
        return;
    }
    char search[20];
    printf("\t\t\t\tEnter the phone number to search: ");
    scanf("%s", search);
    char ph[20], name[20], add[20];
    int flag = 0;
    while(fscanf(ptr, "%s", ph) != EOF) {
        fscanf(ptr, "%s", name);
        fscanf(ptr, "%s", add);
        if(strcmp(ph, search)==0) {
            flag = 1;
            printf("\t\t\t\t\t--------------------------\n");
            printf("\t\t\t\t\tPhone number = %s\n", ph);
            printf("\t\t\t\t\tName = %s\n", name);
            printf("\t\t\t\t\tAddress = %s\n", add);
        }
    }
    if(flag == 0) {
        printf("\t\t\t\t\t-----------\n");
        printf("\t\t\t\t\t0 details\n");
        printf("\t\t\t\t\t-----------\n");
    } else {
        printf("\t\t\t\t\t--------------------------\n");
    }
    return;
}

// Get the details by address
void getName() {
    FILE *ptr;
    ptr = fopen("telephone_data.txt", "r");
    if(ptr == NULL) {
        printf("\t\t\t\tERROR READING FILE!");
        return;
    }
    char search[20];
    printf("\t\t\t\tEnter the name to search: ");
    scanf("%s", search);
    char ph[20], name[20], add[20];
    int flag = 0;
    while(fscanf(ptr, "%s", ph) != EOF) {
        fscanf(ptr, "%s", name);
        fscanf(ptr, "%s", add);
        if(strcmp(name, search)==0) {
            flag = 1;
            printf("\t\t\t\t\t--------------------------\n");
            printf("\t\t\t\t\tPhone number = %s\n", ph);
            printf("\t\t\t\t\tName = %s\n", name);
            printf("\t\t\t\t\tAddress = %s\n", add);
        }
    }
    if(flag == 0) {
        printf("\t\t\t\t\t-----------\n");
        printf("\t\t\t\t\t0 details\n");
        printf("\t\t\t\t\t-----------\n");
    } else {
        printf("\t\t\t\t\t--------------------------\n");
    }
    return;
}

// Get the details by address
void getAdd() {
    FILE *ptr;
    ptr = fopen("telephone_data.txt", "r");
    if(ptr == NULL) {
        printf("\t\t\t\tERROR READING FILE!");
        return;
    }
    char search[20];
    printf("\t\t\t\tEnter the address to search: ");
    scanf("%s", search);
    char ph[20], name[20], add[20];
    int flag = 0;
    while(fscanf(ptr, "%s", ph) != EOF) {
        fscanf(ptr, "%s", name);
        fscanf(ptr, "%s", add);
        if(strcmp(add, search)==0) {
            flag = 1;
            printf("\t\t\t\t\t--------------------------\n");
            printf("\t\t\t\t\tPhone number = %s\n", ph);
            printf("\t\t\t\t\tName = %s\n", name);
            printf("\t\t\t\t\tAddress = %s\n", add);
        }
    }
    if(flag == 0) {
        printf("\t\t\t\t\t-----------\n");
        printf("\t\t\t\t\t0 details\n");
        printf("\t\t\t\t\t-----------\n");
    } else {
        printf("\t\t\t\t\t--------------------------\n");
    }
    return;
}

// Get the details of the customer based on various options
void getData() {
    int choice;
    printf("\t\tGet by:-\n");
    printf("\t\t1.Phone number\n");
    printf("\t\t2.Name\n");
    printf("\t\t3.Address\n");
    printf("\t\t\tEnter your choice: ");
    scanf("%d", &choice);
    switch(choice) {
        case 1:
            getPhone();
            break;
        case 2:
            getName();
            break;
        case 3:
            getAdd();
            break;
        default:
            printf("\t\t\t\tWRONG INPUT!\n");
    }
    return;
}

// Menu driven main-function
int main() {
    int choice;
    printf("\n\t\t\t\t---------------------------------------\n");
    printf("\t\t\t\tWELCOME TO TELEPHONE MANAGEMENT SYSTEM");
    printf("\n\t\t\t\t---------------------------------------\n\n");
    printf("\n----------MENU----------\n");
    printf("\n1.Add a contact\n2.Get details\n3.Exit\n\tEnter your choice: ");
    scanf("%d", &choice);
    while(choice != 3) {
        switch(choice) {
            case 1:
                addContact();
                break;
            case 2:
                getData();
                break;
            default:
                printf("\t\tWRONG CHOICE!\n");
        }
        printf("\n----------MENU----------\n");
        printf("\n1.Add a contact\n2.Get details\n3.Exit\n\tEnter your choice: ");
        scanf("%d", &choice);
    }
    printf("\nTHANK YOU!\n\n");
}