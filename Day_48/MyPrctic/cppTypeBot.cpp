#include <iostream>
#include <windows.h>

int main() {
    std::string sentence = "Babies are born without knee caps. They don't appear until the child reaches 2-6 years of age. Modern records do not compare with that of St Simeon the younger of his life living at the top of a stone pillar on the hill of wounders near Antioch in Syria! 14% of all facts and statistics are made up and 27% of people know that fact.";
    int length = sentence.length();

    std::cout << "Get ready..." << std::endl;
    Sleep(3000);

    for (int c = 0; c < length; ++c) {
        INPUT inputs[2] = {};

        inputs[0].type = INPUT_KEYBOARD;
        inputs[0].ki.wVk = 0;
        inputs[0].ki.dwFlags = KEYEVENTF_UNICODE;
        inputs[0].ki.wScan = sentence[c];
        inputs[0].ki.time = 0;
        inputs[0].ki.dwExtraInfo = GetMessageExtraInfo();

        inputs[1].type = INPUT_KEYBOARD;
        inputs[1].ki.wVk = 0;
        inputs[1].ki.dwFlags = KEYEVENTF_UNICODE | KEYEVENTF_KEYUP;
        inputs[1].ki.wScan = sentence[c];
        inputs[1].ki.time = 0;
        inputs[1].ki.dwExtraInfo = GetMessageExtraInfo();

        SendInput(2, inputs, sizeof(INPUT));

        Sleep(50);  // Sleep for 50 milliseconds between characters
    }

    std::cout << "\nFinished typing the sentence." << std::endl;

    return 0;
}
