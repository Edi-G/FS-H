# AI-Assistent for FS - UiA

Dette prosjektet utvikler en AI-basert assistent for å gi brukerveiledning til FS-systemet ved Universitetet i Agder (UiA). Ved å bruke Retrieval-Augmented Generation (RAG) og LlamaIndex, kombinerer vi relevant informasjon fra en omfattende kunnskapsbase med avanserte språkmodeller for å generere nøyaktige og relevante svar på brukerforespørsler.

## Kom i gang

Følg instruksjonene nedenfor for å sette opp prosjektet på din lokale maskin.

### Krav

- Python 3.7 eller høyere
- pip (Python package installer)

### Installering på Windows (PowerShell)

1. Opprett et virtuelt miljø:
    ```powershell
    python -m venv .venv
    ```

2. Aktiver det virtuelle miljøet:
    ```powershell
    .\.venv\Scripts\activate
    ```

3. Installer nødvendige pakker:
    ```powershell
    pip install -r requirements.txt
    ```

### Installering på macOS

1. Opprett et virtuelt miljø:
    ```bash
    python3 -m venv .venv
    ```

2. Aktiver det virtuelle miljøet:
    ```bash
    source .venv/bin/activate
    ```

3. Installer nødvendige pakker:
    ```bash
    pip install -r requirements.txt
    ```

### Bruk

Etter installasjonen kan du starte AI-assistenten ved å kjøre hovedskriptet:

```bash
streamlit run app.py