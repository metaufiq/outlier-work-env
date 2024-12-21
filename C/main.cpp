#include <iostream>
#include <cstdlib>

int main() {
    std::cout << "Before executing command\n";

    // Execute the "mode 650" command
    int result = system("node -v");

    std::cout << "After executing command\n";

    // Check the exit status of the command
    std::cout << result;
    if (result == -1) {
        std::cerr << "Error executing command\n";
    } else {
        std::cout << "Command executed successfully\n";
    }

    return 0;
}