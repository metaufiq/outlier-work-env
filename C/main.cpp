#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <iostream>
using namespace std;

int parseLine(char currentGame[], char opponentName[], int* homeScore, int* opponentScore) {
    // Find the position of the comma in the currentGame string
    char* commaPos = strchr(currentGame, ',');
    if (commaPos == nullptr) {
        // If there is no comma, return an error code
        return 1;
    }

    // Copy the opponent name from the beginning of the string to the comma position
    strncpy(opponentName, currentGame, commaPos - currentGame);
    opponentName[commaPos - currentGame] = '\0';

    // Find the position of the dash in the currentGame string
    char* dashPos = strchr(commaPos + 1, '-');
    if (dashPos == nullptr) {
        // If there is no dash, return an error code
        return 1;
    }

    // Check for spaces or non-number characters in the home score and opponent score strings
    for (char* p = commaPos + 1; p < dashPos; p++) {
        if (!isdigit(*p) && *p != '-') {
            // If there is a space or non-number character, return an error code
            return 1;
        }
    }
    for (char* p = dashPos + 1; *p != '\0'; p++) {
        if (!isdigit(*p)) {
            // If there is a space or non-number character, return an error code
            return 1;
        }
    }

    // Parse the home score and opponent score from the string
    char homeScoreStr[10], opponentScoreStr[10];
    strncpy(homeScoreStr, commaPos + 1, dashPos - commaPos - 1);
    homeScoreStr[dashPos - commaPos - 1] = '\0';
    strcpy(opponentScoreStr, dashPos + 1);
    *homeScore = atoi(homeScoreStr);
    *opponentScore = atoi(opponentScoreStr);

    // If the parsing was successful, return 0
    return 0;
}

void testParseLine() {
    char opponentName[100];
    int homeScore, opponentScore;

    // Test Case 1: Valid input
    char input1[] = "Lakers,102-95";
    int result1 = parseLine(input1, opponentName, &homeScore, &opponentScore);
    cout << "Test Case 1: " << (result1 == 0 && string(opponentName) == "Lakers" && homeScore == 102 && opponentScore == 95 ? "PASS" : "FAIL") << endl;

    // Test Case 2: Missing comma
    char input2[] = "Lakers 102-95";
    int result2 = parseLine(input2, opponentName, &homeScore, &opponentScore);
    cout << "Test Case 2: " << (result2 == 1 ? "PASS" : "FAIL") << endl;

    // Test Case 3: Missing dash
    char input3[] = "Lakers,102 95";
    int result3 = parseLine(input3, opponentName, &homeScore, &opponentScore);
    cout << "Test Case 3: " << (result3 == 1 ? "PASS" : "FAIL") << endl;

    // Test Case 4: Non-numeric scores
    char input4[] = "Lakers,10a2-95";
    int result4 = parseLine(input4, opponentName, &homeScore, &opponentScore);
    cout << "Test Case 4: " << (result4 == 1 ? "PASS" : "FAIL") << endl;

    // Test Case 5: Empty string
    char input5[] = "";
    int result5 = parseLine(input5, opponentName, &homeScore, &opponentScore);
    cout << "Test Case 5: " << (result5 == 1 ? "PASS" : "FAIL") << endl;

    // Test Case 6: Extra spaces
    char input6[] = "Lakers , 102 - 95";
    int result6 = parseLine(input6, opponentName, &homeScore, &opponentScore);
    cout << "Test Case 6: " << (result6 == 1 ? "PASS" : "FAIL") << endl;

    // Test Case 7: Valid input with different team name
    char input7[] = "Warriors,115-112";
    int result7 = parseLine(input7, opponentName, &homeScore, &opponentScore);
    cout << "Test Case 7: " << (result7 == 0 && string(opponentName) == "Warriors" && homeScore == 115 && opponentScore == 112 ? "PASS" : "FAIL") << endl;
}

int main() {
    testParseLine();
    return 0;
}
