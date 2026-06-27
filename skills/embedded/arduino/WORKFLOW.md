# Arduino Workflow

## 1. Identify the Arduino surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for Arduino and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for microcontroller sketches, sensors, serial I/O, timing loops, memory limits, and library integration.

## 5. Verify with the right tools
Use compile checks, serial monitor validation, pin mapping review, timing tests, and hardware smoke tests. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to Arduino.

