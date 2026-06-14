from backend.core.document_loader import DocumentLoader


def main():

    loader = DocumentLoader()

    documents = loader.load_pdf(
        "brief_ml_notes.pdf"
    )

    print("=" * 50)
    print(f"Pages Loaded: {len(documents)}")
    print("=" * 50)

    first_page = documents[1]

    print(f"Source      : {first_page.source}")
    print(f"Page        : {first_page.page}")
    print(f"Total Pages : {first_page.total_pages}")

    print("\nPreview:\n")

    print(first_page.content[:500])


if __name__ == "__main__":
    main()