#!/usr/bin/env python3
"""
Skrypt do eksportu notebooka Jupyter do formatu HTML
z zachowaniem wszystkich wykresów i outputów
"""

import nbformat
import os
from datetime import datetime

def export_notebook_to_html():
    """
    Eksportuje notebook do HTML używając podstawowej konwersji
    """
    # Ścieżki
    notebook_path = r"c:\Users\pksia\Dropbox\Rozwoj\AI\Data Science - UW\PracaDyplomowa\PracaDyplomowa_v3y.ipynb"
    output_path = r"c:\Users\pksia\Dropbox\Rozwoj\AI\Data Science - UW\PracaDyplomowa\PracaDyplomowa_v3y.html"
    
    try:
        # Próba 1: nbconvert z podstawowymi ustawieniami
        import subprocess
        import sys
        
        cmd = [
            sys.executable, '-m', 'jupyter', 'nbconvert',
            '--to', 'html',
            '--template', 'classic',  # Używa klasycznego szablonu
            '--embed-images',  # Osadza obrazy w HTML
            notebook_path,
            '--output', output_path
        ]
        
        print("🔄 Rozpoczynam eksport...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(f"✅ Sukces! Plik HTML został zapisany jako:")
            print(f"📄 {output_path}")
            return True
        else:
            print(f"❌ Błąd podczas eksportu: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Błąd: {e}")
        return False

def create_manual_html():
    """
    Tworzy podstawowy HTML z contentem notebooka
    """
    try:
        notebook_path = r"c:\Users\pksia\Dropbox\Rozwoj\AI\Data Science - UW\PracaDyplomowa\PracaDyplomowa_v3y.ipynb"
        output_path = r"c:\Users\pksia\Dropbox\Rozwoj\AI\Data Science - UW\PracaDyplomowa\PracaDyplomowa_Manual.html"
        
        # Wczytaj notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Podstawowy HTML template
        html_content = f"""
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Praca Dyplomowa - Predykcja Rotacji Pracowników</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fafafa;
        }}
        
        .cell {{
            margin-bottom: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        .cell-markdown {{
            padding: 20px;
        }}
        
        .cell-code {{
            border-left: 4px solid #007acc;
        }}
        
        .cell-code-input {{
            background-color: #f8f9fa;
            padding: 15px;
            font-family: 'Monaco', 'Courier New', monospace;
            font-size: 14px;
            overflow-x: auto;
            border-bottom: 1px solid #e1e4e8;
        }}
        
        .cell-code-output {{
            padding: 15px;
            background-color: white;
            border-left: 4px solid #28a745;
            margin-left: 4px;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 0;
        }}
        
        h1 {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            margin: -20px -20px 20px -20px;
            border-radius: 8px 8px 0 0;
        }}
        
        pre {{
            background-color: #f6f8fa;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }}
        
        code {{
            background-color: #f6f8fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Monaco', 'Courier New', monospace;
        }}
        
        .output-text {{
            font-family: monospace;
            white-space: pre-wrap;
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 4px;
            border: 1px solid #e1e4e8;
        }}
        
        .timestamp {{
            color: #6a737d;
            font-size: 12px;
            margin-bottom: 10px;
        }}
        
        .cell-number {{
            color: #0366d6;
            font-weight: bold;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="timestamp">
        Wygenerowano: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    </div>
"""
        
        # Przetwórz każdą komórkę
        for i, cell in enumerate(nb.cells, 1):
            if cell.cell_type == 'markdown':
                html_content += f"""
    <div class="cell cell-markdown">
        <div class="cell-number">Komórka {i} (Markdown)</div>
        <div>{cell.source}</div>
    </div>
"""
            elif cell.cell_type == 'code':
                # Kod input
                html_content += f"""
    <div class="cell cell-code">
        <div class="cell-number">Komórka {i} (Kod)</div>
        <div class="cell-code-input">
            <pre><code>{cell.source}</code></pre>
        </div>
"""
                
                # Outputs jeśli istnieją
                if hasattr(cell, 'outputs') and cell.outputs:
                    for output in cell.outputs:
                        if output.output_type == 'stream':
                            html_content += f"""
        <div class="cell-code-output">
            <div class="output-text">{output.text}</div>
        </div>
"""
                        elif output.output_type == 'execute_result' or output.output_type == 'display_data':
                            if 'text/plain' in output.data:
                                html_content += f"""
        <div class="cell-code-output">
                    <div class="output-text">{output.data['text/plain']}</div>
        </div>
"""
                
                html_content += "    </div>\n"
        
        html_content += """
</body>
</html>
"""
        
        # Zapisz HTML
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Manualny HTML został utworzony:")
        print(f"📄 {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Błąd podczas tworzenia manualnego HTML: {e}")
        return False

if __name__ == "__main__":
    print("🚀 EKSPORT NOTEBOOKA DO HTML")
    print("=" * 50)
    
    # Próba 1: Standardowy nbconvert
    print("\n🔧 Próba 1: Standardowy eksport nbconvert...")
    if export_notebook_to_html():
        print("✅ Eksport zakończony pomyślnie!")
    else:
        print("❌ Standardowy eksport nie powiódł się")
        
        # Próba 2: Manualny HTML
        print("\n🔧 Próba 2: Tworzenie prostego HTML...")
        if create_manual_html():
            print("✅ Manualny HTML został utworzony!")
        else:
            print("❌ Nie udało się utworzyć HTML")
    
    print("\n🎉 Gotowe! Sprawdź utworzone pliki HTML.")