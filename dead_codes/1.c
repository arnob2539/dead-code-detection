#include <stdio.h>

void usedFunction() {
    printf("This function is used.\n");
}

void unusedFunction() {
    printf("This function is never used.\n");
}

int main() {
    usedFunction();
    // Commenting out the next line to create potential dead code
    // unusedFunction();

    return 0;
}
