
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2] / 'pages'
def write(lang, path, body, title=None, description=None, published=None):
    p = ROOT / lang / f'{path}.md'
    head, _ = p.read_text().split('\n---\n\n', 1)
    lines = head.split('\n')
    import json
    for i, l in enumerate(lines):
        if title and l.startswith('title: '): lines[i] = 'title: ' + json.dumps(title, ensure_ascii=False)
        if description and l.startswith('description: '): lines[i] = 'description: ' + json.dumps(description, ensure_ascii=False)
        if published is not None and l.startswith('published: '): lines[i] = 'published: ' + json.dumps(published)
    p.write_text('\n'.join(lines) + '\n---\n\n' + body.strip('\n') + '\n')
    print('écrit', lang, path)
def table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
    out += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    return '\n'.join(out)
