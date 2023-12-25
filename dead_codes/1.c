#include <stdio.h>

// Function with dead code
void unusedFunction() {
    printf("This function is never called.\n");
}

int main() {
    // Function call
    usedFunction();

    return 0;
}

// Function with actual use
void usedFunction() {
    printf("This function is called.\n");
}
