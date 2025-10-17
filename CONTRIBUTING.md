# Contributing to PydSQL

Thank you for your interest in contributing to PydSQL! We welcome bug fixes, improvements, and new features.

---

## How to Contribute

1. **Fork the repository** and clone it locally:

```bash
git clone https://github.com/YOUR_USERNAME/PydSQL.git
cd PydSQL
```

2. **Create a new branch** for your feature or bugfix:

```bash
git checkout -b feature/my-feature
```

3. **Make your changes.**

4. **Add tests** (if applicable):
   - Place test files in the `tests/` directory.
   - Use `pytest` for testing.

```bash
pytest
```

5. **Run linting and formatting:**

```bash
black pydsql tests
ruff check pydsql tests
```

6. **Commit your changes** with a clear message:

```bash
git commit -m "Add description of your feature or fix"
```

7. **Push your branch** to your fork:

```bash
git push origin feature/my-feature
```

8. **Open a pull request** on the main repository.

---

## Guidelines

- **Follow PEP 8** coding standards.
- **Write clear docstrings** for all public functions.
- **Keep commits atomic and descriptive.**
- **Test thoroughly** before submitting.

---

## Reporting Issues

If you find a bug or have a feature request:

- Open a new issue on GitHub.
- Include steps to reproduce, expected vs. actual behavior, and any relevant code snippets.

---
