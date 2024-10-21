from typing import Any, Optional

from pydantic import BaseModel


class ChunkingStrategyStatic(BaseModel):
    max_chunk_size_tokens: int
    chunk_overlap_tokens: int

class ChunkingStrategy(BaseModel):
    type: str
    static: Optional[ChunkingStrategyStatic] = None

class VectorStoreFileAttachResponse(BaseModel):
    id: Optional[str] = None
    object: Optional[str] = None
    usage_bytes: Optional[int] = 0
    created_at: Optional[int] = 0
    vector_store_id: Optional[str] = None
    status: Optional[str] = None
    last_error: Optional[Any] = None
    chunking_strategy: Optional[ChunkingStrategy] = None

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> 'VectorStoreFileAttachResponse':
        chunking_strategy_data = data.get('chunking_strategy')
        static_data = chunking_strategy_data.get('static') if chunking_strategy_data else None
        chunking_strategy = ChunkingStrategy(
            type=chunking_strategy_data['type'],
            static=ChunkingStrategyStatic(**static_data) if static_data else None
        ) if chunking_strategy_data else None

        return cls(
            id=data.get('id', ''),
            object=data.get('object', ''),
            usage_bytes=data.get('usage_bytes', 0),
            created_at=data.get('created_at', 0),
            vector_store_id=data.get('vector_store_id', ''),
            status=data.get('status', ''),
            last_error=data.get('last_error', None),
            chunking_strategy=chunking_strategy
        )



