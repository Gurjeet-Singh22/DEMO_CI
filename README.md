🔍 CI Checks & Pre-commit Workflow
To maintain high code quality and consistency across the repository, we use pre-commit hooks and static analysis tools. Below is a breakdown of each check and how to work with them.
--------------------------------------------------------------------------------------------------------------------------------------------------------
✅ Enabled Checks
1. trailing-whitespace
What it does:
Removes unnecessary whitespace at the end of lines.
Why we use it:
Trailing whitespace creates noisy diffs and reduces readability.
--------------------------------------------------------------------------------------------------------------------------------------------------------

2. end-of-file-fixer
What it does:
Ensures files end with a single newline.
Why we use it:
Required by POSIX standards and prevents unnecessary diff changes.
--------------------------------------------------------------------------------------------------------------------------------------------------------

3. check-merge-conflict
What it does:
Detects unresolved merge conflict markers like:
<<<<<<< HEAD
=======
>>>>>>> branch-name
Why we use it:
Prevents broken commits caused by unresolved conflicts.
--------------------------------------------------------------------------------------------------------------------------------------------------------

4. pyright

What it does:
Performs static type checking for Python.

Why we use it:

Catches type-related bugs early
Improves maintainability
Encourages proper type annotations
--------------------------------------------------------------------------------------------------------------------------------------------------------

5. pylint

What it does:
Analyzes Python code for errors, style issues, and bad practices.

Why we use it:

Enforces coding standards
Improves readability
Detects common bugs
--------------------------------------------------------------------------------------------------------------------------------------------------------

⚙️ Pre-commit Workflow
1. Install pre-commit
```
pip install pre-commit
```
--------------------------------------------------------------------------------------------------------------------------------------------------------
2. Install git hooks
```
pre-commit install
```

This sets up hooks to run automatically before each commit.
--------------------------------------------------------------------------------------------------------------------------------------------------------
3. Run checks manually (recommended)
Run on all files:
```
pre-commit run --all-files
Run on staged files only:
pre-commit run
```
--------------------------------------------------------------------------------------------------------------------------------------------------------
4. Fix issues
Some issues are auto-fixed (e.g., whitespace)
Others (pyright, pylint) must be fixed manually
After fixing:

```
git add .
git commit
```

--------------------------------------------------------------------------------------------------------------------------------------------------------
5. CI Enforcement
All checks run in CI as well.
If any check fails:
The build fails
Fix issues locally before merging
--------------------------------------------------------------------------------------------------------------------------------------------------------
💡 Best Practices

Run checks before pushing changes
Add type hints to new Python code
Keep commits clean and focused
Address lint issues early