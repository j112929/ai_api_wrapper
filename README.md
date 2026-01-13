# ai_api_wrapper

## 🚀 How to Run
Now you can simply use:
* Setup: make setup (Installs venv and dependencies)
* Run: make run (Runs the migration tool)
* Demo: make demo (Runs in demo mode)
* Clean: make clean (Removes temporary files)

## Test COBOL Code

```
python main.py bank_core_legacy.cbl
```

##output
```
============================================================
🚀 LEGACY SYSTEM TRANSFORMATION ENGINE V1.0
============================================================
ℹ️  [INFO]    Parsing legacy structure from bank_core_legacy.cbl...
✅ [SUCCESS] Extracted Data Schema: 3 fields identified.
ℹ️  [INFO]    Architecting modern Python microservice...
✅ [SUCCESS] Generated Python Microservice logic.

============================================================
🚀 STARTING SHADOW VERIFICATION LOOP
============================================================
✅ Case #01: MATCH | Input: {'PRINCIPAL': 3438072.75, 'RATE': 43.42, 'TERM': 1... | Result: 18660139.85
✅ Case #02: MATCH | Input: {'PRINCIPAL': 4047198.18, 'RATE': 18.45, 'TERM': 4... | Result: 2924606.58
✅ Case #03: MATCH | Input: {'PRINCIPAL': 4058641.37, 'RATE': 73.97, 'TERM': 1... | Result: 48785376.60
✅ Case #04: MATCH | Input: {'PRINCIPAL': 3903950.91, 'RATE': 87.17, 'TERM': 3... | Result: 85644029.21
✅ Case #05: MATCH | Input: {'PRINCIPAL': 7384799.64, 'RATE': 5.26, 'TERM': 31... | Result: 10131822.03
✅ Case #06: MATCH | Input: {'PRINCIPAL': 3389547.69, 'RATE': 59.62, 'TERM': 2... | Result: 46816319.71
✅ Case #07: MATCH | Input: {'PRINCIPAL': 5301222.22, 'RATE': 26.0, 'TERM': 20... | Result: 23431402.21
✅ Case #08: MATCH | Input: {'PRINCIPAL': 407157.97, 'RATE': 93.13, 'TERM': 27... | Result: 8594887.60
✅ Case #09: MATCH | Input: {'PRINCIPAL': 1853778.43, 'RATE': 47.16, 'TERM': 2... | Result: 20763245.31
✅ Case #10: MATCH | Input: {'PRINCIPAL': 4520171.79, 'RATE': 38.13, 'TERM': 1... | Result: 23985952.59

📊 MIGRATION AUDIT SUMMARY
------------------------------
Total Fields Analyzed : 3
Test Cases Generated  : 10
Verified Exact Matches: 10
Precision Level       : Decimal-128
Risk Assessment       : LOW
------------------------------

✅ [SUCCESS] Production-ready code saved to 'modernized_api.py' in 2.51s
```

## Test Fortran Code

```
python main.py bank_core_legacy.f90
``` 

##output

```
============================================================
🚀 LEGACY SYSTEM TRANSFORMATION ENGINE V1.0
============================================================
ℹ️  [INFO]    Parsing legacy structure from bank_core_legacy.f90...
✅ [SUCCESS] Extracted Data Schema: 3 fields identified.
ℹ️  [INFO]    Architecting modern Python microservice...
✅ [SUCCESS] Generated Python Microservice logic.

============================================================
🚀 STARTING SHADOW VERIFICATION LOOP
============================================================
✅ Case #01: MATCH | Input: {'PRINCIPAL': 4785172.24, 'RATE': 29.88, 'TERM': 8... | Result: 10485269.41
✅ Case #02: MATCH | Input: {'PRINCIPAL': 6124403.51, 'RATE': 35.11, 'TERM': 9... | Result: 16127085.54
✅ Case #03: MATCH | Input: {'PRINCIPAL': 8499171.09, 'RATE': 79.93, 'TERM': 2... | Result: 141528905.25
✅ Case #04: MATCH | Input: {'PRINCIPAL': 8504363.87, 'RATE': 80.93, 'TERM': 6... | Result: 3441290.84
✅ Case #05: MATCH | Input: {'PRINCIPAL': 7455007.16, 'RATE': 64.7, 'TERM': 11... | Result: 44214404.96
✅ Case #06: MATCH | Input: {'PRINCIPAL': 2813366.9, 'RATE': 40.04, 'TERM': 20... | Result: 19431643.84
✅ Case #07: MATCH | Input: {'PRINCIPAL': 3889391.83, 'RATE': 99.68, 'TERM': 3... | Result: 105646772.40
✅ Case #08: MATCH | Input: {'PRINCIPAL': 4190505.61, 'RATE': 12.47, 'TERM': 3... | Result: 13847735.31
✅ Case #09: MATCH | Input: {'PRINCIPAL': 9759429.29, 'RATE': 8.72, 'TERM': 25... | Result: 17729629.88
✅ Case #10: MATCH | Input: {'PRINCIPAL': 2218161.4, 'RATE': 59.49, 'TERM': 90... | Result: 9896881.63

📊 MIGRATION AUDIT SUMMARY
------------------------------
Total Fields Analyzed : 3
Test Cases Generated  : 10
Verified Exact Matches: 10
Precision Level       : Decimal-128
Risk Assessment       : LOW
------------------------------

✅ [SUCCESS] Production-ready code saved to 'modernized_api.py' in 2.51s
```
