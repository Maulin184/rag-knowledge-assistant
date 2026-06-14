from frontend.services.api_client import (
    APIClient
)


def main():

    client = APIClient()

    print(
        "\nGetting documents...\n"
    )

    documents = (
        client.get_documents()
    )

    print(
        documents
    )

    print(
        "\nAPI Client Test Passed"
    )


if __name__ == "__main__":
    main()