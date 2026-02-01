# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.2.0] – 2026-01-31

### Breaking Changes

- Replaced the function-based API with a class-based API.
- Arithmetic operations (`add`, `subtract`, `multiply`, `divide`) are now instance methods of the `Calculator` class.
- Removed top-level function exports from the public API.

### Added

- Introduced the `Calculator` class as the primary public interface.
- Automatic input coercion:
  - Supports `int`, `float`, and numeric `str` values.
  - Inputs are converted internally without requiring explicit casting.
- Centralized input validation using internal utility modules.

### Improved

- Consistent and explicit error handling:
  - Raises `TypeError` for invalid numeric inputs.
  - Raises `ValueError` for division by zero.
- Improved internal project structure to support future extensibility.
- Updated test suite to reflect the new class-based design.

### Internal

- Added internal `utils.convert_to_num` helper for numeric normalization.
- Clarified public API boundaries by limiting exports to supported interfaces.

### Migration Guide

**Before (v0.1.x):**

```python
from mathlib import add
add(2, 3)
```

**After (v0.2.0):**

```python
from mathlib import Calculator

calc = Calculator()
calc.add(2, 3)
```

---

## [0.1.1] - 2026-01-31

### Fixed

- Standardized zero-division handling in `divide()` by raising `ValueError`
- Aligned test cases with updated error behavior

---

## [0.1.0] - 2026-01-31

### Added

- Initial public release of **mathlibxyz**
- Core arithmetic operations:
  - `add`
  - `subtract`
  - `multiply`
  - `divide`
- Explicit error handling for division by zero
