# susy-test-runner
Automated test runner for labs from Unicamp's SuSy


# Instalation

 * Clone the repository
 * pip
   * if you don't have pip installed, click [here](https://pip.pypa.io/en/stable/installing/)
 * Run setup.sh

# Usage

Run with `test-runner [command] [file] [class]`

**commands**
  * run/r - runs the tests for the file
  * monitore/m - keeps listening the file for changes
  * debug/d - shows only debug the messages

**Note:** The file must have the name of the lab that is going to be tested
E.g. if the lab name is LabSemanal01, the name of the source file must be **labSemanal01.c**
