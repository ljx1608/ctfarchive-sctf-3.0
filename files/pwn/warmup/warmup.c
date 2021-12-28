#include <stdio.h>
int main() {
    char input[32];
    char flag[32];
    // read flag file
    FILE *f = fopen("flag", "r");
    fgets(flag, 32, f);
    fclose(f);
    // read the user's guess
    fgets(input, 0x32, stdin);
    // if user's guess matches the flag
    if (!strcmp(flag,input)) {
        puts("Predicted!");
        system("cat flag");
    } else puts("Your flag was wrong :(");
}