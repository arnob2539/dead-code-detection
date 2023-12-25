#include <stdio.h>

void unusedFunction() {
    printf("This function is never called.\n");
}

void usedFunction() {
    printf("This function is called.\n");
}


int main() {
    usedFunction();

    return 0;
}

