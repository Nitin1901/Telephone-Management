// Including necessary libraries
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include"helper.h"

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
    printf("\n---------------------------------------\n");
    printf("WELCOME TO TELEPHONE MANAGEMENT SYSTEM");
    printf("\n---------------------------------------\n\n");
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