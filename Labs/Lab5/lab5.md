## Step 1

nate@nate-ThinkPad-T430:~$ cmake Desktop/Tutorial/step1
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nate
nate@nate-ThinkPad-T430:~$ make
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial

## Step 2

nate@nate-ThinkPad-T430:~$ cmake Desktop/Tutorial/step2
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nate
nate@nate-ThinkPad-T430:~$ make
Scanning dependencies of target MathFunctions
[ 50%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial

## Step 3

nate@nate-ThinkPad-T430:~$ cmake Desktop/Tutorial/step3
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nate
nate@nate-ThinkPad-T430:~$ make
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
nate@nate-ThinkPad-T430:~$ ctest
Test project /home/nate
    Start 1: TutorialRuns
1/5 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialComp25
2/5 Test #2: TutorialComp25 ...................   Passed    0.00 sec
    Start 3: TutorialNegative
3/5 Test #3: TutorialNegative .................   Passed    0.00 sec
    Start 4: TutorialSmall
4/5 Test #4: TutorialSmall ....................   Passed    0.00 sec
    Start 5: TutorialUsage
5/5 Test #5: TutorialUsage ....................   Passed    0.00 sec

100% tests passed, 0 tests failed out of 5

Total Test time (real) =   0.01 sec

## Step 4

nate@nate-ThinkPad-T430:~$ cmake Desktop/Tutorial/step4
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nate
nate@nate-ThinkPad-T430:~$ make
Scanning dependencies of target MathFunctions
[ 50%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
nate@nate-ThinkPad-T430:~$ ctest
Test project /home/nate
    Start 1: TutorialRuns
1/5 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialUsage
2/5 Test #2: TutorialUsage ....................   Passed    0.00 sec
    Start 3: TutorialComp25
3/5 Test #3: TutorialComp25 ...................   Passed    0.00 sec
    Start 4: TutorialComp-25
4/5 Test #4: TutorialComp-25 ..................   Passed    0.00 sec
    Start 5: TutorialComp0.0001
5/5 Test #5: TutorialComp0.0001 ...............   Passed    0.00 sec

100% tests passed, 0 tests failed out of 5

Total Test time (real) =   0.01 sec

## Step 5

nate@nate-ThinkPad-T430:~$ cmake Desktop/Tutorial/step5
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nate
nate@nate-ThinkPad-T430:~$ make
Scanning dependencies of target MakeTable
[ 25%] Building CXX object MathFunctions/CMakeFiles/MakeTable.dir/MakeTable.cxx.o
Linking CXX executable MakeTable
[ 25%] Built target MakeTable
[ 50%] Generating Table.h
Scanning dependencies of target MathFunctions
[ 75%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
Linking CXX static library libMathFunctions.a
[ 75%] Built target MathFunctions
Scanning dependencies of target Tutorial
[100%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
Linking CXX executable Tutorial
[100%] Built target Tutorial
nate@nate-ThinkPad-T430:~$ ctest
Test project /home/nate
    Start 1: TutorialRuns
1/9 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialUsage
2/9 Test #2: TutorialUsage ....................   Passed    0.00 sec
    Start 3: TutorialComp4
3/9 Test #3: TutorialComp4 ....................   Passed    0.00 sec
    Start 4: TutorialComp9
4/9 Test #4: TutorialComp9 ....................   Passed    0.00 sec
    Start 5: TutorialComp5
5/9 Test #5: TutorialComp5 ....................   Passed    0.00 sec
    Start 6: TutorialComp7
6/9 Test #6: TutorialComp7 ....................   Passed    0.00 sec
    Start 7: TutorialComp25
7/9 Test #7: TutorialComp25 ...................   Passed    0.00 sec
    Start 8: TutorialComp-25
8/9 Test #8: TutorialComp-25 ..................   Passed    0.00 sec
    Start 9: TutorialComp0.0001
9/9 Test #9: TutorialComp0.0001 ...............   Passed    0.00 sec

100% tests passed, 0 tests failed out of 9

Total Test time (real) =   0.01 sec



