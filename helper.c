// Including necessary libraries
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include"helper.h"

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
    printf("\tDATA ADDED SUCCESSFULLY!\n\n");
    fclose(ptr);

    return;

}

// Get the details by phone
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

// Get the details by name
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