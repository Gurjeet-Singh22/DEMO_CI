# DEMO_CI
CI Checks & Pre-commit Workflow
To maintain high code quality and consistency across the repository, we have enabled a set of automated CI checks using pre-commit hooks and static analysis tools. Below is a breakdown of each check, why it is used, and how to work with them locally.
✅ Enabled Checks

1. trailing-whitespace
What it does:
Removes any unnecessary whitespace at the end of lines.
Why we use it:
Trailing whitespace is invisible noise that can clutter diffs and reduce readability. Eliminating it keeps commits clean and focused.

2. end-of-file-fixer
What it does:
Ensures that every file ends with a single newline character.
Why we use it:
Many tools and POSIX standards expect files to end with a newline. This avoids unexpected behavior and unnecessary diff changes.

3. check-merge-conflict
What it does:
Detects leftover merge conflict markers such as:
<<<<<<< HEAD
=======
>>>>>>> branch-name
Why we use it:
Prevents accidental commits of unresolved merge conflicts, which can break builds and block deployments.

4. pyright
What it does:
Performs static type checking for Python code.
Why we use it:
Catches type-related bugs early
Improves code reliability and maintainability
Encourages better type annotations

5. pylint
What it does:
Analyzes Python code for stylistic errors, code smells, and potential bugs.
Why we use it:
Enforces coding standards
Improves code readability
Detects common programming errors

⚙️ Pre-commit Workflow
To ensure consistency between local development and CI, follow this workflow:
1. Install dependencies
Make sure you have pre-commit installed:
pip install pre-commit

2. Install git hooks
Run the following command once per repository:
pre-commit install
This sets up the hooks to run automatically before every commit.

3. Run checks manually (optional but recommended)
You can run all checks on all files:
pre-commit run --all-files
Or run on staged files only:
pre-commit run

4. Fix issues
Some hooks (like whitespace fixes) auto-correct issues
Others (like pyright and pylint) require manual fixes
After fixing issues, stage changes again:
git add .
git commit

5. CI enforcement
All the above checks are also enforced in CI.
If any check fails:
The build will fail
You must fix the issues locally before merging

💡 Best Practices
Run pre-commit run --all-files before pushing large changes
Add type hints to new Python code (helps pyright)
Keep commits clean — avoid unnecessary formatting diffs
Fix lint issues early to avoid CI failures
