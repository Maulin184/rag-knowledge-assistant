from backend.models.domain import RAGResponse


class RAGPipeline:

    def __init__(
        self,
        document_manager,
        loader,
        chunker,
        embedder,
        vector_store,
        retrieval_service,
        llm_service
    ):
        self.document_manager = document_manager
        self.loader = loader
        self.chunker = chunker
        self.embedder = embedder
        self.vector_store = vector_store
        self.retrieval_service = retrieval_service
        self.llm_service = llm_service

    def ingest_pdf(
        self,
        pdf_path: str
    ):

        document_info = (
            self.document_manager.register_document(
                pdf_path
            )
        )

        if document_info["already_exists"]:

            return document_info

        documents = self.loader.load_pdf(
            pdf_path
        )

        chunks = self.chunker.create_chunks(
            documents
        )

        embedded_chunks = (
            self.embedder.embed_documents(
                chunks
            )
        )

        self.vector_store.create_index(
            embedded_chunks
        )

        self.vector_store.save_index(
            document_info["document_id"]
        )

        return document_info

    def ask(
        self,
        document_id: str,
        question: str,
        chat_history=None
    ) -> RAGResponse:

        self.vector_store.load_index(
            document_id
        )

        retrieval_result = (
            self.retrieval_service.retrieve(
                question
            )
        )

        answer = (
            self.llm_service.generate_answer(
                question=question,
                context=retrieval_result.context,
                chat_history=chat_history
            )
        )

        return RAGResponse(
            answer=answer,
            sources=retrieval_result.retrieved_chunks
        )