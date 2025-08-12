

## read

```text
use python to implement the following function:

function name: Edit
function description: 
```markdown
Performs exact string replacements in files.

Usage:
- You must use your `Read` tool at least once in the conversation before editing. This tool will error if you attempt an edit without reading the file.
- When editing text from Read tool output, ensure you preserve the exact indentation (tabs/spaces) as it appears AFTER the line number prefix. The line number prefix format is: spaces + line number + tab. Everything after that tab is the actual file content to match. Never include any part of the line number prefix in the old_string or new_string.
- ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.
- Only use emojis if the user explicitly requests it. Avoid adding emojis to files unless asked.
- The edit will FAIL if `old_string` is not unique in the file. Either provide a larger string with more surrounding context to make it unique or use `replace_all` to change every instance of `old_string`.
- Use `replace_all` for replacing and renaming strings across the file. This parameter is useful if you want to rename a variable for instance.
```

function parameter and desc: 
```
{'file_path': {'type': 'string', 'description': 'The absolute path to the file to modify'}, 'new_string': {'type': 'string', 'description': 'The text to replace it with (must be different from old_string)'}, 'old_string': {'type': 'string', 'description': 'The text to replace'}, 'replace_all': {'type': 'boolean', 'description': 'Replace all occurences of old_string (default false)'}}
```
```