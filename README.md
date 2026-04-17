# DG2000 Trigger

DG2000 Trigger is a lightweight desktop controller (PySide6 + PyVISA) for Rigol DG2000 series generators.

It is designed for repeatable two-channel timing control in lab automation workflows:
- CH1 outputs a sine waveform with a configurable cycle (active segment + silent segment).
- CH2 emits one pulse after each CH1 active segment ends, with configurable extra delay.

Typical use cases include synchronized acquisition triggering, timing orchestration, and repetitive test execution.
