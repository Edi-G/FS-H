# FS-H

AI-basert assistent for å gi brukerveiledning til FS-systemet ved Universitetet i Agder (UiA). Dette prosjektet bruker Retrieval-Augmented Generation (RAG) og en vektor-database for å kombinere relevant informasjon fra en omfattende kunnskapsbase med avanserte språkmodeller, og generere nøyaktige og relevante svar på brukerforespørsler. Systemet er designet for å være skalerbart og effektivt, og kan håndtere komplekse forespørsler selv med begrensede maskinvarekrav.

## Innhold

- [Prosjektbeskrivelse](#prosjektbeskrivelse)
- [Installasjonsinstruksjoner](#installasjonsinstruksjoner)
  - [Windows (PowerShell)](#windows-powershell)
  - [macOS](#macos)
- [Mappestruktur](#mappestruktur)
- [Bruk](#bruk)
- [Bidra](#bidra)
- [Lisens](#lisens)
- [Kontakt](#kontakt)

## Prosjektbeskrivelse

Dette prosjektet utvikler en AI-assistent som gir brukerveiledning til FS-systemet ved UiA. Ved å bruke RAG og en vektor-database kan systemet gi presise svar basert på en stor kunnskapsbase. Systemet er optimalisert for effektiv informasjonsuthenting og nøyaktig kontekstualisering.

## Installasjonsinstruksjoner

Følg instruksjonene nedenfor for å sette opp prosjektet på din lokale maskin.

### Windows (PowerShell)

1. Opprett et virtuelt miljø:
    ```powershell
    python -m venv .venv
    ```

2. Tillat skriptkjøring i PowerShell:
    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    ```

3. Aktiver det virtuelle miljøet:
    ```powershell
    .\.venv\Scripts\activate
    ```

4. Installer nødvendige pakker:
    ```powershell
    pip install -r requirements.txt
    ```

### macOS

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

## Mappestruktur

- **AzureTest**: Inneholder tester og konfigurasjoner for integrering med Azure.
- **GPT-RAG**: Implementasjon og konfigurasjoner for GPT-modellen med RAG.
- **Llama-RAG**: Implementasjon og konfigurasjoner for Llama-modellen med RAG.

## Bruk

Etter installasjonen kan du starte AI-assistenten ved å kjøre hovedskriptet i den relevante mappen:

```bash
python main.py
