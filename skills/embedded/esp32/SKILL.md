# ESP32 Skill Definition

## Capability
Use this skill for Wi-Fi, Bluetooth, FreeRTOS tasks, GPIO, power modes, OTA updates, and embedded networking. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with firmware build, serial logs, Wi-Fi reconnect tests, task watchdog checks, and power draw review.

## Best for
- Designing or modifying ESP32-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on ESP32 tooling or runtime behavior.
- Creating prompts or workflows that require accurate ESP32 terminology.

## Inputs
- User goal, acceptance criteria, and affected environment.
- Relevant source files, config files, dependencies, logs, or test output.
- Version constraints and deployment context.
- Security, performance, accessibility, reliability, or maintenance requirements.

## Outputs
- Focused plan, implementation, review, or debugging guidance.
- Technology-specific risks, tradeoffs, and verification steps.
- Updated docs or examples when behavior or usage changes.

## Watch for
Avoid blocking network calls, watchdog resets, unsafe OTA, credential storage issues, and concurrency races.

