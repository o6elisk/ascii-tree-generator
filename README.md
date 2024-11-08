# Directory Tree Generator 🌳

A lightweight Python script to generate ASCII directory trees while intelligently ignoring framework-specific files and directories.

## Features

- 📁 Generates ASCII directory trees
- 💾 Saves output to both console and file
- 🚫 Smart ignore patterns for different frameworks
- 🔧 Easily customizable ignore patterns
- 🐍 No dependencies - uses Python standard library

## Usage

1. Copy `tree_generator.py` to your project root
2. Make it executable (optional):
   ```bash
   chmod +x tree_generator.py
   ```
3. Run the script:
   ```bash
   python tree_generator.py
   ```

The script will:
- Display the tree in your terminal
- Save the tree to `directory_structure.txt` in the same directory as the script.

## Framework-Specific Instructions

### Python/FastAPI Projects
The default configuration is optimized for Python/FastAPI projects. No changes needed!

### Django Projects
Add these patterns to `IGNORE_PATTERNS`:

`migrations`,
`static`,
`media`,
`staticfiles`,
`local_settings.py`,
`db.sqlite3`,

### Node.js/Express Projects
Add these patterns to `IGNORE_PATTERNS`:

```python
'node_modules',
'package-lock.json',
'npm-debug.log',
'yarn.lock',
'yarn-error.log',
'dist',
'coverage',
'.next',
'.nuxt',
```

### React/Vue Projects
Add these patterns to `IGNORE_PATTERNS`:

```python
'build',
'dist',
'.next',
'.nuxt',
'coverage',
'storybook-static',
'.env.local',
'.env.development.local',
'.env.test.local',
'.env.production.local',
```

### Laravel Projects
Add these patterns to `IGNORE_PATTERNS`:

```python
'vendor',
'node_modules',
'public/storage',
'public/hot',
'storage/.key',
'storage/framework',
'.env',
'Homestead.yaml',
'Homestead.json',
```


## Customization
To customize ignore patterns, edit the `IGNORE_PATTERNS` set at the top of the script:

```python
IGNORE_PATTERNS = {
'your_pattern_here',
'another_pattern',
# ...
}
```

## Output Example

```txt
.
├── src/
│   ├── controllers/
│   │   └── main.py
│   ├── models/
│   │   └── user.py
│   └── utils/
│   └── helpers.py
├── tests/
│   └── test_main.py
├── README.md
└── requirements.txt
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to use in any project! 📝
